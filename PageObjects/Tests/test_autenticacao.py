from Page.Cadastro_login import CadastroLogin
from Page.produtos import Produtos
from Page.carrinho import Carrinho
from playwright.sync_api import expect


def test_login(page):
    login = CadastroLogin(page)

    login.acessar_cadastro_login()
    login.fazerLogin(
        email="teste@testeabcde.com",
        senha="123456789"
    )

    expect(
        page.get_by_role("link", name="Logout")
    ).to_be_visible()


def test_adicionar_e_validar_carrinho(page):
    produtos = Produtos(page)
    carrinho = Carrinho(page)

    produtos.acessar_produtos()

    # Continue aqui com os passos do carrinho...