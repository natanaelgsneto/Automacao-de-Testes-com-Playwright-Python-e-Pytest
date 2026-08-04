# 🚀 Automação de Testes com Playwright, Python e Pytest

Projeto desenvolvido para estudos de automação de testes utilizando **Python**, **Playwright** e **Pytest**.

---

# 📥 1. Clonando o Repositório

Abra o terminal (PowerShell, CMD ou Git Bash) e clone o repositório:

```bash
git clone https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git
cd Automacao-de-Testes-com-Playwright-Python-e-Pytest
```

---

# ⚙️ 2. Configurando o Ambiente do Projeto

Acesse a pasta onde estão as configurações do projeto:

```bash
cd PageObjects
```

## Passo 1 – Criar o ambiente virtual

```bash
uv venv
```

---

## Passo 2 – Ativar o ambiente virtual

### Windows (PowerShell)

```powershell
.venv\Scripts\Activate.ps1
```

### Git Bash / Linux / macOS

```bash
source .venv/bin/activate
```

---

## Passo 3 – Instalar as dependências

```bash
uv pip install pytest pytest-playwright playwright
```

---

## Passo 4 – Instalar os navegadores do Playwright

```bash
uv run playwright install
```

---

# 📂 Estrutura do Projeto

```text
Automacao-de-Testes-com-Playwright-Python-e-Pytest/
│
├── PageObjects/
│   ├── .venv/                 # Ambiente virtual
│   ├── Tests/
│   │   ├── Treinamento/       # Exercícios e exemplos
│   │   └── test_first.py      # Primeiro teste
│   └── pyproject.toml         # Configurações do projeto
│
└── README.md                  # Documentação
```

---

# ▶️ 3. Executando os Testes

## Executar todos os testes (Headless)

Executa os testes em segundo plano, sem abrir o navegador.

```bash
uv run pytest
```

---

## Executar todos os testes (Headed)

Executa os testes abrindo a janela do navegador.

```bash
uv run pytest --headed
```

---

## Executar um teste específico

```bash
uv run pytest Tests/test_first.py --headed
```

---

# 🔧 4. Configurando o PyCharm

Para que os testes sejam executados com o navegador aberto ao clicar no botão **▶ Play**:

1. Clique no menu suspenso ao lado do botão **▶ Play**.
2. Selecione **Edit Configurations...**
3. No campo **Additional pytest options** (ou **Additional arguments**), informe:

```text
--headed
```

4. Clique em **Apply**.
5. Clique em **OK**.

---

# 🐞 5. Depuração com o Playwright Inspector

O método `page.pause()` interrompe a execução do teste e abre o **Playwright Inspector**, permitindo inspecionar elementos, criar seletores e acompanhar a execução da automação.

## Exemplo

```python
from playwright.sync_api import Page

def test_exemplo(page: Page):
    page.goto("https://www.google.com")

    page.pause()

    page.get_by_role("textbox").fill("Playwright")
```

## Durante a pausa é possível

- 🔍 Inspecionar elementos da página.
- 🎯 Capturar seletores automaticamente.
- ▶️ Continuar a execução clicando em **Resume**.
- ⏭️ Executar passo a passo (**Step Over**).
- 🧪 Validar seletores antes de utilizá-los no código.

---

# 💡 Dicas

- Mantenha o ambiente virtual sempre ativado.
- Execute `uv run playwright install` apenas na primeira configuração ou quando atualizar o Playwright.
- Utilize `page.pause()` apenas durante a depuração.
- Antes de finalizar os testes, remova ou comente `page.pause()` para evitar interrupções durante a execução automática.

---

# 🛠️ Tecnologias Utilizadas

- Python
- Playwright
- Pytest
- pytest-playwright
- uv
- PyCharm

---

# 📚 Referências

- Playwright
- Pytest
- Python
