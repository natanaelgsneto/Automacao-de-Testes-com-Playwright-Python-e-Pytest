from Page.Cadastro_login import CadastroLogin


def test_login_com_sucesso(page):
    login = CadastroLogin(page)

    # Abre a página de login
    login.acessar_cadastro_login()

    # Preenche email e senha e clica em Login
    login.fazerLogin(
        email="teste.pageobjects.2026@teste.com",
        senha="123456"
    )

    # Valida que o usuário está logado ("Logged in as" e "Logout" no menu)
    login.validarLoginComSucesso()
