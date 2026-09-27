from Page.Cadastro_login import CadastroLogin
def test_login_valido(page):
    login = CadastroLogin(page)
    login.fazerLogin(email="ngsneto@gmail.com", senha="123")

    # Força a abertura do navegador e pausa o teste aqui!
    page.pause()