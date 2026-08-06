Juntei tudo em um único README completo, com a ordem correta (do zero até execução, debug, POM, relatórios e CI/CD).

Crie/substitua seu arquivo:

```text
README.md
```

pelo conteúdo abaixo:

```markdown
# 🚀 Automação de Testes com Playwright, Python e Pytest

Projeto desenvolvido para estudos e prática de **Automação de Testes Web** utilizando:

- 🐍 Python
- 🎭 Playwright
- 🧪 Pytest
- ⚡ uv
- 💻 PyCharm
- 🔧 Git/GitHub

O objetivo deste projeto é demonstrar a criação de testes automatizados, organização de código, boas práticas de QA Automation e execução de testes utilizando Playwright com Pytest.

---

# 📌 Objetivos do Projeto

Neste projeto são praticados:

- Navegação em páginas Web
- Localizadores (Locators)
- get_by_role
- get_by_label
- get_by_text
- XPath e CSS Selector
- Click
- Double Click
- Hover
- Fill
- Type
- Select Option
- Checkbox
- Radio Button
- Assertions
- Esperas automáticas
- Page Object Model
- Playwright Inspector
- Execução com Pytest

---

# ✅ Pré-requisitos

Antes de iniciar, tenha instalado:

## Python

Recomendado:

```

Python 3.12+

````

Verificar:

```bash
python --version
````

---

## Git

Verificar:

```bash
git --version
```

---

## uv

O projeto utiliza o **uv** para criar ambientes virtuais e gerenciar dependências.

Verificar:

```bash
uv --version
```

Instalar:

```bash
pip install uv
```

---

# 📥 1. Clonando o Repositório

Abra o terminal:

PowerShell, CMD ou Git Bash.

Clone o projeto:

```bash
git clone https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git
```

Entre na pasta:

```bash
cd Automacao-de-Testes-com-Playwright-Python-e-Pytest
```

---

# ⚙️ 2. Configurando o Ambiente do Projeto

## Criar ambiente virtual

Na raiz do projeto:

```bash
uv venv
```

Será criada a pasta:

```
.venv/
```

---

## Ativar ambiente virtual

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

### Git Bash / Linux / macOS

```bash
source .venv/bin/activate
```

---

# 📦 3. Instalar Dependências

Instalar tudo:

```bash
uv pip install pytest pytest-playwright playwright
```

---

# 🌐 4. Instalar Navegadores do Playwright

Executar:

```bash
uv run playwright install
```

Este comando instala:

* Chromium
* Firefox
* WebKit

---

# 📂 5. Estrutura do Projeto

Exemplo:

```
Automacao-de-Testes-com-Playwright-Python-e-Pytest
│
├── .venv/
│   └── Ambiente virtual
│
├── pages/
│   ├── login_page.py
│   └── home_page.py
│
├── tests/
│   │
│   ├── Command/
│   │   └── hover.py
│   │
│   ├── fill/
│   │   └── checkanduncheck.py
│   │
│   ├── Expect/
│   │   └── expect.py
│   │
│   └── test_first.py
│
├── pyproject.toml
│
├── .gitignore
│
└── README.md
```

---

# 🧪 6. Pytest + Playwright

O pytest-playwright fornece automaticamente a fixture:

```
page
```

Ela cria uma página do navegador para cada teste.

Exemplo:

```python
from playwright.sync_api import Page


def test_google(page: Page):

    page.goto(
        "https://google.com"
    )
```

---

# ▶️ 7. Executando os Testes

## Executar todos os testes

Modo invisível:

```bash
uv run pytest
```

Este modo é chamado:

```
Headless
```

O navegador roda em segundo plano.

---

# 🌎 Executar abrindo o navegador

```bash
uv run pytest --headed
```

## O que significa --headed?

O parâmetro:

```
--headed
```

faz o navegador abrir na tela durante a execução.

Com ele é possível:

✅ acompanhar os passos do teste
✅ visualizar cliques e preenchimentos
✅ encontrar erros visualmente
✅ utilizar o Playwright Inspector

---

# Executar teste específico

Exemplo:

```bash
uv run pytest tests/test_first.py --headed
```

---

# Executar apenas uma função

Exemplo:

Arquivo:

```
hover.py
```

Função:

```python
def test_hover(page):
```

Comando:

```bash
uv run pytest tests/Command/hover.py::test_hover --headed
```

---

# 💻 8. Configurando PyCharm

Para executar com navegador aberto pelo botão ▶ Play:

1. Abrir:

```
Run
```

2. Selecionar:

```
Edit Configurations...
```

3. Escolher:

```
pytest
```

4. Em:

```
Additional pytest options
```

Adicionar:

```
--headed
```

5. Clique:

```
Apply → OK
```

Agora ao clicar em ▶ o navegador abrirá.

---

# 🐞 9. Playwright Inspector

Para depuração utilize:

```python
page.pause()
```

Exemplo:

```python
from playwright.sync_api import Page


def test_exemplo(page: Page):

    page.goto(
        "https://google.com"
    )

    page.pause()

    page.get_by_role(
        "textbox"
    ).fill(
        "Playwright"
    )
```

---

Durante a pausa é possível:

🔍 Inspecionar elementos

🎯 Criar seletores automaticamente

▶ Resume

⏭ Step Over

🧪 Validar Locators

---

# 🏗️ 10. Page Object Model (POM)

O projeto utiliza o padrão:

```
Page Object Model
```

Objetivo:

* Separar páginas dos testes
* Evitar código duplicado
* Facilitar manutenção

Exemplo:

```
pages/

login_page.py
```

Código:

```python
class LoginPage:

    def __init__(self,page):
        self.page = page


    def acessar(self):

        self.page.goto(
            "https://site.com/login"
        )
```

---

# 📊 11. Relatório HTML

Instalar:

```bash
uv pip install pytest-html
```

Executar:

```bash
uv run pytest --html=report.html
```

Será criado:

```
report.html
```

---

# 📸 12. Evidências de Teste

O Playwright permite:

* Screenshot
* Vídeo
* Trace

Exemplo:

```bash
uv run pytest --tracing on
```

---

# 🚀 13. CI/CD GitHub Actions

Fluxo:

```
Código
 |
Git Commit
 |
GitHub
 |
GitHub Actions
 |
Pytest
 |
Resultado
```

Benefícios:

* Execução automática
* Validação do código
* Integração contínua

---

# 🧹 14. Arquivo .gitignore

Criar:

```
.gitignore
```

Adicionar:

```
.venv/

__pycache__/

.pytest_cache/

*.pyc

.idea/

report.html
```

---

# 💡 15. Boas Práticas

✅ Usar nomes claros nos testes

✅ Criar Page Objects

✅ Usar Locators estáveis

✅ Evitar código duplicado

✅ Remover `page.pause()` antes da entrega

✅ Manter dependências atualizadas

---

# 🛠️ Tecnologias Utilizadas

| Tecnologia        | Uso                     |
| ----------------- | ----------------------- |
| Python            | Linguagem               |
| Playwright        | Automação Web           |
| Pytest            | Execução dos testes     |
| pytest-playwright | Integração              |
| uv                | Ambiente e dependências |
| PyCharm           | IDE                     |
| Git/GitHub        | Versionamento           |

---

# 📚 Referências

Playwright:

[https://playwright.dev/](https://playwright.dev/)

Pytest:

[https://docs.pytest.org/](https://docs.pytest.org/)

Python:

[https://www.python.org/](https://www.python.org/)

---

# 👨‍💻 Autor

Projeto desenvolvido para estudos de:

**QA Automation
Python + Playwright + Pytest**

```

Esse arquivo já está no formato de **README de portfólio para GitHub**.
```
