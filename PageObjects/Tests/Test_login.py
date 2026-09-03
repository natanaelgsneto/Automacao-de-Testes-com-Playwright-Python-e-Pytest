from Page.Cadastro_login import Cadastro_login

def test_login_valido(page):
    login = Cadastro_login(page)
    login.acessarLogin()
    login.fazerLogin(email="ngsneto@gmail.com", senha="123")

    # Força a abertura do navegador e pausa o teste aqui!
    page.pause()