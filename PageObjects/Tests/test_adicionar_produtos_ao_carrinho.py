from PageObjects.Page.produtos import Produtos
from PageObjects.Page.carrinho import Carrinho


def test_adicionar_produtos_ao_carrinho(page):
    produtos = Produtos(page)
    carrinho = Carrinho(page)

    # Abre a página de produtos
    produtos.acessar_produtos()

    # Adiciona o primeiro produto
    produtos.adicionar_produto_ao_carrinho(
        indice_produto="0"
    )
    produtos.botao_continuar_comprando.click()

    # Adiciona o segundo produto
    produtos.adicionar_produto_ao_carrinho(
        indice_produto="1"
    )
    produtos.botao_continuar_comprando.click()

    # Abre o carrinho diretamente
    page.goto("/view_cart")

    # Valida o primeiro produto
    carrinho.validar_carrinho(
        indice_produto="0",
        cabecalho_descricao_produto="Blue Top",
        descricao_produto="Women > Tops",
        preco_produto="Rs. 500",
        preco_total_produto="Rs. 500"
    )

    # Valida o segundo produto
    carrinho.validar_carrinho(
        indice_produto="1",
        cabecalho_descricao_produto="Men Tshirt",
        descricao_produto="Men > Tshirts",
        preco_produto="Rs. 400",
        preco_total_produto="Rs. 400"
    )

    #para rodar python -m pytest "PageObjects\Tests\test_adicionar_produtos_ao_carrinho.py" --headed --slowmo=1000 -v -s
    #PARA abrir o trace.zip acesse  trace.playwright.dev. e faça o upload  do arquivo trace.zip