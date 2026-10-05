# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

Study project for web test automation with Playwright + Pytest (Python, sync API) against https://automationexercise.com/. Code, comments, and identifiers are in Portuguese — keep new code in Portuguese to match.

## Commands

The environment is managed with `uv` (venv at `.venv/`).

```bash
uv run playwright install chromium                       # browsers (first time)
uv run pytest                                            # runs PageObjects/Tests (testpaths in pytest.ini)
uv run pytest PageObjects/Tests/test_autenticacao.py::test_login -v
uv run pytest PageObjects/Tests/test_adicionar_produtos_ao_carrinho.py --slowmo=1000 -v -s
uv run pytest test_validacao_banco.py                    # files outside testpaths must be passed explicitly
```

Trace files (`trace.zip`) are viewed by uploading them to trace.playwright.dev.

## How the test run is configured (non-obvious)

- `pytest.ini` always adds `--headed --base-url=https://automationexercise.com/`, so `page.goto("/login")` resolves against the site; tests open visible browser windows by default.
- Root `conftest.py` overrides `browser_context_args` to emulate an **iPhone 12** for every test. Locators and layouts are therefore the mobile version of the site — keep this in mind when a selector works in a desktop browser but fails in tests.
- `pythonpath = . PageObjects`, so both import styles resolve and both are used: `from Page.produtos import Produtos` and `from PageObjects.Page.produtos import Produtos`.
- Only `test_*.py` files under `PageObjects/Tests` are collected by default. Many files under `Tests/Command`, `Tests/Expec`, `Tests/fill`, `Tests/dbclick`, `Tests/Treinamento` are practice scripts not named `test_*`, so they are not collected. `ValidacaoBanco/`, `auth/`, and the root `test_validacao_banco.py` are outside `testpaths`.

## Architecture

- **Page Object Model** in `PageObjects/Page/`: `BasePage` (navigation helpers using relative URLs) is subclassed by `CadastroLogin`; `Produtos` and `Carrinho` take a `page` directly. Page objects expose locators as attributes (built in `__init__`) plus action/validation methods that use `expect`. Tests in `PageObjects/Tests/` instantiate page objects with the pytest-playwright `page` fixture.
- **Utilities** in `PageObjects/Page/utilitarios/` (the canonical package — `utilities/` holds an older, diverging copy of `comparador_de_arquivos.py`):
  - `comparador_de_arquivos.py` — compares base vs. current TXT/PDF/Excel files (pandas, PyPDF2); sample files live in `PageObjects/Arquivos/` (`base.*` / `atual.*`). Run via `PageObjects/Page/executar_comparacao.py` / `executar_comparacaoExcel.py`.
  - `bancos_dados.py` — DB validation helpers on SQLAlchemy (`criar_engine`, `montar_connection_string`, `registro_existe`, `contar_registros`, `validar_valor_coluna`, ...); SQLite sample DB at `stores/loja.db` (tables `usuarios`, `produtos`), seeded by the scripts in `ValidacaoBanco/`.
- **Authenticated session**: `auth/setup_auth.py` logs in and saves `storage_state` to `auth/state.json` for reuse.

## Known pitfalls

- `ValidacaoBanco/test_validar_banco.py` imports `PageObjects.Page.utilities.bancosDeDados`, which does not exist — the module is `PageObjects.Page.utilitarios.bancos_dados`.
- `utilitarios/__init_.py` has a typo (single trailing underscore), so it is not a real package init; imports work only through implicit namespace packages.
- `requirements.txt` is UTF-16 encoded and omits pandas, PyPDF2, and SQLAlchemy, which the utilities need; `PageObjects/pyproject.toml` declares no dependencies.
- There is no `.gitignore`: `__pycache__/`, traces, videos, `relatorio.html`, and auth state files are committed. Don't add new generated artifacts to commits.
