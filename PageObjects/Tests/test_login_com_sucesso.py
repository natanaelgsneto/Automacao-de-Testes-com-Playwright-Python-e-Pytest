from Page.Cadastro_login import CadastroLogin


def test_login_com_sucesso(page, credenciais_login):
    email, senha = credenciais_login
    login = CadastroLogin(page)

    # Abre a página de login
    login.acessar_cadastro_login()

    # Preenche email e senha (de LOGIN_EMAIL e LOGIN_SENHA) e clica em Login
    login.fazerLogin(
        email=email,
        senha=senha
    )

    # Valida que o usuário está logado ("Logged in as" e "Logout" no menu)
    login.validarLoginComSucesso()
