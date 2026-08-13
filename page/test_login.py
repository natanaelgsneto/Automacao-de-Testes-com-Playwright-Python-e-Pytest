from playwright.sync_api import Page, expect
from page.Cadastro_login import CadastroLogin

def test_usuario_nao_logado(page: Page):
    login = CadastroLogin(page)
    login.acessar_home()
    # Correção: use not_to_be_visible() (sem underscore depois do not)
    expect(page.get_by_role("link", name="Logout")).not_to_be_visible()
    page.pause()

def test_login_valido(page: Page):
    login = CadastroLogin(page)
    login.acessar_home()
    login.acessar_cadastro_login()
    login.fazer_login(email='test@testecab.com', senha='123')