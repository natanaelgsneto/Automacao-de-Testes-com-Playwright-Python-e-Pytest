from Page.Cadastro_login import CadastroLogin
from Page.produtos import Produtos
from Page.carrinho import Carrinho
from playwright.sync_api import expect


def test_login(page, credenciais_login):
    email, senha = credenciais_login
    login = CadastroLogin(page)

    login.acessar_cadastro_login()
    login.fazerLogin(
        email=email,
        senha=senha
    )

    expect(
        page.get_by_role("link", name="Logout")
    ).to_be_visible()


def test_adicionar_e_validar_carrinho(page):
    produtos = Produtos(page)
    carrinho = Carrinho(page)

    produtos.acessar_produtos()

    # Continue aqui com os passos do carrinho...