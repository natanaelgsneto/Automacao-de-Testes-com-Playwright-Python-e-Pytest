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

# 📑 Índice

- Objetivos do Projeto
- Pré-requisitos
- Clonando o Repositório
- Configurando o Ambiente
- Instalando Dependências
- Instalando os Navegadores
- Estrutura do Projeto
- Primeiro Teste
- Executando os Testes
- Playwright Inspector
- Locators
- Principais Comandos
- Auto Wait
- Assertions
- Fixtures
- Page Object Model (POM)
- Relatórios HTML
- Evidências de Teste
- GitHub Actions (CI/CD)
- Arquivo .gitignore
- Boas Práticas
- Roadmap
- Tecnologias Utilizadas
- Referências
- Autor

---

# 📌 Objetivos do Projeto

Neste projeto são praticados:

- Navegação em páginas Web
- Localizadores (Locators)
- `get_by_role`
- `get_by_label`
- `get_by_text`
- `get_by_placeholder`
- CSS Selector
- XPath
- Click
- Double Click
- Hover
- Fill
- Type
- Keyboard
- Mouse
- Select Option
- Checkbox
- Radio Button
- Upload de arquivos
- Download de arquivos
- Assertions
- Esperas automáticas
- Fixtures
- Page Object Model (POM)
- Playwright Inspector
- Screenshots
- Relatórios
- Execução com Pytest

---

# 🎯 O que é o Playwright?

O **Playwright** é um framework de automação de testes desenvolvido pela Microsoft.

Ele permite automatizar navegadores modernos como:

- Chromium
- Firefox
- WebKit

Possui recursos avançados como:

- Esperas automáticas
- Execução paralela
- Auto Wait
- Captura de screenshots
- Gravação de vídeos
- Trace Viewer
- Playwright Inspector

---

# 🎯 O que é o Pytest?

O **Pytest** é um framework para criação e execução de testes em Python.

Ele fornece recursos como:

- Fixtures
- Parametrização
- Relatórios
- Organização dos testes
- Execução paralela
- Plugins

Neste projeto, o Pytest é utilizado juntamente com o Playwright.

---

# ⚡ O que é o uv?

O **uv** é um gerenciador moderno para projetos Python.

Ele permite:

- Criar ambientes virtuais
- Instalar dependências
- Executar comandos Python
- Gerenciar versões

É muito mais rápido que o pip tradicional.

---

# ✅ Pré-requisitos

Antes de iniciar, tenha instalado:

## 🐍 Python

Recomendado:

```
Python 3.12+
```

Download:

https://www.python.org/

Durante a instalação marque:

```
☑ Add Python to PATH
```

Verificar instalação:

```bash
python --version
```

Exemplo:

```text
Python 3.12.5
```

---

## 🔧 Git

Download:

https://git-scm.com/

Verificar instalação:

```bash
git --version
```

Exemplo:

```text
git version 2.49.0
```

---

## 💻 PyCharm

Download:

https://www.jetbrains.com/pycharm/

Recomendado:

- PyCharm Community Edition
- Plugin Python habilitado

---

## ⚡ uv

Instalar:

```bash
pip install uv
```

Verificar:

```bash
uv --version
```

Exemplo:

```text
uv 0.8.x
```

---

# 📥 1. Clonando o Repositório

Abra o terminal:

- PowerShell
- CMD
- Git Bash

Clone o projeto:

```bash
git clone https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git
```

Entre na pasta:

```bash
cd Automacao-de-Testes-com-Playwright-Python-e-Pytest
```

---

# ⚙️ 2. Configurando o Ambiente

## Criando ambiente virtual

Na raiz do projeto execute:

```bash
uv venv
```

Será criada a pasta:

```text
.venv/
```

Estrutura:

```text
Projeto
│
├── .venv/
└── README.md
```

---

## Ativando ambiente virtual

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

Resultado esperado:

```text
(.venv)
```

### Git Bash / Linux / macOS

```bash
source .venv/bin/activate
```

---

# 📦 3. Instalando Dependências

Instalar todas as dependências:

```bash
uv pip install pytest pytest-playwright playwright
```

Bibliotecas instaladas:

| Biblioteca | Função |
|------------|---------|
| pytest | Framework de testes |
| playwright | Automação Web |
| pytest-playwright | Integração Playwright + Pytest |

Verificar instalação:

```bash
uv pip list
```

---

# 🌐 4. Instalando os Navegadores

Executar:

```bash
uv run playwright install
```

Serão instalados:

- Chromium
- Firefox
- WebKit

Instalar apenas o Chromium:

```bash
uv run playwright install chromium
```

Instalar apenas Firefox:

```bash
uv run playwright install firefox
```

Instalar apenas WebKit:

```bash
uv run playwright install webkit
```

Verificar a instalação executando um teste simples posteriormente.

---

# 📂 5. Estrutura do Projeto

Estrutura recomendada:

```text
Automacao-de-Testes-com-Playwright-Python-e-Pytest
│
├── .venv/
│
├── pages/
│   ├── login_page.py
│   ├── home_page.py
│   └── products_page.py
│
├── tests/
│   │
│   ├── Command/
│   │   ├── click.py
│   │   ├── hover.py
│   │   ├── fill.py
│   │   └── dragdrop.py
│   │
│   ├── Locator/
│   │   ├── role.py
│   │   ├── text.py
│   │   ├── label.py
│   │   └── xpath.py
│   │
│   ├── Expect/
│   │   └── expect.py
│   │
│   ├── test_login.py
│   ├── test_home.py
│   └── test_first.py
│
├── pyproject.toml
├── .gitignore
└── README.md
```

---

# 🧪 6. Primeiro Teste Automatizado

Crie o arquivo:

```text
tests/test_first.py
```

Código:

```python
from playwright.sync_api import Page

def test_google(page: Page):

    page.goto(
        "https://google.com"
    )
```

O teste acima:

- abre o navegador;
- acessa o Google;
- finaliza automaticamente ao término da execução.

---

➡️ **Continua na PARTE 2**, onde serão abordadas a execução dos testes, `--headed`, `uv run pytest`, execução de arquivos específicos, `-k`, `-v`, `--browser` e muito mais.
# ▶️ 7. Executando os Testes

Após configurar o ambiente e instalar as dependências, já é possível executar os testes automatizados.

---

## Executar todos os testes

Na raiz do projeto execute:

```bash
uv run pytest
```

O Pytest localizará automaticamente todos os arquivos que seguem o padrão:

```text
test_*.py

*_test.py
```

Exemplo:

```text
tests/
│
├── test_first.py
├── test_login.py
└── test_home.py
```

---

## O que acontece quando executamos?

Ao executar:

```bash
uv run pytest
```

O Pytest:

1. Localiza os arquivos de teste.
2. Cria um navegador.
3. Executa cada teste.
4. Fecha o navegador.
5. Exibe o resultado.

Exemplo:

```text
============================
3 passed in 4.82s
============================
```

---

# 🕶 Execução Headless

Por padrão o Playwright executa em:

```
Headless
```

Ou seja:

- navegador invisível
- maior velocidade
- ideal para CI/CD
- ideal para servidores

---

# 🌎 Abrindo o navegador

Para visualizar a automação execute:

```bash
uv run pytest --headed
```

Agora será possível acompanhar:

- abertura do navegador
- preenchimento de campos
- cliques
- navegação
- encerramento

---

# 🎯 O que significa --headed?

O parâmetro

```text
--headed
```

informa ao Playwright que o navegador deve abrir normalmente.

Muito utilizado para:

- estudar automação
- encontrar erros
- gravar vídeos
- utilizar o Inspector

---

# 🌐 Escolhendo o navegador

Chromium

```bash
uv run pytest --headed --browser chromium
```

Firefox

```bash
uv run pytest --headed --browser firefox
```

WebKit

```bash
uv run pytest --headed --browser webkit
```

---

# 🚀 Executar apenas um arquivo

Exemplo:

```bash
uv run pytest tests/test_first.py --headed
```

Outro exemplo:

```bash
uv run pytest tests/test_login.py --headed
```

---

# 📂 Executar uma pasta inteira

Executando todos os testes da pasta Command:

```bash
uv run pytest tests/Command --headed
```

Executando todos os testes da pasta Expect:

```bash
uv run pytest tests/Expect --headed
```

---

# 📁 Entrando na pasta do teste

Também é possível executar entrando na pasta.

```bash
cd tests/Command
```

Agora execute:

```bash
uv run pytest hover.py --headed
```

---

# 🎯 Executar uma função específica

Arquivo:

```text
hover.py
```

Função:

```python
def test_hover(page):
```

Executar:

```bash
uv run pytest hover.py::test_hover --headed
```

Outro exemplo:

```python
def test_menu(page):

def test_login(page):

def test_logout(page):
```

Executar apenas login:

```bash
uv run pytest test_login.py::test_login --headed
```

---

# 🏗 Executar uma classe específica

Arquivo:

```python
class TestLogin:

    def test_login(self, page):
        ...

    def test_logout(self, page):
        ...
```

Executar apenas a classe:

```bash
uv run pytest test_login.py::TestLogin --headed
```

---

# 🔍 Executar um método específico

```bash
uv run pytest test_login.py::TestLogin::test_login --headed
```

---

# 🔎 Executar utilizando -k

O parâmetro:

```text
-k
```

executa testes pelo nome.

Exemplo:

```bash
uv run pytest -k hover
```

Executa todos os testes contendo:

```
hover
```

Outro exemplo:

```bash
uv run pytest -k login
```

Também funciona com expressões:

```bash
uv run pytest -k "login or cadastro"
```

```bash
uv run pytest -k "not login"
```

---

# 🏷 Executar utilizando marcadores

Criando marcador:

```python
import pytest

@pytest.mark.login
def test_login(page):
    ...
```

Executar:

```bash
uv run pytest -m login
```

---

# 📈 Execução Verbose

Modo detalhado:

```bash
uv run pytest -v
```

Saída:

```text
tests/test_login.py::test_login PASSED

tests/test_home.py::test_home PASSED
```

---

# ⚡ Execução silenciosa

```bash
uv run pytest -q
```

---

# 🐢 Execução lenta

Excelente para estudos.

```bash
uv run pytest --headed --slowmo 500
```

Cada ação aguardará:

```
500 ms
```

Outro exemplo:

```bash
uv run pytest --headed --slowmo 1000
```

Agora cada ação aguardará:

```
1 segundo
```

---

# ⏱ Configurando Timeout

Timeout padrão:

```
30 segundos
```

Alterando:

```python
page.set_default_timeout(60000)
```

Agora o timeout será:

```
60 segundos
```

---

# 📌 Executando múltiplos arquivos

```bash
uv run pytest tests/test_login.py tests/test_home.py --headed
```

---

# 📋 Executando por diretório

```bash
uv run pytest tests
```

ou

```bash
uv run pytest tests --headed
```

---

# 🧪 Executando novamente apenas os testes que falharam

```bash
uv run pytest --lf
```

---

# ♻ Executando os testes que falharam primeiro

```bash
uv run pytest --ff
```

---

# 🛑 Parar na primeira falha

```bash
uv run pytest -x
```

---

# 🔢 Parar após duas falhas

```bash
uv run pytest --maxfail=2
```

---

# 📊 Exibir resumo detalhado

```bash
uv run pytest -ra
```

---

# 🖥 Executando pelo PyCharm

Clique com o botão direito no arquivo de teste.

Escolha:

```
Run 'pytest in ...'
```

Ou utilize o botão:

```
▶ Run
```

---

# ⚙ Configurando o botão ▶ do PyCharm

Abra:

```
Run
```

Depois:

```
Edit Configurations...
```

Selecione:

```
pytest
```

No campo:

```
Additional pytest options
```

Adicione:

```text
--headed
```

Caso queira abrir sempre no Chromium:

```text
--headed --browser chromium
```

Clique em:

```
Apply

OK
```

Agora, ao clicar em **▶ Run**, o navegador será aberto automaticamente.

---

# 💡 Dicas importantes

✔ Utilize `--headed` durante o desenvolvimento.

✔ Utilize modo Headless em produção e pipelines de CI/CD.

✔ Execute apenas um arquivo quando estiver desenvolvendo uma funcionalidade.

✔ Utilize `-k` para economizar tempo executando apenas o teste desejado.

✔ Utilize `-v` para visualizar detalhes da execução.

✔ Utilize `--slowmo` quando estiver aprendendo Playwright.

✔ Utilize `pytest -x` para interromper a execução ao encontrar a primeira falha.

---

➡️ **Continua na PARTE 3**, onde serão abordados:

- Playwright Inspector
- `page.pause()`
- `PWDEBUG`
- Todos os Locators
- CSS Selector
- XPath
- Auto Wait
- Assertions (`expect`)
- Boas práticas para localização de elementos
  # 🐞 8. Playwright Inspector

Durante o desenvolvimento dos testes é comum precisar pausar a execução para inspecionar elementos, validar seletores e acompanhar cada ação.

O **Playwright Inspector** é a ferramenta oficial para depuração de testes.

Com ele é possível:

- 🔍 Inspecionar elementos da página
- 🎯 Criar seletores automaticamente
- ▶ Continuar a execução
- ⏭ Executar passo a passo
- ⏸ Pausar a execução
- 🧪 Testar Locators
- 📋 Copiar seletores

---

## Utilizando page.pause()

Basta adicionar:

```python
page.pause()
```

Exemplo:

```python
from playwright.sync_api import Page

def test_exemplo(page: Page):

    page.goto(
        "https://playwright.dev"
    )

    page.pause()

    page.get_by_role(
        "link",
        name="Docs"
    ).click()
```

Ao chegar no `page.pause()`, o navegador será pausado e o Inspector será aberto.

---

# Utilizando PWDEBUG

Outra forma é executar utilizando:

### Windows PowerShell

```powershell
$env:PWDEBUG=1
uv run pytest
```

Executando apenas um arquivo:

```powershell
$env:PWDEBUG=1
uv run pytest tests/Command/hover.py
```

Abrindo o navegador:

```powershell
$env:PWDEBUG=1
uv run pytest tests/Command/hover.py --headed
```

---

### Linux / macOS

```bash
PWDEBUG=1 uv run pytest
```

---

# Quando utilizar o Inspector?

Sempre que:

- um Locator não funcionar
- um botão não for encontrado
- precisar criar um XPath
- quiser validar um CSS Selector
- quiser acompanhar a execução

---

# 🎯 9. Locators

Os **Locators** são responsáveis por localizar elementos da página.

O Playwright recomenda utilizar primeiro:

1. get_by_role()
2. get_by_label()
3. get_by_placeholder()
4. get_by_text()
5. locator()

---

# get_by_role()

É o Locator recomendado pela Microsoft.

Exemplo:

```python
page.get_by_role(
    "button",
    name="Entrar"
).click()
```

Campo de texto:

```python
page.get_by_role(
    "textbox"
).fill(
    "Playwright"
)
```

Link:

```python
page.get_by_role(
    "link",
    name="Documentação"
).click()
```

Checkbox:

```python
page.get_by_role(
    "checkbox"
).check()
```

Radio:

```python
page.get_by_role(
    "radio"
).check()
```

Combobox:

```python
page.get_by_role(
    "combobox"
).select_option("Brasil")
```

---

# get_by_label()

Muito utilizado em formulários.

HTML:

```html
<label>Email</label>
<input>
```

Playwright:

```python
page.get_by_label(
    "Email"
).fill(
    "teste@email.com"
)
```

---

# get_by_placeholder()

HTML:

```html
<input placeholder="Digite seu email">
```

Playwright:

```python
page.get_by_placeholder(
    "Digite seu email"
).fill(
    "teste@email.com"
)
```

---

# get_by_text()

Localiza elementos pelo texto.

```python
page.get_by_text(
    "Entrar"
).click()
```

Outro exemplo:

```python
page.get_by_text(
    "Cadastrar"
).click()
```

---

# get_by_alt_text()

Utilizado em imagens.

```python
page.get_by_alt_text(
    "Logo"
).click()
```

---

# get_by_title()

Localiza pelo atributo title.

```python
page.get_by_title(
    "Pesquisar"
).click()
```

---

# get_by_test_id()

Muito utilizado em aplicações React.

HTML:

```html
<button data-testid="btn-login">
```

Playwright:

```python
page.get_by_test_id(
    "btn-login"
).click()
```

---

# locator()

Permite utilizar CSS Selector ou XPath.

CSS:

```python
page.locator(
    "#email"
).fill(
    "teste"
)
```

Classe:

```python
page.locator(
    ".botao"
).click()
```

Atributo:

```python
page.locator(
    "[name='email']"
).fill(
    "teste"
)
```

---

# XPath

Também pode ser utilizado.

```python
page.locator(
    "//button"
).click()
```

Outro exemplo:

```python
page.locator(
    "//input[@id='email']"
).fill(
    "teste@email.com"
)
```

Apesar de suportado, prefira `get_by_role()` ou CSS quando possível.

---

# CSS Selector

Exemplos:

```python
page.locator(
    "#login"
)
```

```python
page.locator(
    ".btn-primary"
)
```

```python
page.locator(
    "input[name='email']"
)
```

---

# 🎮 10. Principais Comandos Playwright

Abrir página:

```python
page.goto(
    "https://google.com"
)
```

Clique:

```python
page.click(
    "#login"
)
```

Double Click:

```python
page.dblclick(
    "#login"
)
```

Hover:

```python
page.hover(
    "#menu"
)
```

Fill:

```python
page.fill(
    "#email",
    "teste@email.com"
)
```

Type:

```python
page.type(
    "#email",
    "Playwright"
)
```

Press:

```python
page.press(
    "#email",
    "Enter"
)
```

Check:

```python
page.check(
    "#aceito"
)
```

Uncheck:

```python
page.uncheck(
    "#aceito"
)
```

Selecionar opção:

```python
page.select_option(
    "#estado",
    "PB"
)
```

Upload:

```python
page.set_input_files(
    "#arquivo",
    "curriculo.pdf"
)
```

Screenshot:

```python
page.screenshot(
    path="prints/home.png"
)
```

Reload:

```python
page.reload()
```

Voltar:

```python
page.go_back()
```

Avançar:

```python
page.go_forward()
```

---

# ⏳ 11. Auto Wait

Uma das maiores vantagens do Playwright é a espera automática.

Antes de executar uma ação ele verifica:

- elemento existe
- elemento está visível
- elemento está habilitado
- elemento está estável
- elemento pode receber clique

Exemplo:

```python
page.get_by_role(
    "button",
    name="Entrar"
).click()
```

O Playwright aguardará automaticamente o botão ficar pronto.

---

# Evite

```python
page.wait_for_timeout(5000)
```

Problemas:

- testes lentos
- tempo fixo
- aumenta a chance de falhas

---

# Prefira

```python
from playwright.sync_api import expect

expect(
    page.get_by_role(
        "button",
        name="Entrar"
    )
).to_be_visible()
```

---

# ✔ 12. Assertions

As Assertions validam se o comportamento da aplicação está correto.

Importe:

```python
from playwright.sync_api import expect
```

Título:

```python
expect(page).to_have_title(
    "Google"
)
```

URL:

```python
expect(page).to_have_url(
    "https://google.com"
)
```

Elemento visível:

```python
expect(
    page.get_by_text("Sucesso")
).to_be_visible()
```

Elemento oculto:

```python
expect(
    page.get_by_text("Erro")
).to_be_hidden()
```

Texto:

```python
expect(
    page.get_by_role(
        "heading"
    )
).to_have_text(
    "Bem-vindo"
)
```

Contém texto:

```python
expect(
    page.locator("#mensagem")
).to_contain_text(
    "Sucesso"
)
```

Campo preenchido:

```python
expect(
    page.locator("#email")
).to_have_value(
    "teste@email.com"
)
```

Checkbox marcado:

```python
expect(
    page.get_by_role("checkbox")
).to_be_checked()
```

Elemento habilitado:

```python
expect(
    page.get_by_role(
        "button",
        name="Salvar"
    )
).to_be_enabled()
```

Elemento desabilitado:

```python
expect(
    page.get_by_role(
        "button",
        name="Salvar"
    )
).to_be_disabled()
```

---

# 💡 Boas práticas para Locators

✅ Prefira `get_by_role()`

✅ Utilize `get_by_label()` em formulários

✅ Utilize `get_by_test_id()` quando disponível

✅ Evite XPath muito longo

✅ Evite seletores frágeis

✅ Utilize nomes claros e descritivos

---

➡️ **Continua na PARTE 4**, onde veremos:

- Fixtures do Pytest
- Browser, Context e Page
- Page Object Model (POM)
- Organização profissional do projeto
- Screenshots
- Vídeos
- Trace Viewer
- Relatórios HTML
- Evidências de teste
  # 🧩 13. Fixtures do Pytest

As **Fixtures** são um dos recursos mais importantes do Pytest.

Elas permitem reutilizar código entre vários testes, evitando duplicação e facilitando a manutenção.

---

## O que é uma Fixture?

Uma Fixture é uma função executada antes (e/ou depois) de um teste para preparar o ambiente necessário.

No Playwright, o plugin `pytest-playwright` já fornece várias fixtures prontas.

As principais são:

- `page`
- `browser`
- `context`
- `browser_name`
- `playwright`

---

## Fixture page

É a fixture mais utilizada.

Ela fornece uma página do navegador pronta para uso.

```python
from playwright.sync_api import Page

def test_google(page: Page):

    page.goto(
        "https://google.com"
    )
```

---

## Fixture browser

Fornece acesso ao navegador.

```python
def test_browser(browser):

    print(browser)
```

---

## Fixture context

O **Browser Context** representa uma sessão isolada do navegador.

Cada contexto possui:

- Cookies
- Cache
- Sessão
- Local Storage

Exemplo:

```python
def test_context(context):

    page = context.new_page()

    page.goto(
        "https://google.com"
    )
```

---

## Fixture browser_name

Permite descobrir qual navegador está executando.

```python
def test_browser(browser_name):

    print(browser_name)
```

Resultado:

```text
chromium
```

ou

```text
firefox
```

ou

```text
webkit
```

---

# 🌐 Browser → Context → Page

A arquitetura do Playwright funciona desta forma:

```text
Playwright
     │
 Browser
     │
 Browser Context
     │
    Page
```

Cada **Browser Context** funciona como um navegador independente.

Isso permite executar testes isolados.

---

# 📁 Organização do Projeto

Uma estrutura organizada facilita a manutenção e evolução do projeto.

```text
Automacao-de-Testes-com-Playwright-Python-e-Pytest
│
├── .venv/
│
├── pages/
│   ├── login_page.py
│   ├── home_page.py
│   ├── products_page.py
│   └── cart_page.py
│
├── tests/
│   ├── Command/
│   ├── Expect/
│   ├── Locator/
│   ├── test_login.py
│   ├── test_home.py
│   └── test_cart.py
│
├── screenshots/
│
├── videos/
│
├── traces/
│
├── reports/
│
├── conftest.py
│
├── pyproject.toml
│
├── .gitignore
│
└── README.md
```

---

# 🏗️ 14. Page Object Model (POM)

O **Page Object Model** é um padrão de projeto utilizado para separar a lógica da página dos testes.

Benefícios:

- Código organizado
- Fácil manutenção
- Reutilização
- Menor duplicação
- Melhor legibilidade

---

## Sem POM

```python
def test_login(page):

    page.goto("https://site.com")

    page.fill("#email","admin@email.com")

    page.fill("#senha","123456")

    page.click("#login")
```

Embora funcione, toda a lógica fica dentro do teste.

---

## Com POM

### login_page.py

```python
class LoginPage:

    def __init__(self, page):
        self.page = page

    def acessar(self):
        self.page.goto("https://site.com")

    def preencher_email(self, email):
        self.page.get_by_label("Email").fill(email)

    def preencher_senha(self, senha):
        self.page.get_by_label("Senha").fill(senha)

    def clicar_login(self):
        self.page.get_by_role(
            "button",
            name="Entrar"
        ).click()
```

---

### test_login.py

```python
from pages.login_page import LoginPage

def test_login(page):

    login = LoginPage(page)

    login.acessar()

    login.preencher_email(
        "admin@email.com"
    )

    login.preencher_senha(
        "123456"
    )

    login.clicar_login()
```

Agora o teste fica mais limpo e a lógica permanece centralizada na página.

---

# 📸 15. Screenshots

O Playwright permite capturar imagens durante a execução.

Capturar a tela inteira:

```python
page.screenshot(
    path="screenshots/home.png"
)
```

Capturar apenas um elemento:

```python
page.get_by_role(
    "button",
    name="Entrar"
).screenshot(
    path="screenshots/botao.png"
)
```

---

# 🎥 16. Gravação de Vídeos

O Playwright pode gravar vídeos automaticamente.

Exemplo de configuração:

```python
browser.new_context(
    record_video_dir="videos/"
)
```

Após a execução:

```text
videos/
```

conterá os arquivos gravados.

---

# 📂 Organização das Evidências

```text
Projeto
│
├── screenshots/
│
├── videos/
│
├── traces/
│
└── reports/
```

---

# 🔍 17. Trace Viewer

O Trace Viewer registra toda a execução do teste.

Inclui:

- cliques
- teclas pressionadas
- screenshots
- DOM
- requisições
- respostas
- console

---

## Gerar Trace

```bash
uv run pytest --tracing on
```

---

## Abrir Trace

```bash
uv run playwright show-trace trace.zip
```

Será aberta uma interface gráfica permitindo analisar toda a execução.

---

# 📊 18. Relatórios HTML

Instalar:

```bash
uv pip install pytest-html
```

Gerar relatório:

```bash
uv run pytest --html=reports/report.html
```

Será criada a pasta:

```text
reports/
```

Com o arquivo:

```text
report.html
```

Esse relatório apresenta:

- quantidade de testes
- tempo de execução
- falhas
- sucessos
- detalhes de erros

---

# 📷 Evidências de Teste

Em projetos reais é comum armazenar:

- Screenshots
- Vídeos
- Trace Viewer
- Logs
- Relatórios HTML

Esses artefatos ajudam na análise de falhas e documentação da execução.

---

# ⚙️ Arquivo conftest.py

O arquivo `conftest.py` permite compartilhar configurações e fixtures entre todos os testes.

Exemplo:

```python
import pytest

@pytest.fixture
def usuario():

    return {
        "email": "admin@email.com",
        "senha": "123456"
    }
```

Utilizando a fixture:

```python
def test_login(page, usuario):

    page.goto("https://site.com")

    page.get_by_label(
        "Email"
    ).fill(
        usuario["email"]
    )

    page.get_by_label(
        "Senha"
    ).fill(
        usuario["senha"]
    )
```

---

# 📌 Dicas de Organização

Uma boa prática é manter:

```text
pages/
```

Somente Page Objects.

```text
tests/
```

Somente testes.

```text
screenshots/
```

Somente capturas de tela.

```text
reports/
```

Relatórios.

```text
videos/
```

Gravações.

```text
traces/
```

Arquivos do Trace Viewer.

Essa organização facilita a navegação no projeto e segue padrões utilizados em equipes de QA Automation.

---

# 💡 Boas práticas

✅ Utilize o POM para separar a lógica dos testes.

✅ Centralize seletores nas classes de página.

✅ Reutilize Fixtures sempre que possível.

✅ Organize evidências em pastas específicas.

✅ Gere relatórios ao final das execuções.

✅ Mantenha o projeto limpo e padronizado.

---

➡️ **Continua na PARTE 5**, onde veremos:

- Git e GitHub
- GitHub Actions (CI/CD)
- `.gitignore`
- Boas práticas de automação
- Convenções de nomenclatura
- Resolução de problemas comuns
- Dicas para projetos profissionais

  # 🌿 19. Git e GitHub

O Git é um sistema de controle de versão distribuído que permite acompanhar todas as alterações realizadas no projeto.

O GitHub é uma plataforma para hospedagem de repositórios Git, facilitando o trabalho em equipe, versionamento e integração contínua.

---

# Inicializando um repositório

Caso o projeto ainda não esteja versionado:

```bash
git init
```

---

# Verificando o status

```bash
git status
```

Exemplo:

```text
On branch main

No commits yet

Untracked files:
README.md
tests/
pages/
```

---

# Adicionando arquivos

Adicionar todos os arquivos:

```bash
git add .
```

Adicionar apenas um arquivo:

```bash
git add README.md
```

---

# Criando um Commit

```bash
git commit -m "Primeiro commit"
```

Boas mensagens de commit:

```text
feat: adiciona testes de login

fix: corrige locator do botão entrar

docs: atualiza README

refactor: melhora Page Object

test: adiciona testes de cadastro
```

---

# Conectando ao GitHub

Criando o repositório no GitHub:

```
New Repository
```

Depois execute:

```bash
git remote add origin https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git
```

---

# Enviando para o GitHub

Primeiro envio:

```bash
git push -u origin main
```

Próximos envios:

```bash
git push
```

---

# Atualizando o Projeto

Baixar alterações:

```bash
git pull
```

Enviar alterações:

```bash
git push
```

---

# Trabalhando com Branches

Criar:

```bash
git branch feature-login
```

Trocar:

```bash
git checkout feature-login
```

Ou:

```bash
git switch feature-login
```

Criar e trocar:

```bash
git checkout -b feature-login
```

---

# 📦 20. Arquivo .gitignore

O arquivo `.gitignore` impede que arquivos desnecessários sejam enviados para o GitHub.

Exemplo:

```gitignore
# Ambiente Virtual
.venv/

# Python
__pycache__/
*.pyc

# Pytest
.pytest_cache/

# PyCharm
.idea/

# VS Code
.vscode/

# Relatórios
reports/

# Screenshots
screenshots/

# Vídeos
videos/

# Trace Viewer
traces/

# Logs
*.log

# Sistema Operacional
.DS_Store
Thumbs.db
```

---

# 🚀 21. GitHub Actions (CI/CD)

O GitHub Actions permite executar os testes automaticamente sempre que ocorrer:

- Push
- Pull Request
- Merge

Fluxo:

```text
Desenvolvedor
      │
      ▼
Git Commit
      │
      ▼
Git Push
      │
      ▼
GitHub
      │
      ▼
GitHub Actions
      │
      ▼
Instala Dependências
      │
      ▼
Executa Playwright
      │
      ▼
Resultado
```

---

## Estrutura

```text
.github/
└── workflows/
    └── playwright.yml
```

---

## Exemplo de Workflow

```yaml
name: Playwright Tests

on:
  push:
    branches:
      - main

jobs:
  tests:

    runs-on: ubuntu-latest

    steps:

      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install uv
        run: pip install uv

      - name: Install Dependencies
        run: uv pip install pytest pytest-playwright playwright

      - name: Install Browsers
        run: uv run playwright install

      - name: Execute Tests
        run: uv run pytest
```

---

# 📊 22. Estrutura Recomendada para Projetos

```text
Projeto
│
├── .github/
│
├── pages/
│
├── tests/
│
├── screenshots/
│
├── videos/
│
├── traces/
│
├── reports/
│
├── conftest.py
│
├── pyproject.toml
│
├── .gitignore
│
├── README.md
│
└── requirements.txt
```

---

# 🧹 23. Boas Práticas

## Nome dos arquivos

Utilize:

```text
test_login.py

test_home.py

test_checkout.py
```

Evite:

```text
teste1.py

arquivo.py

novo.py
```

---

## Nome dos testes

Bom exemplo:

```python
def test_login_com_usuario_valido():
```

Outro exemplo:

```python
def test_adicionar_produto_ao_carrinho():
```

Evite:

```python
def teste():
```

---

## Organização

✔ Um teste para cada cenário.

✔ Não reutilize código copiando e colando.

✔ Utilize Page Objects.

✔ Utilize Fixtures.

✔ Organize por funcionalidade.

---

## Locators

Prefira:

```python
get_by_role()
```

Depois:

```python
get_by_label()
```

Depois:

```python
get_by_placeholder()
```

Depois:

```python
get_by_test_id()
```

Somente quando necessário:

```python
locator()

CSS

XPath
```

---

## Assertions

Sempre valide o resultado esperado.

Exemplo:

```python
expect(
    page.get_by_text(
        "Login realizado"
    )
).to_be_visible()
```

---

## Esperas

Nunca utilize:

```python
page.wait_for_timeout(5000)
```

Prefira:

```python
expect(locator).to_be_visible()
```

---

## Page Object

Centralize:

- URLs
- Locators
- Métodos

Nunca espalhe locators em vários testes.

---

## Dados de Teste

Evite escrever valores diretamente nos testes.

Prefira:

```python
usuario = {
    "email": "admin@email.com",
    "senha": "123456"
}
```

Ou fixtures.

---

# 🐞 24. Resolução de Problemas

## Locator não encontrado

Verifique:

- texto correto
- elemento visível
- iframe
- tempo de carregamento

---

## Timeout

Aumente:

```python
page.set_default_timeout(60000)
```

---

## Browser não abre

Execute novamente:

```bash
uv run playwright install
```

---

## Dependências não encontradas

Instale novamente:

```bash
uv pip install pytest pytest-playwright playwright
```

---

## Ambiente virtual

Ative:

Windows

```powershell
.venv\Scripts\Activate.ps1
```

Linux/macOS

```bash
source .venv/bin/activate
```

---

# 💡 Dicas para Projetos Profissionais

✔ Utilize POM.

✔ Mantenha código limpo.

✔ Utilize nomes claros.

✔ Faça commits frequentes.

✔ Atualize o README.

✔ Gere relatórios.

✔ Capture screenshots em falhas.

✔ Grave vídeos quando necessário.

✔ Utilize CI/CD.

✔ Revise os testes periodicamente.

---

# 📚 Recursos para Estudo

Documentação oficial do Playwright:

https://playwright.dev/python/

Documentação do Pytest:

https://docs.pytest.org/

Python:

https://www.python.org/

Git:

https://git-scm.com/

GitHub:

https://github.com/

PyCharm:

https://www.jetbrains.com/pycharm/

---

# ✅ Checklist do Projeto

- [x] Python instalado
- [x] Git instalado
- [x] uv instalado
- [x] Ambiente virtual criado
- [x] Dependências instaladas
- [x] Navegadores instalados
- [x] Primeiro teste criado
- [x] Testes executados
- [x] Uso do `--headed`
- [x] Uso do Playwright Inspector
- [x] Locators
- [x] Assertions
- [x] Auto Wait
- [x] Fixtures
- [x] Page Object Model
- [x] Screenshots
- [x] Relatórios HTML
- [x] GitHub Actions
- [x] GitHub

---

➡️ **Continua na PARTE 6 (última)**, que incluirá:

- FAQ (Perguntas Frequentes)
- Cheatsheet completo dos comandos Playwright + Pytest
- Atalhos úteis
- Roadmap de estudos
- Próximos passos
- Tecnologias utilizadas
- Referências
- Autor
- Considerações finais
  # 📌 Estrutura de Testes Automatizados

## Organização do Projeto

Uma boa organização dos arquivos facilita a manutenção, evolução e execução dos testes automatizados.

Exemplo de estrutura utilizada:

```
Projeto_Playwright/
│
├── tests/
│   ├── test_login.py
│   ├── test_busca.py
│   └── test_produto.py
│
├── pages/
│   ├── login_page.py
│   ├── home_page.py
│   └── produto_page.py
│
├── utils/
│   └── helpers.py
│
├── screenshots/
│
├── reports/
│
├── pytest.ini
│
├── requirements.txt
│
└── README.md
```

---

# 📂 Organização Page Object Model (POM)

O projeto utiliza o padrão **Page Object Model**, uma arquitetura muito utilizada em automação de testes.

O objetivo é separar:

* Código dos testes;
* Elementos das páginas;
* Ações realizadas no sistema.

## Benefícios do POM:

✅ Código mais organizado;

✅ Maior reutilização;

✅ Facilidade de manutenção;

✅ Menos duplicação;

✅ Testes mais profissionais.

---

# 🧩 Exemplo de Page Object

Arquivo:

```
pages/login_page.py
```

Exemplo:

```python
class LoginPage:

    def __init__(self, page):
        self.page = page

        self.usuario = page.locator("#username")
        self.senha = page.locator("#password")
        self.botao_login = page.locator("#login")


    def realizar_login(self, usuario, senha):

        self.usuario.fill(usuario)
        self.senha.fill(senha)
        self.botao_login.click()
```

---

# 🧪 Exemplo de Teste utilizando Page Object

Arquivo:

```
tests/test_login.py
```

Código:

```python
from pages.login_page import LoginPage


def test_login(page):

    login = LoginPage(page)

    page.goto("https://exemplo.com")

    login.realizar_login(
        "usuario_teste",
        "senha_teste"
    )

    assert page.title() != ""
```

---

# ⚙️ Configuração do Pytest

Arquivo:

```
pytest.ini
```

Exemplo:

```ini
[pytest]

addopts = -v

testpaths =
    tests
```

Esse arquivo permite configurar o comportamento do Pytest.

---

# 🚀 Execução dos Testes

Executar testes normalmente:

```bash
pytest
```

Executar mostrando o navegador:

```bash
pytest --headed
```

Executar utilizando Chromium:

```bash
pytest --browser chromium
```

Executar um arquivo específico:

```bash
pytest tests/test_login.py
```

---

# 📊 Relatórios de Testes

O Pytest permite gerar relatórios para análise dos resultados.

Exemplo:

```bash
pytest --html=reports/teste.html
```

O relatório apresenta:

* Testes executados;
* Testes aprovados;
* Testes falhados;
* Tempo de execução;
* Erros encontrados.

---

# 🐞 Evidências de Falha

Em automação profissional é importante capturar evidências.

Exemplos:

* Screenshot automático;
* Logs;
* Vídeos da execução;
* Relatórios HTML.

Essas informações ajudam na análise dos problemas encontrados.

---

# 🔄 Integração com Git e GitHub

O projeto utiliza Git para controle de versão.

Principais comandos:

Clonar projeto:

```bash
git clone URL_DO_REPOSITORIO
```

Verificar alterações:

```bash
git status
```

Adicionar arquivos:

```bash
git add .
```

Criar commit:

```bash
git commit -m "Implementação dos testes Playwright"
```

Enviar alterações:

```bash
git push
```

---

# 🎯 Objetivos Técnicos Desenvolvidos

Durante o desenvolvimento deste projeto foram praticados:

✔ Automação Web com Playwright;

✔ Criação de testes automatizados;

✔ Uso do Pytest;

✔ Organização com Page Object Model;

✔ Execução em diferentes navegadores;

✔ Controle de versão com Git;

✔ Boas práticas de Engenharia de Software;

✔ Estrutura profissional de projetos de testes.

---

# 📚 Conhecimentos Aplicados

Tecnologias utilizadas:

| Tecnologia | Utilização                  |
| ---------- | --------------------------- |
| Python     | Linguagem principal         |
| Playwright | Automação Web               |
| Pytest     | Framework de testes         |
| uv         | Gerenciamento de ambiente   |
| Git        | Controle de versão          |
| GitHub     | Hospedagem do código        |
| PyCharm    | Ambiente de desenvolvimento |

---

# ✅ Conclusão

Este projeto demonstra a criação de uma base profissional para automação de testes Web utilizando Python e Playwright.

A aplicação dos conceitos de organização, boas práticas e padrões de projeto permite criar testes:

* Mais confiáveis;
* Mais fáceis de manter;
* Escaláveis;
* Adequados para ambientes profissionais de QA.

O conhecimento adquirido serve como base para atuação em:

* QA Automation;
* Engenharia de Testes;
* Desenvolvimento de Software;
* Integração Contínua (CI/CD).
# 📌 Parte 8 — Relatórios Profissionais com pytest-html, Screenshots, Vídeos, Logs e Evidências de Falha no Playwright

Nesta etapa será apresentada a evolução do projeto de automação de testes para um modelo mais profissional de **QA Automation**, adicionando:

* 📊 Relatórios HTML com pytest-html;
* 📸 Captura automática de screenshots;
* 🎥 Gravação de vídeos das execuções;
* 📝 Logs para investigação de erros;
* 🔎 Evidências de falha;
* 📁 Organização dos artefatos de testes.

Esses recursos são utilizados em ambientes reais para facilitar a análise dos resultados dos testes.

---

# 🎯 Objetivo

Quando um teste falha, o analista de qualidade precisa responder:

* O que aconteceu?
* Onde ocorreu o erro?
* Qual tela estava aberta?
* Qual era o estado do navegador?
* Como reproduzir o problema?

Por isso, uma automação profissional gera evidências.

Fluxo:

```text
Execução do teste
        │
        ▼
Teste aprovado?
        │
 ┌──────┴──────┐
 │             │
SIM           NÃO
 │             │
 ▼             ▼
Resultado    Screenshot
OK           Vídeo
              Logs
              Relatório
```

---

# 📂 Estrutura do Projeto com Relatórios

Após adicionar evidências:

```text
Automacao-de-Testes-com-Playwright-Python-e-Pytest
│
├── tests
│   │
│   └── Command
│       └── hover.py
│
├── reports
│   │
│   ├── teste.html
│   ├── screenshots
│   │   └── erro_login.png
│   │
│   └── videos
│       └── teste.webm
│
├── logs
│   └── execution.log
│
├── conftest.py
│
├── pytest.ini
│
└── pyproject.toml
```

---

# 📊 1. Relatório HTML com pytest-html

O plugin **pytest-html** permite gerar relatórios visuais dos testes.

Instalação:

```powershell
uv add pytest-html
```

ou:

```powershell
pip install pytest-html
```

---

# ▶️ Executando com Relatório

Comando:

```powershell
uv run pytest --html=reports/teste.html
```

Resultado:

```text
reports
 └── teste.html
```

O relatório apresenta:

✅ Nome dos testes;

✅ Status;

✅ Tempo de execução;

✅ Erros encontrados;

✅ Detalhes da execução.

---

# 📸 2. Captura de Screenshot no Playwright

O Playwright permite capturar imagens da tela.

Exemplo:

Arquivo:

```text
tests/Command/hover.py
```

Código:

```python
from playwright.sync_api import Page


def test_google(page: Page):

    page.goto("https://www.google.com")

    page.screenshot(
        path="reports/screenshots/google.png"
    )

    assert "Erro" in page.title()
```

---

# Resultado:

Será criado:

```text
reports/screenshots/google.png
```

Exemplo de evidência:

```text
Teste falhou
      │
      ▼
Screenshot criado
      │
      ▼
Analista verifica a tela
```

---

# 📸 Screenshot Automático em Falhas

Para evitar colocar screenshot manual em todos os testes, podemos utilizar o arquivo:

```text
conftest.py
```

Código:

```python
import pytest


@pytest.fixture
def page(page):

    yield page

    if page.is_closed():
        return

```

---

# 🎥 3. Gravação de Vídeo com Playwright

O vídeo permite assistir exatamente o que ocorreu durante o teste.

Configuração:

Arquivo:

```text
conftest.py
```

Exemplo:

```python
import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def context(browser):

    context = browser.new_context(
        record_video_dir="reports/videos"
    )

    yield context

    context.close()
```

---

# Resultado:

Após execução:

```text
reports/videos

└── teste.webm
```

O vídeo mostra:

* Abertura do navegador;
* Cliques;
* Digitação;
* Navegação;
* Erros.

---

# 📝 4. Configuração de Logs

Logs ajudam a registrar informações da execução.

Criar:

```text
logs/execution.log
```

---

Configuração:

```python
import logging


logging.basicConfig(
    filename="logs/execution.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


logging.info("Teste iniciado")
```

---

Exemplo do arquivo:

```text
2026-08-06 10:30:00 INFO Teste iniciado

2026-08-06 10:30:05 INFO Página aberta

2026-08-06 10:30:10 ERROR Elemento não encontrado
```

---

# 🔎 5. Evidências Profissionais de Falha

Em uma empresa, quando ocorre um erro, normalmente são anexados:

## Screenshot

```text
erro.png
```

Mostra:

* Tela do sistema;
* Mensagem de erro;
* Estado da aplicação.

---

## Vídeo

```text
teste.webm
```

Mostra:

* Sequência de ações;
* Momento exato da falha.

---

## Log

```text
execution.log
```

Mostra:

* Horários;
* Passos executados;
* Erros técnicos.

---

## Relatório HTML

```text
teste.html
```

Mostra:

* Resultado geral;
* Testes aprovados;
* Testes reprovados.

---

# ⚙️ Configuração Profissional com pytest.ini

Arquivo:

```text
pytest.ini
```

Exemplo:

```ini
[pytest]

addopts =
    -v
    --html=reports/teste.html

testpaths =
    tests
```

Agora basta executar:

```powershell
uv run pytest
```

O relatório será gerado automaticamente.

---

# 🚀 Integração com GitHub Actions

O relatório pode ser armazenado como artefato.

Adicionar no:

```text
.github/workflows/playwright.yml
```

Após executar os testes:

```yaml
- name: Salvar relatório
  uses: actions/upload-artifact@v4

  with:
    name: playwright-report
    path: reports/
```

---

# Fluxo Completo Profissional

```text
Desenvolvedor envia código
          │
          ▼
GitHub Actions inicia
          │
          ▼
Executa Playwright
          │
          ▼
Teste passou?
          │
    ┌─────┴─────┐
    │           │
   SIM         NÃO
    │           │
    ▼           ▼
 Relatório   Screenshot
 OK          Vídeo
             Logs
             Relatório
```

---

# 🏆 Resultado Final do Projeto

Após esta etapa, a automação possui:

✅ Testes automatizados;

✅ Organização Page Object Model;

✅ Execução com Pytest;

✅ Navegadores Playwright;

✅ Pipeline CI/CD;

✅ Relatórios HTML;

✅ Evidências de falha;

✅ Logs;

✅ Vídeos;

✅ Estrutura profissional de QA.

---

# 📚 Conceito aplicado no mercado

Essa estrutura aproxima o projeto de um ambiente real de:

* QA Automation Engineer;
* Analista de Testes;
* SDET (Software Development Engineer in Test);
* Times que utilizam DevOps e CI/CD.

O projeto agora possui características de uma automação escalável e preparada para integração contínua.
PARTE 10 — FRAMEWORK PROFISSIONAL PLAYWRIGHT

Fixtures Avançadas, Configuração por Ambiente, Variáveis .env,
Dados Externos e Arquitetura Corporativa


Nesta etapa vamos transformar o projeto Playwright em um framework de automação profissional, semelhante ao utilizado em equipes de QA.

Objetivos:

✅ Escalar centenas de testes
✅ Separar ambientes DEV/HML/PROD
✅ Reutilizar código
✅ Controlar dados de teste
✅ Facilitar manutenção
✅ Preparar para CI/CD


==================================================
1. EVOLUÇÃO DO PROJETO
==================================================


Antes:

teste_login.py
teste_cadastro.py


Problemas:

❌ Código duplicado
❌ Difícil manutenção
❌ Configuração espalhada


Agora:


Automacao-Playwright

│
├── tests
│   ├── test_login.py
│   └── test_usuario.py
│
├── pages
│   ├── login_page.py
│   └── usuario_page.py
│
├── fixtures
│   └── browser.py
│
├── config
│   └── settings.py
│
├── data
│   └── usuarios.json
│
├── utils
│   └── helpers.py
│
├── reports
│
├── screenshots
│
├── logs
│
├── .env
├── pytest.ini
└── conftest.py



==================================================
2. O PAPEL DO conftest.py
==================================================


O arquivo:


conftest.py


é o coração do Pytest.


Ele controla:


- Navegador
- Sessões
- Dados compartilhados
- Configurações
- Hooks



Exemplo:


import pytest


@pytest.fixture
def usuario():

    return {

        "email":
        "teste@email.com",

        "senha":
        "123456"

    }



Uso:


def test_login(usuario):

    print(
    usuario["email"]
    )



==================================================
3. FIXTURES AVANÇADAS PLAYWRIGHT
==================================================


Exemplo:


import pytest


@pytest.fixture
def abrir_site(page):

    page.goto(
    "https://www.google.com"
    )

    return page



Teste:


def test_google(abrir_site):

    assert (
    abrir_site.title()
    ==
    "Google"
    )



==================================================
4. ESCOPO DAS FIXTURES
==================================================


Function:


@pytest.fixture(
scope="function"
)


Executa em cada teste.


Exemplo:


Teste 1
abre navegador


Teste 2
abre navegador



--------------------------


Session:


@pytest.fixture(
scope="session"
)



Executa uma única vez.


Fluxo:


Inicio execução

↓

Abre ambiente

↓

Executa todos testes

↓

Finaliza



Outros escopos:


class

module

package



==================================================
5. CONFIGURAÇÃO CENTRALIZADA
==================================================


Criar:


config/settings.py



Código:


import os


BASE_URL = os.getenv(
    "BASE_URL"
)


BROWSER = os.getenv(
    "BROWSER",
    "chromium"
)



Uso:


from config.settings import BASE_URL


page.goto(BASE_URL)



==================================================
6. VARIÁVEIS DE AMBIENTE .env
==================================================


Não colocar:


senha="123456"



Problemas:


❌ Segurança

❌ Exposição no GitHub

❌ Dificuldade para trocar ambiente



Criar:


.env



Exemplo:


BASE_URL=https://homologacao.site.com

USER_TESTE=admin

PASSWORD_TESTE=123456



==================================================
7. INSTALAR python-dotenv
==================================================


Com uv:


uv add python-dotenv



Carregar:


from dotenv import load_dotenv

import os


load_dotenv()


usuario = os.getenv(
"USER_TESTE"
)


senha = os.getenv(
"PASSWORD_TESTE"
)



==================================================
8. AMBIENTES DEV, HML E PROD
==================================================


Estrutura:


config

├── dev.env

├── hml.env

└── prod.env



dev.env


BASE_URL=https://dev.site.com



hml.env


BASE_URL=https://hml.site.com



prod.env


BASE_URL=https://site.com



==================================================
9. ESCOLHER AMBIENTE NA EXECUÇÃO
==================================================


Executar:


pytest --env=hml



Resultado:


Carrega:

hml.env


BASE_URL=https://hml.site.com



==================================================
10. OPÇÃO PERSONALIZADA PYTEST
==================================================


conftest.py



Código:


def pytest_addoption(parser):

    parser.addoption(
        "--env",
        action="store",
        default="dev"
    )



@pytest.fixture
def ambiente(request):

    return request.config.getoption(
        "--env"
    )



Executar:


pytest --env=prod



==================================================
11. MASSA DE TESTES EXTERNA
==================================================


Evitar:


usuario="admin"

senha="123"



Criar:


data/usuarios.json



Conteúdo:


{

"admin":{

"email":
"admin@email.com",

"senha":
"123456"

}

}



Ler arquivo:


import json


with open(
"data/usuarios.json"
) as arquivo:

    dados=json.load(
    arquivo
    )



==================================================
12. TESTE PARAMETRIZADO
==================================================


Exemplo:


@pytest.mark.parametrize(

"usuario",

[

"admin",

"cliente"

]

)


def test_login(usuario):

    print(usuario)



Resultado:


test_login[admin]

test_login[cliente]



==================================================
13. CAMADA DE SERVICES
==================================================


Estrutura:


services

├── api_login.py

└── usuario_service.py



Exemplo:


class UsuarioService:


    def criar_usuario(
        self,
        nome
    ):

        return {

        "nome":nome

        }



Teste:


def test_usuario():

    service=UsuarioService()


    usuario=
    service.criar_usuario(
    "Natanael"
    )


    assert usuario["nome"]=="Natanael"



==================================================
14. LOGS PROFISSIONAIS
==================================================


Instalar:


uv add loguru



Criar:


utils/logger.py



Código:


from loguru import logger


logger.add(
"logs/testes.log"
)



Uso:


from utils.logger import logger


logger.info(
"Executando login"
)



==================================================
15. CONFIGURAÇÃO pytest.ini
==================================================


Arquivo:


pytest.ini



Conteúdo:


[pytest]


testpaths =
    tests


addopts =
    -v
    --html=reports/report.html


markers =

    smoke: testes principais

    regression: testes completos



==================================================
16. TESTES POR CATEGORIA
==================================================


Exemplo:


@pytest.mark.smoke


def test_login():

    pass



Executar:


pytest -m smoke



==================================================
17. FIXTURE DE AUTENTICAÇÃO
==================================================


Cenário:

Todos testes precisam estar logados.



Exemplo:


@pytest.fixture

def usuario_logado(page):


    page.goto(
    "/login"
    )


    page.fill(
    "#email",
    "admin"
    )


    page.fill(
    "#senha",
    "123"
    )


    page.click(
    "#entrar"
    )


    return page



Teste:


def test_dashboard(usuario_logado):


    assert (

    "Dashboard"

    in usuario_logado.title()

    )



==================================================
18. ARQUITETURA FINAL PROFISSIONAL
==================================================


Framework Playwright


        |

        ↓


Tests

(Testes)


        |

        ↓


Pages

(Page Objects)


        |

        ↓


Services

(API)


        |

        ↓


Fixtures

(Configuração)


        |

        ↓


Utils

(Ferramentas)


        |

        ↓


Reports

(Resultados)



==================================================
19. FLUXO DE EXECUÇÃO PROFISSIONAL
==================================================


Comando:


pytest --env=hml



↓

Carrega ambiente


↓

Inicializa Browser


↓

Executa Fixtures


↓

Executa Testes


↓

Captura evidências


↓

Gera relatório


↓

Publica resultado CI/CD



==================================================
20. RESULTADO DA PARTE 10
==================================================


Você aprendeu:


✅ Arquitetura profissional Playwright

✅ Fixtures avançadas

✅ conftest.py profissional

✅ Configuração por ambiente

✅ Variáveis .env

✅ Massa de testes externa

✅ Parametrização

✅ Logs

✅ Organização corporativa

✅ Estrutura pronta para empresas



PRÓXIMA ETAPA:


PARTE 11 — TESTES DE API AVANÇADOS COM PLAYWRIGHT


Conteúdo:


- REST API na prática
- GET
- POST
- PUT
- DELETE
- Headers
- Token JWT
- OAuth
- Autenticação
- Mock de APIs
- Testes de contrato
- Integração API + Banco + Interface
- Cenários reais de QA

PARTE 11 — TESTES DE API AVANÇADOS COM PLAYWRIGHT

REST API, GET, POST, PUT, DELETE, Headers, Tokens JWT,
OAuth, Mock de APIs e Integração API + Interface


Nesta etapa vamos evoluir o framework para testar APIs profissionalmente.

Em ambientes reais de QA, não testamos apenas telas.

Um sistema normalmente possui:


Usuário

   |

   ↓

Frontend (Web/Mobile)

   |

   ↓

API REST

   |

   ↓

Banco de Dados



O Playwright permite validar:


✅ Interface Web

✅ Serviços REST

✅ Autenticação

✅ Dados retornados pelo backend

✅ Integração Frontend + API



==================================================
1. O QUE É API TESTING?
==================================================


API Testing é validar diretamente os serviços responsáveis pela comunicação entre sistemas.


Exemplo:


Tela Login

↓

POST /login

↓

API valida usuário

↓

Retorna Token

↓

Usuário entra no sistema



==================================================
2. POR QUE TESTAR API?
==================================================


Vantagens:


✅ Mais rápido que teste UI

✅ Encontrar erros antes da tela

✅ Validar regras de negócio

✅ Maior cobertura

✅ Menor fragilidade



Comparação:


Teste UI:


Abrir navegador

Digitar usuário

Clicar botão

Esperar página

Validar resultado



Teste API:


Enviar requisição

Validar resposta



==================================================
3. APIRequestContext DO PLAYWRIGHT
==================================================


O Playwright possui cliente HTTP próprio:


APIRequestContext



Permite:


- GET

- POST

- PUT

- PATCH

- DELETE



==================================================
4. CONFIGURANDO API NO PROJETO
==================================================


Estrutura:


Automacao-Playwright


│

├── api

│   ├── api_client.py

│   └── usuario_api.py


├── tests

│   └── test_api.py


├── pages


└── conftest.py



==================================================
5. CRIANDO CLIENTE API
==================================================


Arquivo:


api/api_client.py



Código:


from playwright.sync_api import APIRequestContext



class APIClient:


    def __init__(
        self,
        request
    ):

        self.request = request



    def get(
        self,
        endpoint
    ):

        return self.request.get(
            endpoint
        )



    def post(
        self,
        endpoint,
        data
    ):

        return self.request.post(
            endpoint,
            data=data
        )



==================================================
6. CRIANDO FIXTURE API
==================================================


Arquivo:


conftest.py



Código:


import pytest

from playwright.sync_api import Playwright



@pytest.fixture

def api_context(
    playwright: Playwright
):


    request = (

        playwright.request

        .new_context(

            base_url=
            "https://api.exemplo.com"

        )

    )


    return request



==================================================
7. TESTE GET API
==================================================


Exemplo:


GET /usuarios



Teste:


def test_listar_usuario(
    api_context
):


    response = (

        api_context

        .get(

        "/usuarios"

        )

    )


    assert response.ok



    dados = response.json()



    assert len(dados) > 0



==================================================
8. VALIDANDO STATUS CODE
==================================================


Exemplo:


assert response.status == 200



Principais códigos:


200

Sucesso



201

Criado



400

Erro requisição



401

Não autorizado



403

Sem permissão



404

Não encontrado



500

Erro servidor



==================================================
9. TESTE POST API
==================================================


Criando usuário:


POST /usuarios



Código:


def test_criar_usuario(
    api_context
):


    response = (

        api_context

        .post(

        "/usuarios",

        data={


        "nome":

        "Natanael",


        "email":

        "teste@email.com"


        }

        )

    )


    assert response.status == 201



==================================================
10. TESTE PUT API
==================================================


Atualizar usuário:


PUT /usuarios/1



Código:


response = (


api_context


.put(


"/usuarios/1",


data={


"nome":

"Novo Nome"


}


)


)



assert response.ok



==================================================
11. TESTE DELETE API
==================================================


Excluir:


DELETE /usuarios/1



Código:


response = (


api_context


.delete(


"/usuarios/1"


)


)



assert response.status == 204



==================================================
12. TRABALHANDO COM HEADERS
==================================================


Muitas APIs precisam:


Authorization

Content-Type



Exemplo:


request = (


playwright.request


.new_context(


extra_http_headers={


"Content-Type":

"application/json"


}


)


)



==================================================
13. AUTENTICAÇÃO COM TOKEN JWT
==================================================


Fluxo:


Usuário


↓

POST /login


↓

API retorna:


{

token:

"abc123"

}


↓

Enviar token nas próximas chamadas



==================================================
14. LOGIN VIA API
==================================================


Exemplo:


response = (


api_context


.post(


"/login",


data={


"email":

"admin@email.com",


"senha":

"123456"


}


)


)



token = response.json()["token"]



==================================================
15. USANDO TOKEN JWT
==================================================


Criar novo contexto:


api = (


playwright.request


.new_context(


extra_http_headers={


"Authorization":


f"Bearer {token}"


}


)


)



Agora:


api.get(
"/usuarios"
)



já está autenticado.



==================================================
16. OAUTH 2.0
==================================================


Fluxo:


Aplicação


↓

Servidor OAuth


↓

Access Token


↓

API protegida



Exemplo:


headers={


"Authorization":


"Bearer TOKEN"


}



==================================================
17. CRIANDO CAMADA API OBJECT
==================================================


Assim como POM:


Interface:


pages



API:


api



Estrutura:


api


└── usuario_api.py



Código:


class UsuarioAPI:


    def __init__(

        self,

        client

    ):

        self.client = client



    def criar(

        self,

        usuario

    ):


        return (

        self.client.post(

        "/usuarios",

        usuario

        )

        )



==================================================
18. MOCK DE APIS
==================================================


Mock significa simular uma API.



Usado quando:


- Backend não está pronto

- Testar erros

- Simular respostas



Exemplo:


page.route(


"**/usuarios",


lambda route:


route.fulfill(


status=200,


body='{"nome":"Teste"}'


)


)



==================================================
19. INTERCEPTAÇÃO DE CHAMADAS
==================================================


Fluxo:


Browser


↓

Intercepta requisição


↓

Altera resposta


↓

Continua teste



==================================================
20. TESTE API + INTERFACE
==================================================


Cenário real:


Criar usuário pela API:


POST /usuarios



Depois validar na tela:


GET /usuarios


↓

Página mostra usuário



Código:


def test_usuario_completo(

api_context,

page

):


    api_context.post(


    "/usuarios",


    data={


    "nome":

    "Teste"


    }


    )



    page.goto(

    "/usuarios"

    )



    expect(


    page.get_by_text(

    "Teste"

    )


    ).to_be_visible()



==================================================
21. TESTES DE CONTRATO
==================================================


Validar formato:



Resposta:


{


"id":1,


"nome":"João",


"email":"teste@email.com"


}



Teste:


dados=response.json()



assert "id" in dados


assert "email" in dados



==================================================
22. VALIDAÇÃO DE SCHEMA JSON
==================================================


Instalar:


uv add jsonschema



Exemplo:


schema={


"type":

"object",


"properties":{


"id":{


"type":

"integer"


}


}


}



==================================================
23. TESTES NEGATIVOS
==================================================


Testar erros:



Enviar senha errada:


response = api.post(


"/login",


data={


"senha":

"errada"


}


)



assert response.status == 401



==================================================
24. ORGANIZAÇÃO FINAL API
==================================================


Automacao-Playwright


│

├── api

│

│── api_client.py

│

│── usuario_api.py


├── pages


├── tests


├── fixtures


├── data


├── reports


└── logs



==================================================
25. FLUXO PROFISSIONAL DE API TESTING
==================================================


Teste iniciado


↓

Criar contexto API


↓

Enviar Request


↓

Receber Response


↓

Validar Status


↓

Validar Dados


↓

Gerar Evidência


↓

Relatório



==================================================
RESULTADO DA PARTE 11
==================================================


Você aprendeu:


✅ API Testing com Playwright

✅ APIRequestContext

✅ GET / POST / PUT / DELETE

✅ Headers HTTP

✅ Token JWT

✅ OAuth 2.0

✅ Mock de APIs

✅ Interceptação de chamadas

✅ Testes de contrato

✅ Validação JSON

✅ API + Interface

✅ Arquitetura profissional de APIs



==================================================
PRÓXIMA ETAPA
==================================================


PARTE 12 — TESTES AVANÇADOS DE INTERFACE PLAYWRIGHT


Conteúdo:


- Upload de arquivos

- Download

- Iframes

- Abas múltiplas

- Popups

- Alerts

- Drag and Drop

- Mouse avançado

- Teclado

- Eventos

- Manipulação de páginas múltiplas

- Cenários reais de aplicações web
  PARTE 12 — TESTES AVANÇADOS DE INTERFACE COM PLAYWRIGHT

Upload, Download, Iframes, Abas Múltiplas, Popups,
Alerts, Drag and Drop, Mouse, Teclado e Eventos


Nesta etapa vamos aprofundar os testes de interface Web (UI Testing) usando recursos avançados do Playwright.

Em aplicações reais encontramos:

✅ Upload de documentos
✅ Download de relatórios
✅ Sistemas com iframe
✅ Várias abas abertas
✅ Popups de navegador
✅ Alertas JavaScript
✅ Componentes dinâmicos
✅ Interações com mouse e teclado



==================================================
1. ESTRUTURA DOS TESTES AVANÇADOS
==================================================


Automacao-Playwright


│

├── tests

│

│── test_upload.py

│── test_download.py

│── test_iframe.py

│── test_popup.py


├── pages


├── utils


└── conftest.py



==================================================
2. UPLOAD DE ARQUIVOS
==================================================


Cenário real:


Usuário precisa enviar:


- Foto

- PDF

- Documento

- XML



Exemplo HTML:


<input type="file">



Usando Playwright:


page.set_input_files(

"input[type=file]",

"arquivos/documento.pdf"

)



==================================================
3. UPLOAD COM LOCATOR
==================================================


Exemplo:


arquivo = (

page.locator(

"input[type=file]"

)

)



arquivo.set_input_files(

"teste.pdf"

)



==================================================
4. UPLOAD MÚLTIPLOS ARQUIVOS
==================================================


page.set_input_files(


"input[type=file]",


[


"foto.png",


"documento.pdf"


]


)



==================================================
5. VALIDANDO UPLOAD
==================================================


Depois do envio:


expect(


page.get_by_text(

"Arquivo enviado"

)


).to_be_visible()



==================================================
6. DOWNLOAD DE ARQUIVOS
==================================================


Cenário:


Usuário clica:


Gerar relatório


↓

Download PDF



Capturar download:


with page.expect_download() as download_info:


    page.click(

    "text=Download"

    )


download = download_info.value



Salvar arquivo:


download.save_as(


"downloads/relatorio.pdf"

)



==================================================
7. VALIDANDO DOWNLOAD
==================================================


Verificar nome:


assert (


"relatorio"


in download.suggested_filename


)



==================================================
8. TRABALHANDO COM IFRAMES
==================================================


Iframe é uma página dentro de outra página.


Exemplo:


<iframe

src="pagamento.html">

</iframe>



==================================================
9. LOCALIZANDO IFRAME
==================================================


frame = (


page.frame_locator(

"iframe"

)


)



Interagir:


frame.get_by_label(

"Cartão"

).fill(

"123456"

)



==================================================
10. IFRAME COM NOME
==================================================


frame = page.frame(

name="pagamento"

)



==================================================
11. MÚLTIPLAS ABAS DO NAVEGADOR
==================================================


Cenário:


Usuário clica:


Abrir contrato


↓

Nova aba



Capturar nova página:


with page.expect_popup() as popup_info:


    page.click(

    "text=Abrir contrato"

    )



nova_aba = popup_info.value



==================================================
12. TRABALHANDO COM NOVA ABA
==================================================


nova_aba.wait_for_load_state()



titulo = nova_aba.title()



assert titulo == "Contrato"



==================================================
13. MANIPULANDO VÁRIAS PÁGINAS
==================================================


pages = context.pages



print(

len(pages)

)



Resultado:


Página principal


Página nova



==================================================
14. POPUPS DO NAVEGADOR
==================================================


Exemplo:


alert(

"Confirmar exclusão"

)



Capturar:


page.on(


"dialog",


lambda dialog:


dialog.accept()


)



==================================================
15. TIPOS DE DIALOG
==================================================


Playwright suporta:


alert

OK


confirm

Aceitar/Cancelar


prompt

Digitar texto



==================================================
16. CONFIRM DIALOG
==================================================


Aceitar:


page.on(


"dialog",


lambda dialog:


dialog.accept()


)



Cancelar:


dialog.dismiss()



==================================================
17. PROMPT JAVASCRIPT
==================================================


Exemplo:


Digite seu nome



Código:


page.on(


"dialog",


lambda dialog:


dialog.accept(

"Natanael"

)


)



==================================================
18. DRAG AND DROP
==================================================


Cenário:


Arquivo


↓

Pasta



Código:


page.drag_and_drop(


"#arquivo",


"#pasta"


)



==================================================
19. MOUSE AVANÇADO
==================================================


O Playwright controla:


- Clique

- Duplo clique

- Movimento

- Arrastar



Clique:


page.mouse.click(


100,


200


)



Mover mouse:


page.mouse.move(


500,


300


)



==================================================
20. DUPLO CLIQUE
==================================================


page.mouse.dblclick(


200,


200


)



==================================================
21. CLIQUE BOTÃO DIREITO
==================================================


page.mouse.click(


100,


100,


button="right"


)



==================================================
22. TECLADO AVANÇADO
==================================================


Exemplo:


page.keyboard.press(


"Enter"

)



CTRL + A:


page.keyboard.press(


"Control+A"

)



Copiar:


page.keyboard.press(


"Control+C"

)



Colar:


page.keyboard.press(


"Control+V"

)



==================================================
23. DIGITANDO TEXTO
==================================================


page.keyboard.type(


"Playwright"


)



==================================================
24. EVENTOS DE PÁGINA
==================================================


Escutar eventos:


page.on(


"console",


lambda msg:


print(msg.text)


)



==================================================
25. EVENTOS DE REDE
==================================================


Capturar chamadas:


page.on(


"request",


lambda request:


print(request.url)


)



Resposta:


page.on(


"response",


lambda response:


print(response.status)


)



==================================================
26. ESPERANDO EVENTOS ESPECÍFICOS
==================================================


Exemplo:


with page.expect_request(


"**/api/login"


):


    page.click(

    "Entrar"

    )



==================================================
27. TRABALHANDO COM MÚLTIPLOS ELEMENTOS
==================================================


Encontrar vários:


lista = page.locator(

"li"

)



Quantidade:


print(

lista.count()

)



Percorrer:


for item in lista.all():

    print(

    item.text_content()

    )



==================================================
28. ELEMENTOS INVISÍVEIS
==================================================


Verificar:


expect(


page.locator(

"#erro"

)


).not_to_be_visible()



==================================================
29. CAMPOS DESABILITADOS
==================================================


expect(


page.locator(

"#botao"

)


).to_be_disabled()



==================================================
30. CAMPOS HABILITADOS
==================================================


expect(


page.locator(

"#botao"

)


).to_be_enabled()



==================================================
31. TESTANDO TABELAS
==================================================


HTML:


<table>

<tr>

<td>João</td>

</tr>

</table>



Buscar:


page.locator(

"table tr"

)



==================================================
32. TESTANDO MENUS
==================================================


Abrir:


page.hover(

"Menu"

)



Clicar opção:


page.click(

"Submenu"

)



==================================================
33. TESTANDO COMPONENTES MODERNOS
==================================================


Aplicações:


- React

- Angular

- Vue



Playwright funciona diretamente porque testa o navegador real.



==================================================
34. CENÁRIO PROFISSIONAL COMPLETO
==================================================


Sistema financeiro:


Login


↓

Abrir relatório


↓

Nova aba


↓

Gerar PDF


↓

Download arquivo


↓

Validar documento


↓

Registrar evidência



==================================================
35. BOAS PRÁTICAS
==================================================


Evite:


time.sleep(5)



Prefira:


page.wait_for_load_state()



ou:


expect(element)

.to_be_visible()



==================================================
RESULTADO DA PARTE 12
==================================================


Você aprendeu:


✅ Upload de arquivos

✅ Download automático

✅ Iframes

✅ Múltiplas abas

✅ Popups

✅ Alertas JavaScript

✅ Drag and Drop

✅ Mouse avançado

✅ Teclado

✅ Eventos de navegador

✅ Eventos de rede

✅ Tabelas

✅ Menus

✅ Componentes modernos



==================================================
PRÓXIMA ETAPA
==================================================


PARTE 13 — QUALIDADE E BOAS PRÁTICAS EM AUTOMAÇÃO PLAYWRIGHT


Conteúdo:


- Código limpo aplicado a testes

- SOLID para QA

- Design Patterns

- Estratégia de automação

- Pirâmide de testes

- Manutenção de testes

- Tratamento de erros

- Refatoração

- Padrões usados por equipes profissionais de QA

PARTE 13 — QUALIDADE E BOAS PRÁTICAS EM AUTOMAÇÃO PLAYWRIGHT

Código Limpo aplicado a testes, SOLID para QA,
Design Patterns, Estratégia de Automação,
Pirâmide de Testes, Manutenção e Refatoração


Nesta etapa vamos aprender como criar uma automação de testes profissional.

Um teste que apenas funciona não é suficiente.

Em empresas, a automação precisa ser:

✅ Fácil de manter
✅ Fácil de entender
✅ Reutilizável
✅ Escalável
✅ Confiável
✅ Rápida


==================================================
1. O QUE É QUALIDADE EM AUTOMAÇÃO?
==================================================


Automação de qualidade significa criar testes que:


- Encontram defeitos

- Possuem baixa manutenção

- Geram resultados confiáveis

- Podem crescer com o sistema



Exemplo ruim:


test_login.py


1000 linhas de código


Problemas:


❌ Difícil manutenção

❌ Código duplicado

❌ Alterações quebram vários testes



Exemplo profissional:


Teste

↓

Page Object

↓

Componentes

↓

Fixtures

↓

Utils



==================================================
2. PRINCÍPIOS DE CÓDIGO LIMPO
==================================================


Código limpo significa:


Código:

- Simples

- Organizado

- Legível

- Reutilizável



==================================================
3. NOMES CLAROS
==================================================


Evite:


def teste1():

    pass



Prefira:


def test_usuario_realiza_login_com_sucesso():

    pass



O nome deve explicar o comportamento.



==================================================
4. EVITAR DUPLICAÇÃO DE CÓDIGO
==================================================


Código ruim:


page.fill(

"#email",

"admin"

)


page.fill(

"#senha",

"123"

)



Repetido em vários testes.



Melhor:


Criar Page Object:


login_page.py



class LoginPage:


    def preencher_login(
        self,
        usuario,
        senha
    ):

        self.email.fill(usuario)

        self.senha.fill(senha)



==================================================
5. PRINCÍPIO DRY
==================================================


DRY:


Don't Repeat Yourself



Não repetir código.



Exemplo:


Criar:


utils/helpers.py



Função:


def gerar_usuario():

    return {

    "nome":"Teste"

    }



Usar em vários testes.



==================================================
6. PRINCÍPIO KISS
==================================================


KISS:


Keep It Simple



Evitar:


Código complexo


Prefira:


Código simples e direto.



==================================================
7. PRINCÍPIO YAGNI
==================================================


YAGNI:


You Aren't Gonna Need It



Não criar funcionalidades antes da necessidade.



Exemplo:


Criar 50 funções que nunca serão usadas.


Evitar.



==================================================
8. SOLID APLICADO A QA
==================================================


SOLID são princípios para criar sistemas organizados.


Também aplicamos em automação.



==================================================
S — SINGLE RESPONSIBILITY
==================================================


Uma classe deve ter uma única responsabilidade.



Errado:


LoginPage:


- Faz login

- Gera relatório

- Salva arquivo

- Envia email



Correto:


LoginPage


Responsável apenas por login.



ReportService


Responsável por relatórios.



==================================================
O — OPEN/CLOSED
==================================================


Aberto para extensão.

Fechado para alteração.



Exemplo:


Criar:


BrowserFactory



Permitir:


Chrome

Firefox

WebKit



Sem alterar todos testes.



==================================================
L — LISKOV SUBSTITUTION
==================================================


Objetos devem poder ser substituídos sem quebrar o sistema.



Exemplo:


Browser:


Chromium


Firefox


WebKit



Todos devem funcionar com mesma interface.



==================================================
I — INTERFACE SEGREGATION
==================================================


Não criar interfaces gigantes.



Separar responsabilidades.



Exemplo:


Evitar:


UsuarioService:


- Criar usuário

- Gerar relatório

- Login

- Exportar arquivo



Separar:


UsuarioService


ReportService


AuthService



==================================================
D — DEPENDENCY INVERSION
==================================================


Depender de abstrações.


Não criar:


Teste depende diretamente do navegador.



Melhor:


Teste depende de fixture.


Fixture controla navegador.



==================================================
9. DESIGN PATTERNS EM AUTOMAÇÃO
==================================================


Padrões comuns:


- Page Object Model

- Factory Pattern

- Singleton

- Strategy Pattern

- Builder Pattern



==================================================
10. PAGE OBJECT MODEL (POM)
==================================================


Padrão mais utilizado em QA.



Estrutura:


pages


├── login_page.py

├── produto_page.py

└── checkout_page.py



Teste:


test_login.py



Responsabilidade:


Teste valida comportamento.


Page contém elementos.



==================================================
11. FACTORY PATTERN
==================================================


Criar objetos dinamicamente.



Exemplo:


BrowserFactory


Retorna:


Chromium


Firefox


WebKit



Código:


class BrowserFactory:


    def criar(
        navegador
    ):


        if navegador=="chrome":

            return Chromium()



==================================================
12. SINGLETON
==================================================


Garantir uma única instância.



Uso:


Configuração global


Banco


Logs



Exemplo:


Uma única configuração carregada.



==================================================
13. STRATEGY PATTERN
==================================================


Permite trocar comportamento.



Exemplo:


Login:


Login normal


Login OAuth


Login JWT



Mesmo teste usando estratégias diferentes.



==================================================
14. BUILDER PATTERN
==================================================


Criar objetos complexos.



Exemplo:


Cadastro:


Usuário


+

Endereço


+

Pagamento



==================================================
15. PIRÂMIDE DE TESTES
==================================================


Estratégia profissional:


              /\

             /  \

            / UI \

           /------\

          / API    \

         /----------\

        / Unitários  \

       ---------------



Quanto mais alto:


- Mais lento

- Mais caro



==================================================
16. DISTRIBUIÇÃO IDEAL
==================================================


Exemplo:


70%

Testes Unitários



20%

Testes API



10%

Testes UI



==================================================
17. TESTES UI COM PLAYWRIGHT
==================================================


Usar para:


✅ Fluxos críticos

✅ Login

✅ Compra

✅ Cadastro

✅ Processos principais



Evitar:


Testar tudo pela interface.



==================================================
18. TRATAMENTO DE ERROS
==================================================


Exemplo:


try:


    page.click(
    "Enviar"
    )


except Exception as erro:


    logger.error(erro)



==================================================
19. RETRY DE TESTES
==================================================


Testes instáveis podem tentar novamente.



Instalar:


uv add pytest-rerunfailures



Executar:


pytest --reruns 2



==================================================
20. TESTES FLAKY
==================================================


Flaky Test:


Teste que:


Às vezes passa

Às vezes falha



Causas:


- Esperas incorretas

- Dados compartilhados

- Dependência externa



==================================================
21. ISOLAMENTO DE TESTES
==================================================


Cada teste deve ser independente.



Errado:


Teste 2 depende do resultado do Teste 1



Correto:


Cada teste prepara seu próprio cenário.



==================================================
22. GESTÃO DE DADOS DE TESTE
==================================================


Utilizar:


- JSON

- YAML

- Banco de dados

- APIs



Evitar dados fixos dentro do teste.



==================================================
23. VERSIONAMENTO
==================================================


Automação deve estar no:


Git



Estrutura:


main


develop


feature/test-login



==================================================
24. CODE REVIEW DE TESTES
==================================================


Antes de aceitar:


Verificar:


✅ Código limpo

✅ Sem duplicação

✅ Boa nomenclatura

✅ Evidências

✅ Cobertura



==================================================
25. PADRÃO PROFISSIONAL DE PROJETO
==================================================


Automacao-Playwright


│

├── tests

│

├── pages

│

├── components

│

├── api

│

├── fixtures

│

├── services

│

├── utils

│

├── config

│

├── reports

│

├── logs

│

└── data



==================================================
26. FLUXO PROFISSIONAL QA
==================================================


Requisito


↓

Caso de teste


↓

Automação


↓

Execução


↓

Relatório


↓

Análise


↓

Melhoria contínua



==================================================
RESULTADO DA PARTE 13
==================================================


Você aprendeu:


✅ Código limpo para QA

✅ DRY

✅ KISS

✅ YAGNI

✅ SOLID aplicado a testes

✅ Design Patterns

✅ Page Object Model

✅ Estratégia de automação

✅ Pirâmide de testes

✅ Tratamento de erros

✅ Testes estáveis

✅ Manutenção profissional



==================================================
PRÓXIMA ETAPA
==================================================


PARTE 14 — DOCKER + PLAYWRIGHT


Conteúdo:


- O que é Docker

- Criando ambiente de testes

- Dockerfile

- Containers

- Imagens

- Execução Playwright em container

- Docker Compose

- Integração com CI/CD

- Ambiente profissional reproduzível
  PARTE 14 — DOCKER + PLAYWRIGHT

Docker, Containers, Imagens, Dockerfile,
Execução de Testes em Container, Docker Compose e CI/CD


Nesta etapa vamos aprender como executar o framework Playwright dentro de containers Docker.

Empresas utilizam Docker para garantir que:

✅ Todos executem os testes no mesmo ambiente
✅ Dependências sejam controladas
✅ O CI/CD tenha ambiente reproduzível
✅ Problemas de máquina sejam reduzidos


==================================================
1. O QUE É DOCKER?
==================================================


Docker é uma plataforma para criar e executar containers.


Um container é um ambiente isolado contendo:


- Sistema operacional mínimo

- Python

- Bibliotecas

- Playwright

- Navegadores

- Código de testes



Exemplo:


Computador


↓

Docker


↓

Container Playwright


↓

Executa testes



==================================================
2. POR QUE USAR DOCKER EM AUTOMAÇÃO?
==================================================


Sem Docker:


Máquina A:

Python 3.12

Playwright X


Máquina B:

Python 3.11

Playwright Y



Resultado:


❌ Testes diferentes

❌ Falhas inesperadas



Com Docker:


Todos usam:


Mesmo Python

Mesmo Playwright

Mesmo Browser



==================================================
3. CONCEITOS IMPORTANTES
==================================================


IMAGE


É o modelo do ambiente.



Exemplo:


Imagem Playwright Python



CONTAINER


É uma execução da imagem.



Exemplo:


Container executando testes.



DOCKERFILE


Arquivo que cria a imagem.



==================================================
4. INSTALANDO DOCKER
==================================================


Instalar:


Docker Desktop



Verificar:


docker --version



Resultado:


Docker version 28.x.x



==================================================
5. ESTRUTURA DO PROJETO COM DOCKER
==================================================


Automacao-Playwright


│

├── tests

│

├── pages

│

├── reports

│

├── screenshots

│

├── Dockerfile

│

├── docker-compose.yml

│

├── requirements.txt

│

└── pytest.ini



==================================================
6. ARQUIVO requirements.txt
==================================================


Criar:


requirements.txt



Conteúdo:


pytest

pytest-playwright

pytest-html

pytest-xdist

python-dotenv

loguru



==================================================
7. CRIANDO DOCKERFILE
==================================================


Criar:


Dockerfile



Conteúdo:


FROM mcr.microsoft.com/playwright/python:v1.55.0



WORKDIR /app



COPY requirements.txt .



RUN pip install -r requirements.txt



COPY . .



CMD [

"pytest"

]



==================================================
8. ENTENDENDO O DOCKERFILE
==================================================


FROM


Define a imagem base.



WORKDIR


Define pasta de trabalho.



COPY


Copia arquivos para o container.



RUN


Executa comandos.



CMD


Comando inicial.



==================================================
9. CRIANDO IMAGEM DOCKER
==================================================


Executar:


docker build -t automacao-playwright .



O Docker:


1 - Baixa imagem Python


2 - Instala dependências


3 - Copia projeto


4 - Cria ambiente



==================================================
10. EXECUTANDO CONTAINER
==================================================


Comando:


docker run automacao-playwright



Resultado:


Container inicia


↓

Executa Pytest


↓

Gera resultado



==================================================
11. EXECUTANDO COM RELATÓRIOS
==================================================


Comando:


docker run \

-v $(pwd)/reports:/app/reports \

automacao-playwright



O relatório fica disponível na máquina.



==================================================
12. DOCKER COM PLAYWRIGHT BROWSER
==================================================


Imagem oficial:


mcr.microsoft.com/playwright/python



Ela já possui:


✅ Chromium

✅ Firefox

✅ WebKit



Não precisa instalar manualmente.



==================================================
13. EXECUÇÃO HEADLESS
==================================================


No Docker normalmente:


Browser roda sem interface gráfica.



Modo:


Headless



Exemplo:


pytest



==================================================
14. EXECUÇÃO HEADED COM DISPLAY
==================================================


Para abrir navegador:


Necessário:


X Server


ou


VNC



Usado principalmente para debug.



==================================================
15. DOCKER COM VARIÁVEIS .env
==================================================


Arquivo:


.env



Exemplo:


BASE_URL=https://hml.site.com

USER=admin

PASSWORD=123



Executar:


docker run --env-file .env automacao-playwright



==================================================
16. DOCKER COM VOLUMES
==================================================


Volumes permitem compartilhar arquivos.



Exemplo:


Código local:


./reports



Container:


/app/reports



Comando:


docker run \

-v ./reports:/app/reports \

automacao-playwright



==================================================
17. DOCKER COM DOCKER COMPOSE
==================================================


Docker Compose gerencia vários containers.



Criar:


docker-compose.yml



==================================================
18. EXEMPLO docker-compose.yml
==================================================


version:


'3'



services:


  testes:


    build: .


    volumes:


      - ./reports:/app/reports


    environment:


      BASE_URL:

      https://hml.site.com



==================================================
19. EXECUTANDO COM COMPOSE
==================================================


Criar ambiente:


docker compose build



Executar:


docker compose up



==================================================
20. PARA EXECUTAR TESTES ESPECÍFICOS
==================================================


Exemplo:


docker compose run testes pytest tests/test_login.py



==================================================
21. PARALELISMO COM DOCKER
==================================================


Usando:


pytest-xdist



Comando:


pytest -n auto



Docker pode executar vários containers:


Container 1

Teste Login


Container 2

Teste Cadastro


Container 3

Teste Compra



==================================================
22. DOCKER NO GITHUB ACTIONS
==================================================


Fluxo:


Git Push


↓

GitHub Actions


↓

Criar Container


↓

Instalar ambiente


↓

Executar Playwright


↓

Gerar relatório



==================================================
23. EXEMPLO PIPELINE
==================================================


.github/workflows/test.yml



Fluxo:


name:

Playwright Tests



steps:


Checkout código



↓

Configurar Docker



↓

Build imagem



↓

Executar testes



==================================================
24. BENEFÍCIOS NO CI/CD
==================================================


Com Docker:


✅ Ambiente igual produção

✅ Menos erros

✅ Execução automática

✅ Fácil manutenção

✅ Escalabilidade



==================================================
25. BOAS PRÁTICAS DOCKER + PLAYWRIGHT
==================================================


Utilizar:


✅ Imagem oficial Playwright

✅ .dockerignore

✅ Variáveis ambiente

✅ Volumes para relatórios

✅ Logs externos

✅ Containers pequenos



==================================================
26. ARQUIVO .dockerignore
==================================================


Criar:


.dockerignore



Conteúdo:


.git

.pytest_cache

__pycache__

reports

screenshots



==================================================
27. ESTRUTURA FINAL PROFISSIONAL
==================================================


Automacao-Playwright


│

├── tests

├── pages

├── api

├── fixtures

├── config

├── utils

├── reports

├── logs

├── Dockerfile

├── docker-compose.yml

├── .env

├── pytest.ini

└── requirements.txt



==================================================
28. FLUXO PROFISSIONAL COMPLETO
==================================================


Desenvolvedor


↓

Git Push


↓

GitHub Actions


↓

Docker Build


↓

Criar Container


↓

Executar Playwright


↓

Gerar Evidências


↓

Publicar Relatório



==================================================
RESULTADO DA PARTE 14
==================================================


Você aprendeu:


✅ Conceito de Docker

✅ Containers

✅ Imagens

✅ Dockerfile

✅ Docker Compose

✅ Executar Playwright em container

✅ Variáveis .env

✅ Volumes

✅ Paralelismo

✅ Integração CI/CD

✅ Ambiente profissional reproduzível



==================================================
PRÓXIMA ETAPA
==================================================


PARTE 15 — PROJETO FINAL PROFISSIONAL PLAYWRIGHT


Conteúdo:


- Criar framework completo

- Arquitetura final

- Testes UI + API

- POM

- Fixtures

- Docker

- CI/CD

- Relatórios

- Evidências

- README profissional

- Projeto pronto para portfólio GitHub
  PARTE 15 — PROJETO FINAL PROFISSIONAL PLAYWRIGHT

Framework Completo de Automação,
Arquitetura Final, UI + API, POM, Fixtures,
Docker, CI/CD, Relatórios, Evidências e Portfólio GitHub


Nesta etapa vamos montar a estrutura final de um projeto profissional de automação de testes usando:

✅ Python
✅ Playwright
✅ Pytest
✅ API Testing
✅ Page Object Model
✅ Docker
✅ GitHub Actions
✅ Relatórios
✅ Evidências


O objetivo é criar um framework semelhante ao utilizado em empresas de QA.



==================================================
1. OBJETIVO DO PROJETO FINAL
==================================================


Criar uma automação capaz de:


- Testar aplicações Web

- Testar APIs REST

- Executar em diferentes navegadores

- Gerar relatórios

- Capturar evidências

- Rodar automaticamente no CI/CD

- Ser mantida por uma equipe



==================================================
2. ARQUITETURA FINAL DO FRAMEWORK
==================================================


Estrutura:


Automacao-Playwright


│

├── tests

│   ├── ui

│   │   ├── test_login.py

│   │   ├── test_cadastro.py

│   │

│   └── api

│       ├── test_usuario_api.py


│

├── pages

│   ├── login_page.py

│   ├── cadastro_page.py


│

├── components

│   ├── menu_component.py

│   └── modal_component.py


│

├── api

│   ├── api_client.py

│   └── usuario_api.py


│

├── fixtures

│   └── browser.py


│

├── config

│   └── settings.py


│

├── data

│   └── usuarios.json


│

├── utils

│   ├── logger.py

│   └── helpers.py


│

├── reports


├── screenshots


├── videos


├── logs


├── Dockerfile


├── docker-compose.yml


├── pytest.ini


├── requirements.txt


├── .env


└── README.md



==================================================
3. CAMADA DE TESTES
==================================================


Responsabilidade:


Executar cenários.


Exemplo:


tests/ui/test_login.py



Código:


def test_login_sucesso(page):


    page.goto(
    "/login"
    )


    page.fill(
    "#email",
    "admin"
    )


    page.fill(
    "#senha",
    "123456"
    )


    page.click(
    "#entrar"
    )


    assert (
    "Dashboard"
    in page.title()
    )



==================================================
4. PAGE OBJECT MODEL
==================================================


Objetivo:


Separar:


Teste


de


Elementos da página.



Estrutura:


pages/login_page.py



Exemplo:


class LoginPage:


    def __init__(
        self,
        page
    ):


        self.page = page


        self.email = (

        page.locator(
        "#email"
        )

        )


        self.senha = (

        page.locator(
        "#senha"
        )

        )


        self.botao = (

        page.locator(
        "#entrar"
        )

        )



    def login(
        self,
        usuario,
        senha
    ):


        self.email.fill(usuario)


        self.senha.fill(senha)


        self.botao.click()



==================================================
5. TESTE USANDO PAGE OBJECT
==================================================


test_login.py



Código:


from pages.login_page import LoginPage



def test_login(page):


    login = LoginPage(page)


    login.login(

    "admin",

    "123456"

    )



==================================================
6. COMPONENTES REUTILIZÁVEIS
==================================================


Componentes comuns:


- Menu

- Barra de pesquisa

- Modal

- Tabela

- Alertas



Exemplo:


components/menu_component.py



class Menu:


    def __init__(
        self,
        page
    ):

        self.page = page



    def abrir_usuario(self):

        self.page.click(
        "text=Usuários"
        )



==================================================
7. FIXTURES PROFISSIONAIS
==================================================


Arquivo:


conftest.py



Responsável por:


- Browser

- Context

- Dados

- Configurações



Exemplo:


@pytest.fixture


def usuario_teste():


    return {


    "email":

    "admin@email.com",


    "senha":

    "123456"


    }



==================================================
8. CONFIGURAÇÃO POR AMBIENTE
==================================================


Ambientes:


DEV


HML


PROD



Arquivos:


config


├── dev.env

├── hml.env

└── prod.env



Exemplo:


BASE_URL=https://hml.site.com



==================================================
9. VARIÁVEIS .ENV
==================================================


Arquivo:


.env



Exemplo:


BASE_URL=https://site.com

USER=admin

PASSWORD=123456



Nunca colocar senha diretamente no código.



==================================================
10. TESTES DE API
==================================================


Estrutura:


api


├── api_client.py

└── usuario_api.py



Exemplo:


class UsuarioAPI:


    def criar_usuario(
        self,
        usuario
    ):


        return self.client.post(

        "/usuarios",

        usuario

        )



==================================================
11. INTEGRAÇÃO API + UI
==================================================


Cenário:


Criar usuário pela API


↓

Abrir sistema


↓

Validar usuário na tela



Benefício:


Testes mais rápidos e completos.



==================================================
12. RELATÓRIOS PROFISSIONAIS
==================================================


Utilizar:


pytest-html



Executar:


pytest --html=report.html



Resultado:


reports


└── report.html



==================================================
13. CAPTURA DE SCREENSHOTS
==================================================


Quando teste falhar:


page.screenshot(


path="screenshots/falha.png"


)



==================================================
14. GRAVAÇÃO DE VÍDEOS
==================================================


Configuração:


context = browser.new_context(

record_video_dir="videos/"

)



Resultado:


videos


└── teste.webm



==================================================
15. LOGS PROFISSIONAIS
==================================================


Utilizar:


Loguru



Exemplo:


logger.info(

"Iniciando teste login"

)



Arquivo:


logs/testes.log



==================================================
16. EXECUÇÃO MULTI-BROWSER
==================================================


Executar:


Chromium:


pytest --browser chromium



Firefox:


pytest --browser firefox



WebKit:


pytest --browser webkit



==================================================
17. EXECUÇÃO PARALELA
==================================================


Instalar:


pytest-xdist



Executar:


pytest -n auto



Benefício:


Reduz tempo de execução.



==================================================
18. DOCKER NO PROJETO
==================================================


Arquivos:


Dockerfile


docker-compose.yml



Objetivo:


Garantir mesmo ambiente para todos.



==================================================
19. DOCKERFILE FINAL
==================================================


FROM mcr.microsoft.com/playwright/python:v1.55.0



WORKDIR /app



COPY requirements.txt .



RUN pip install -r requirements.txt



COPY . .



CMD ["pytest"]



==================================================
20. DOCKER COMPOSE
==================================================


docker-compose.yml



Exemplo:


services:


  testes:


    build: .


    volumes:


      - ./reports:/app/reports



==================================================
21. PIPELINE CI/CD
==================================================


Fluxo:


Código


↓

Git Push


↓

GitHub Actions


↓

Docker


↓

Playwright


↓

Testes


↓

Relatório



==================================================
22. ESTRUTURA GITHUB ACTIONS
==================================================


.github


└── workflows


    └── tests.yml



Executa:


- Instala ambiente

- Instala dependências

- Executa testes

- Publica relatório



==================================================
23. README PROFISSIONAL
==================================================


O projeto deve conter:


Título


Descrição


Tecnologias


Como instalar


Como executar


Estrutura


Exemplos


Resultados



==================================================
24. EXEMPLO DE EXECUÇÃO
==================================================


Comando:


uv run pytest



Resultado:


========================


10 testes executados


10 aprovados


Relatório gerado



========================



==================================================
25. FLUXO FINAL DO FRAMEWORK
==================================================


Requisito


↓

Caso de teste


↓

Automação Playwright


↓

Execução local


↓

Docker


↓

CI/CD


↓

Relatório


↓

Análise QA



==================================================
26. COMPETÊNCIAS DESENVOLVIDAS
==================================================


Após concluir este projeto você domina:


✅ Python para QA

✅ Playwright

✅ Pytest

✅ Page Object Model

✅ Fixtures

✅ API Testing

✅ REST

✅ JWT

✅ Mock

✅ Docker

✅ GitHub Actions

✅ CI/CD

✅ Relatórios

✅ Arquitetura profissional



==================================================
27. PROJETO PARA PORTFÓLIO
==================================================


No GitHub apresentar:


Nome:


Automacao-Web-Playwright-Python



Descrição:


Framework profissional de automação de testes utilizando Python, Playwright e Pytest com testes UI, API, Docker e CI/CD.



Demonstrar:


- Código organizado

- Evidências

- Relatórios

- Pipeline funcionando



==================================================
28. CONCLUSÃO DO CURSO
==================================================


Você saiu de:


Teste simples:


Abrir navegador

Clicar botão



Para:


Framework profissional:


Arquitetura

+

Automação UI

+

API

+

Docker

+

CI/CD

+

Relatórios

+

Boas práticas QA



==================================================
FIM DA TRILHA PRINCIPAL
==================================================


Próximos níveis:


PARTE 16 — Playwright + Inteligência Artificial para QA


Conteúdo:


- IA criando casos de teste

- Geração automática de scripts

- Análise de falhas

- ChatGPT/Copilot para QA


PARTE 17 — Mercado de Trabalho QA Automation


Conteúdo:


- Como montar portfólio

- Projetos para GitHub

- Perguntas de entrevista

- Cenários reais de empresas

- Preparação para vaga QA Automation
  PARTE 16 — PLAYWRIGHT + INTELIGÊNCIA ARTIFICIAL PARA QA

IA aplicada à Automação de Testes,
Geração de Casos de Teste, Criação de Scripts,
Análise de Falhas, ChatGPT, Copilot e IA para QA


Nesta etapa vamos aprender como utilizar Inteligência Artificial para aumentar a produtividade de profissionais de QA Automation.

A IA não substitui o conhecimento de testes.

Ela funciona como uma ferramenta para:

✅ Criar casos de teste
✅ Gerar código Playwright
✅ Encontrar melhorias
✅ Analisar falhas
✅ Documentar testes
✅ Aumentar produtividade



==================================================
1. O PAPEL DA IA NO QA
==================================================


Antes:


Analista QA


↓

Analisa requisito


↓

Cria casos de teste


↓

Escreve automação


↓

Executa testes



Com IA:


Analista QA


↓

IA auxilia análise


↓

Gera sugestões


↓

QA valida


↓

Automação final



==================================================
2. IA NO CICLO DE TESTES
==================================================


Aplicações:


Planejamento


↓

Criação de cenários


↓

Automação


↓

Execução


↓

Análise de resultados


↓

Melhoria contínua



==================================================
3. GERAÇÃO DE CASOS DE TESTE COM IA
==================================================


Exemplo:


Requisito:


"Usuário deve conseguir realizar login"



IA pode gerar:


Caso 1:

Login com usuário válido


Entrada:

Email correto

Senha correta


Resultado esperado:

Usuário acessa dashboard



--------------------------


Caso 2:

Senha inválida


Entrada:

Email correto

Senha errada


Resultado esperado:

Mensagem de erro



--------------------------


Caso 3:

Campos vazios


Resultado:

Sistema bloqueia acesso



==================================================
4. CRIANDO CENÁRIOS BDD COM IA
==================================================


Formato:


GIVEN

WHEN

THEN



Exemplo:


Feature:

Login



Scenario:

Usuário realiza login válido



Given:

Usuário está na página login



When:

Informa usuário e senha válidos



Then:

Sistema direciona para dashboard



==================================================
5. GERANDO TESTES PLAYWRIGHT COM IA
==================================================


Comando para IA:


"Crie um teste Playwright Python para validar login"



Resultado esperado:


from playwright.sync_api import expect



def test_login(page):


    page.goto(

    "/login"

    )


    page.fill(

    "#email",

    "admin@email.com"

    )


    page.fill(

    "#senha",

    "123456"

    )


    page.click(

    "#entrar"

    )


    expect(

    page

    ).to_have_url(

    "/dashboard"

    )



==================================================
6. IA AUXILIANDO PAGE OBJECT MODEL
==================================================


Solicitação:


"Crie Page Object para tela Login"



Resultado:


pages/login_page.py



class LoginPage:


    def __init__(
        self,
        page
    ):

        self.page = page


        self.email = page.locator(
        "#email"
        )


        self.senha = page.locator(
        "#senha"
        )



    def login(
        self,
        email,
        senha
    ):


        self.email.fill(email)


        self.senha.fill(senha)



==================================================
7. GERAÇÃO DE LOCATORS COM IA
==================================================


Problema:


HTML complexo.



IA pode sugerir:


Antes:


div:nth-child(4)



Depois:


page.get_by_role(

"button",

name="Entrar"

)



Melhor:


- Mais estável

- Mais legível

- Mais profissional



==================================================
8. IA ANALISANDO ERROS
==================================================


Exemplo:


Erro:


TimeoutError:

Element not found



IA pode analisar:


Possíveis causas:


- Locator incorreto

- Elemento carregando tarde

- Necessário esperar

- Mudança no HTML



Solução:


Usar:


expect()


wait_for()


melhor locator



==================================================
9. IA PARA MELHORAR TESTES FLAKY
==================================================


Teste flaky:


Uma hora passa.

Outra hora falha.



IA ajuda:


Encontrar:


- Esperas inadequadas

- Dependência entre testes

- Dados compartilhados

- Problemas de ambiente



==================================================
10. IA PARA DOCUMENTAÇÃO
==================================================


A IA pode criar:


README


Casos de teste


Documentação técnica


Comentários de código


Relatórios



Exemplo:


Entrada:


"Explique esse teste"



Saída:


Descrição do cenário


Passos executados


Resultado esperado



==================================================
11. IA + GITHUB COPILOT
==================================================


Copilot auxilia:


- Completar código

- Criar funções

- Sugerir melhorias

- Encontrar erros



Exemplo:


Digitando:


def test_login



IA sugere:


Estrutura completa do teste.



==================================================
12. IA PARA REFATORAÇÃO
==================================================


Código antigo:


100 linhas



IA pode sugerir:


- Criar Page Object

- Remover repetição

- Melhorar nomes

- Separar responsabilidades



==================================================
13. IA GERANDO MASSA DE TESTES
==================================================


Exemplo:


Criar usuários:


Usuário 1:

Nome:

João


Email:

joao@email.com



Usuário 2:

Nome:

Maria


Email:

maria@email.com



Pode gerar:


JSON


CSV


SQL


Dados fictícios



==================================================
14. IA TESTANDO APIs
==================================================


Solicitação:


"Crie testes API REST usando Playwright"



Pode gerar:


GET


POST


PUT


DELETE


JWT


Headers


Validação JSON



==================================================
15. IA + TESTE DE CONTRATO
==================================================


IA ajuda criar:


Schemas JSON


Validações


Modelos de resposta



Exemplo:


Validar:


"id"


"nome"


"email"



==================================================
16. IA PARA ANÁLISE DE RELATÓRIOS
==================================================


Entrada:


Relatório de execução:


100 testes


5 falhas



IA pode:


- Agrupar erros

- Identificar padrões

- Sugerir correções

- Priorizar problemas



==================================================
17. IA NO CI/CD
==================================================


Pipeline:


GitHub Actions


↓

Executa testes


↓

Gera relatório


↓

IA analisa falhas


↓

Envia resumo



==================================================
18. EXEMPLO DE FLUXO PROFISSIONAL
==================================================


Desenvolvedor:


Entrega requisito



↓

QA usa IA


Cria cenários



↓

QA cria Playwright


Automação



↓

Pipeline executa



↓

IA analisa resultados



↓

Equipe corrige



==================================================
19. FERRAMENTAS DE IA PARA QA
==================================================


Exemplos:


ChatGPT


Uso:


- Criar testes

- Explicar erros

- Refatorar código



GitHub Copilot


Uso:


- Autocomplete

- Sugestões de código



Ferramentas de Test Management com IA


Uso:


- Casos de teste

- Documentação



==================================================
20. BOAS PRÁTICAS USANDO IA
==================================================


Sempre:


✅ Revisar código gerado

✅ Validar regras de negócio

✅ Não enviar dados sensíveis

✅ Entender o código criado

✅ Manter padrões do projeto



==================================================
21. IA NÃO SUBSTITUI QA
==================================================


A IA não substitui:


- Pensamento crítico

- Conhecimento do sistema

- Estratégia de testes

- Análise de risco



O profissional continua responsável pela qualidade.



==================================================
22. FRAMEWORK PLAYWRIGHT + IA
==================================================


Arquitetura:


Automacao-Playwright



+

IA



↓

Geração de testes


↓

Análise de falhas


↓

Melhoria contínua



==================================================
RESULTADO DA PARTE 16
==================================================


Você aprendeu:


✅ IA aplicada ao QA

✅ Geração de casos de teste

✅ Geração de scripts Playwright

✅ Criação de Page Objects

✅ Melhoria de Locators

✅ Análise de erros

✅ Redução de testes flaky

✅ Documentação automática

✅ IA no CI/CD

✅ Uso profissional de ChatGPT e Copilot



==================================================
PRÓXIMA ETAPA
==================================================


PARTE 17 — PLAYWRIGHT PARA MERCADO DE TRABALHO QA AUTOMATION


Conteúdo:


- Como montar portfólio profissional

- Projeto GitHub

- README de qualidade

- Perguntas de entrevista

- Cenários reais de empresas

- Competências exigidas

- Plano para conseguir vaga QA Automation
  PARTE 17 — PLAYWRIGHT PARA MERCADO DE TRABALHO QA AUTOMATION

Como montar portfólio profissional,
Projeto GitHub, README, Entrevistas,
Cenários reais de empresas e preparação para vaga QA Automation


Nesta etapa final vamos transformar todo conhecimento adquirido em um perfil profissional para o mercado de trabalho.

O objetivo é apresentar um projeto que demonstre:

✅ Conhecimento técnico
✅ Organização profissional
✅ Capacidade de automação
✅ Conhecimento de QA
✅ Experiência prática


==================================================
1. O QUE EMPRESAS BUSCAM EM QA AUTOMATION
==================================================


Um profissional QA Automation precisa dominar:


Conhecimentos técnicos:


✅ Python

✅ Playwright

✅ Selenium (diferencial)

✅ Pytest

✅ API Testing

✅ REST

✅ SQL

✅ Git

✅ CI/CD

✅ Docker



Conhecimentos de QA:


✅ Casos de teste

✅ Cenários

✅ Estratégia de testes

✅ Bugs

✅ Evidências

✅ Qualidade de software



==================================================
2. PERFIL DE UM QA AUTOMATION JÚNIOR
==================================================


O profissional deve saber:


- Criar testes automatizados

- Encontrar elementos na página

- Criar Page Objects

- Trabalhar com APIs

- Executar testes

- Analisar falhas

- Gerar relatórios



==================================================
3. PERFIL PLENO
==================================================


Além do básico:


- Criar frameworks

- Melhorar arquitetura

- Configurar CI/CD

- Trabalhar com Docker

- Revisar código

- Apoiar outros QAs



==================================================
4. PROJETO PARA PORTFÓLIO
==================================================


Criar um projeto no GitHub:


Nome:


Automacao-Web-Playwright-Python



Descrição:


Framework profissional de automação de testes utilizando Python, Playwright e Pytest com testes Web, API, Docker e CI/CD.



==================================================
5. ESTRUTURA DO REPOSITÓRIO
==================================================


GitHub:


Automacao-Web-Playwright-Python



│

├── tests

│

├── pages

│

├── api

│

├── fixtures

│

├── config

│

├── data

│

├── reports

│

├── screenshots

│

├── videos

│

├── logs

│

├── Dockerfile

│

├── docker-compose.yml

│

├── pytest.ini

│

├── requirements.txt

│

└── README.md



==================================================
6. README PROFISSIONAL
==================================================


Todo projeto deve possuir documentação.



Estrutura:


# Automação Web Playwright Python



## Sobre o projeto


Framework de automação utilizando:


- Python

- Playwright

- Pytest



## Funcionalidades


✔ Testes Web


✔ Testes API


✔ Page Object Model


✔ Relatórios


✔ Docker


✔ CI/CD



==================================================
7. DOCUMENTAR INSTALAÇÃO
==================================================


Exemplo:


Instalar dependências:


uv sync



Instalar browsers:


playwright install



Executar:


pytest



==================================================
8. MOSTRAR RESULTADOS
==================================================


Adicionar:


Screenshots


Vídeos


Relatórios HTML


Badges CI/CD



Exemplo:


Tests:


✅ 50 aprovados

❌ 0 falhas



==================================================
9. CASOS DE TESTE PARA PORTFÓLIO
==================================================


Criar cenários reais:


Login:


- Login válido

- Senha inválida

- Usuário bloqueado



Cadastro:


- Criar usuário

- Validar campos

- Mensagens de erro



Compra:


- Adicionar produto

- Finalizar pedido

- Validar pagamento



==================================================
10. PROJETO COMPLETO DE DEMONSTRAÇÃO
==================================================


Aplicação exemplo:


Sistema E-commerce



Testes:


Login


↓

Produtos


↓

Carrinho


↓

Checkout


↓

Pagamento



==================================================
11. COMO APRESENTAR O PROJETO
==================================================


Em entrevista:


"Desenvolvi um framework de automação utilizando Python, Playwright e Pytest."


"Implementei Page Object Model, testes API, Docker e pipeline CI/CD."


"Os testes geram relatórios e evidências automaticamente."



==================================================
12. PERGUNTAS DE ENTREVISTA PLAYWRIGHT
==================================================


Pergunta:


O que é Playwright?



Resposta:


Framework de automação criado pela Microsoft para testes de aplicações Web utilizando navegadores reais.



==================================================
13. DIFERENÇA SELENIUM X PLAYWRIGHT
==================================================


Selenium:


- Mais antigo

- Grande comunidade

- Depende mais de configuração



Playwright:


- Mais moderno

- Auto wait

- Suporte Chromium, Firefox e WebKit

- API integrada



==================================================
14. O QUE É PAGE OBJECT MODEL?
==================================================


Resposta:


É um padrão que separa os elementos e ações das páginas dos testes, facilitando manutenção e reutilização.



==================================================
15. O QUE SÃO FIXTURES?
==================================================


Resposta:


São recursos do Pytest utilizados para preparar ambientes, dados e objetos antes da execução dos testes.



==================================================
16. COMO EVITAR TESTES FLAKY?
==================================================


Resposta:


Utilizar:


- Esperas automáticas

- Locators estáveis

- Dados isolados

- Boa arquitetura

- Evitar dependência entre testes



==================================================
17. COMO TESTAR APIs?
==================================================


Resposta:


Utilizando:


- APIRequestContext

- GET

- POST

- PUT

- DELETE

- Headers

- Tokens JWT



==================================================
18. COMO EXECUTAR TESTES NO CI/CD?
==================================================


Resposta:


Utilizando:


GitHub Actions


↓

Instala dependências


↓

Executa Pytest


↓

Gera relatório



==================================================
19. PERGUNTAS DE QA GERAL
==================================================


O que é teste de software?


Resposta:


Processo de avaliar um sistema para encontrar defeitos e garantir qualidade.



--------------------------------------------------


Diferença entre teste funcional e não funcional:



Funcional:


Valida funcionalidades.



Não funcional:


Valida desempenho, segurança e usabilidade.



--------------------------------------------------


O que é bug?


Resposta:


Comportamento diferente do esperado.



==================================================
20. FERRAMENTAS IMPORTANTES PARA APRENDER
==================================================


Automação:


Playwright

Selenium

Cypress



API:


Postman

Rest Assured



Gestão:


Jira

Azure DevOps



CI/CD:


GitHub Actions

Jenkins



Banco:


SQL



==================================================
21. PLANO DE ESTUDO QA AUTOMATION
==================================================


FASE 1:


Fundamentos QA


↓

FASE 2:


Python


↓

FASE 3:


Playwright


↓

FASE 4:


Pytest


↓

FASE 5:


API Testing


↓

FASE 6:


Docker


↓

FASE 7:


CI/CD


↓

FASE 8:


Portfólio



==================================================
22. CHECKLIST PROFISSIONAL
==================================================


Antes de buscar vaga:


☐ Sei Python


☐ Sei Playwright


☐ Sei criar testes


☐ Sei usar POM


☐ Sei testar API


☐ Sei usar Git


☐ Sei Docker básico


☐ Sei CI/CD


☐ Tenho projeto GitHub


☐ Tenho README



==================================================
23. NÍVEL ALCANÇADO APÓS O CURSO
==================================================


Após completar todas as partes:


Você consegue atuar como:


QA Automation Júnior



Com evolução para:


QA Automation Pleno



==================================================
24. CONCLUSÃO FINAL
==================================================


A trilha completa passou por:


Parte 1:

Fundamentos


Parte 2:

Configuração


Parte 3:

Playwright básico


Parte 4:

Pytest


Parte 5:

POM


Parte 6:

Projeto real


Parte 7:

CI/CD


Parte 8:

Relatórios


Parte 9:

Testes avançados


Parte 10:

Framework profissional


Parte 11:

API Testing


Parte 12:

UI Avançado


Parte 13:

Boas práticas


Parte 14:

Docker


Parte 15:

Projeto final


Parte 16:

IA aplicada ao QA


Parte 17:

Mercado de trabalho



==================================================
FIM DO CURSO PLAYWRIGHT + PYTHON + PYTEST
==================================================


Resultado:


✅ Framework profissional criado

✅ Projeto para GitHub

✅ Conhecimento de QA Automation

✅ Preparação para entrevistas

✅ Base para carreira em Automação de Testes
  
