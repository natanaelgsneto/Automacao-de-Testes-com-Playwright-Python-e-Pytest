from Page.Carrinho.Produto import Produtos
from Page.Carrinho.Carrinho import Carrinho


def test_adicionar_produtos_ao_carrinho(page):
    produtos = Produtos(page)

    produtos.acessar_produtos()

    precoprodutos = produtos.card_produto.nth(1).locator('.productinfo h2').inner_text().replace('Rs.', '')

    print(precoprodutos)

    page.pause()

    #para rodar
    #python -m pytest Page/Carrinho/test_adicionar_produtos_ao_carrinho_em_500.py::test_adicionar_produtos_ao_carrinho -v
