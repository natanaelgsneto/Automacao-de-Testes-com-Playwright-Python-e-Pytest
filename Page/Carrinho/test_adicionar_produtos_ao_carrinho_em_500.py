from Page.Carrinho.Produto import Produtos


def test_adicionar_produtos_ao_carrinho(page):
    produtos = Produtos(page)

    produtos.acessar_produtos()

    precoprodutos = (
        produtos.card_produto
        .nth(1)
        .locator('.productinfo h2')
        .inner_text()
        .replace('Rs.', '')
    )

    precoprodutos = int(precoprodutos.strip())

    print(precoprodutos)
    print(type(precoprodutos))

    page.pause()

    if precoprodutos <= 500:
        print("Produto custa até 500")
    else:
        print("Produto custa mais de 500")