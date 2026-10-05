import pytest

from Page.produtos import Produtos
from Page.detalhes_produto import DetalhesProduto


# 1. A página lista os produtos
def test_listar_todos_os_produtos(page):
    produtos = Produtos(page)

    produtos.acessar_produtos()

    produtos.validar_lista_de_produtos()


# 2. A busca mostra o produto esperado entre os resultados
@pytest.mark.parametrize(
    "termo, produto_esperado",
    [
        pytest.param("Top", "Blue Top", id="busca-top"),
        pytest.param("Jeans", "Grunt Blue Slim Fit Jeans", id="busca-jeans"),
    ],
)
def test_buscar_produto(page, termo, produto_esperado):
    produtos = Produtos(page)

    produtos.acessar_produtos()
    produtos.buscar_produto(termo)

    produtos.validar_resultado_da_busca(termo, produto_esperado)


# 3. Busca por um termo que não existe não traz nenhum produto
def test_buscar_produto_inexistente(page):
    produtos = Produtos(page)

    produtos.acessar_produtos()
    produtos.buscar_produto("produtoinexistentexyz")

    produtos.validar_busca_sem_resultados()


# 4. "View Product" abre a página de detalhes com os dados do produto
def test_ver_detalhes_do_produto(page):
    produtos = Produtos(page)
    detalhes = DetalhesProduto(page)

    produtos.acessar_produtos()
    produtos.ver_produto("Blue Top")

    detalhes.validar_detalhes_do_produto(
        id_produto=1,
        nome="Blue Top",
        categoria="Women > Tops",
        preco="Rs. 500",
        disponibilidade="In Stock",
        condicao="New",
        marca="Polo"
    )
