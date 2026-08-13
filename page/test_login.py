from playwright.sync_api import Page
from page.Treinamento.Cadastro_login import CadastroLogin


def test_login_valido(page: Page):
    login = CadastroLogin(page)
    login.acessar_home()
    login.acessar_cadastro_login()
    login.fazer_login(email='test@testecab.com', senha='123')