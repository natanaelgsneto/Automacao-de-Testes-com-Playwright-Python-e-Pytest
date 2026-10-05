---
name: gerar-teste
description: Gera um teste automatizado Playwright + Pytest para uma página do automationexercise.com seguindo o Page Object Model do projeto. Usar quando o usuário pedir para criar, gerar ou escrever um teste (ou cenários de teste) para uma página ou funcionalidade do site.
argument-hint: "[página ou funcionalidade] [cenários desejados]"
---

# Gerar teste com Playwright + Pytest

Pedido: $ARGUMENTS

Gere o teste em Python com Playwright (API síncrona) e Pytest, seguindo os passos abaixo na ordem.

## 1. Analisar a página com o Playwright MCP

Antes de escrever código, navegue até a página com as ferramentas `mcp__playwright__*` (`browser_navigate`, `browser_snapshot`, `browser_fill_form`, `browser_click`, `browser_evaluate`):

- Confirme os papéis (role), nomes acessíveis, placeholders e textos dos elementos que o teste vai usar.
- Execute o fluxo de cada cenário no navegador e anote o que a página realmente mostra: URL final, mensagens de sucesso e de erro (texto exato).
- Verifique atributos de validação dos campos (`type`, `required`): quando o próprio navegador bloqueia o envio do formulário, o site não responde nada e o teste deve conferir a validação HTML5, não uma mensagem do site.
- Os testes rodam emulando um **iPhone 12** (ver `conftest.py`). Se o layout importar, confira a página com `browser_resize` em 390x664.
- Um navegador já logado é redirecionado de `/login` para a home. Se o MCP estiver logado, acesse `/logout` antes de analisar telas de login/cadastro.
- Feche o navegador com `browser_close` ao terminar. Não apague a pasta `.playwright-mcp/` que o MCP gera.

Nunca invente seletores ou mensagens: use apenas o que foi confirmado na página.

## 2. Page Object em `PageObjects/Page/`

- Reaproveite o Page Object existente da página antes de criar outro (ex.: `Cadastro_login.py` → `CadastroLogin`, `produtos.py` → `Produtos`, `carrinho.py` → `Carrinho`). Leia o arquivo antes de editar.
- Página nova: crie `PageObjects/Page/<nome_da_pagina>.py` com uma classe que herda de `BasePage` (`from Page.base_page import BasePage`), recebe `page` no `__init__` e chama `super().__init__(page)`.
- Navegação usa URLs relativas (`self.page.goto("/products")`), pois o `pytest.ini` define `--base-url=https://automationexercise.com/`. Coloque métodos de navegação reutilizáveis no `BasePage`.
- Declare os locators como atributos no `__init__`; ações e validações viram métodos.
- Assertions de página ficam em métodos `validar_...` do Page Object, usando `expect()`.

## 3. Seletores

Ordem de preferência:

1. `get_by_role("button", name="Login")`, `get_by_role("link", name="Cart")`, `get_by_role("textbox", name="Password")`
2. `get_by_placeholder("Email Address")`
3. `get_by_text("Your email or password is incorrect!")`

- Quando o mesmo elemento aparece mais de uma vez na página, restrinja pelo contêiner em vez de usar índice ou CSS: `self.page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address")`.
- Evite seletores CSS frágeis (classes de layout, `nth-child`, caminhos longos) e XPath. Use CSS ou `data-qa` só quando não houver role, placeholder ou texto que identifique o elemento, e explique o motivo num comentário.

## 4. Teste em `PageObjects/Tests/`

- Arquivo `PageObjects/Tests/test_<funcionalidade>.py` e funções `test_<cenario>`: só arquivos e funções com prefixo `test_` são coletados.
- Use a fixture `page` do pytest-playwright. Não crie `browser`, `context` nem `page` manualmente.
- Importe os Page Objects como os testes existentes: `from Page.Cadastro_login import CadastroLogin`.
- Cada teste é independente: abre a própria página, faz o próprio setup e não depende da ordem nem do estado deixado por outro teste.
- Cenários com o mesmo fluxo e entradas diferentes usam `@pytest.mark.parametrize` com `pytest.param(..., id="nome-do-cenario")`.
- Credenciais vêm da fixture `credenciais_login` do `conftest.py` raiz (`email, senha = credenciais_login`), que lê `LOGIN_EMAIL` e `LOGIN_SENHA`. Nunca escreva email ou senha reais no código.
- Assertions com `expect()` do Playwright (`to_be_visible`, `to_have_text`, `to_have_url`, `to_be_hidden`), não `assert` sobre valores lidos da página, pois `expect()` espera o elemento automaticamente. Para URLs, use `re.compile(r"/caminho$")`.
- Não use `page.pause()` nem `page.wait_for_timeout()` em testes finais.

## 5. Nomenclatura

- snake_case em português para tudo o que você criar: arquivos, funções, métodos, variáveis e fixtures (`acessar_produtos`, `validar_produto_no_carrinho`, `test_adicionar_produto_ao_carrinho`).
- Classes em PascalCase em português (`Produtos`, `Carrinho`).
- O `CadastroLogin` já tem métodos em camelCase (`fazerLogin`, `validarLoginComSucesso`). Use-os como estão, sem renomear, a menos que o usuário peça.
- Comentários em português, como no restante do projeto.

## 6. Executar e validar

Rode o teste criado no modo headed:

```bash
.venv/Scripts/python -m pytest PageObjects/Tests/test_<funcionalidade>.py --headed -v
```

- Se `uv` estiver disponível, `uv run pytest ... --headed -v` também funciona.
- Testes que fazem login precisam de `LOGIN_EMAIL` e `LOGIN_SENHA` definidas no ambiente.
- Se pytest rejeitar `--headed`/`--base-url`, faltam `pytest-playwright` e `pytest-base-url` no `.venv`. Avise o usuário antes de instalar.
- Se um teste falhar, investigue a causa na página com o MCP e corrija. Não enfraqueça a assertion para o teste passar.
- Para cenários negativos, confirme que o teste falha quando deveria (por exemplo, rodando com dados que tornam a condição falsa).

Ao final, informe os arquivos criados ou alterados, os cenários cobertos e o resultado da execução. Não faça commit nem push sem o usuário pedir.
