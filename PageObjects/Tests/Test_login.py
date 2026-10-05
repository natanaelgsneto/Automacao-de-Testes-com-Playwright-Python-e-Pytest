from Page.Cadastro_login import CadastroLogin
def test_login_valido(page, credenciais_login):
    email, senha = credenciais_login
    login = CadastroLogin(page)
    login.fazerLogin(email=email, senha=senha)

    # Força a abertura do navegador e pausa o teste aqui!
    page.pause()