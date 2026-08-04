# 🚀 Automação de Testes E2E com Playwright, Python e Pytest

Guia completo para configuração do ambiente, desenvolvimento e execução de automação de testes web utilizando **Python**, **Playwright**, **Pytest** e o gerenciador de pacotes **`uv`**.

---

## 🛠️ Requisitos Prévios (Instalação do Zero)

Antes de começar, certifique-se de ter as seguintes ferramentas instaladas no seu sistema operacional:

### 1. Python
* Faça o download e instale o Python (versão 3.9 ou superior) pelo site oficial: [python.org](https://www.python.org/downloads/).
* ⚠️ **Atenção (Windows):** Na tela de instalação, marque obrigatoriamente a opção **"Add Python to PATH"**.

### 2. Git
* Faça o download do Git em: [git-scm.com](https://git-scm.com/downloads).
* Siga a instalação padrão ("Next, Next, Install").

### 3. Gerenciador `uv` (Fast Package Installer)
O `uv` é um gerenciador de ambientes e pacotes Python de alta performance utilizado neste projeto.
* Para instalar no **Windows (PowerShell)**:
  ```powershell
  powershell -ExecutionPolicy ByPass -c "irm [https://astral.sh/uv/install.ps1](https://astral.sh/uv/install.ps1) | iex"
