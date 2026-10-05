from Page.Cadastro_login import CadastroLogin


def test_login(page, credenciais_login):
    email, senha = credenciais_login

    # 1. Abre a página de login
    page.goto("https://automationexercise.com/login")

    # 2. Cria o objeto da página de login
    login = CadastroLogin(page)

    # 3. Preenche os dados e tenta entrar
    login.fazerLogin(
        email=email,
        senha=senha
    )

    # 4. Mantém a página aberta por 5 segundos
    page.wait_for_timeout(5000)