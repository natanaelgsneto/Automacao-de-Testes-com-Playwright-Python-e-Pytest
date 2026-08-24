from playwright.sync_api import Page, expect

from Page.Carrinho.Produtos import Produtos
from Page.Carrinho.Carrinho import Carrinho


def bloquear_propagandas(page: Page):
    """
    Remove elementos de propaganda que podem ficar
    sobre os elementos da página.
    """

    page.add_style_tag(content="""
        iframe[id^="aswift_"],
        iframe[title="Advertisement"],
        ins.adsbygoogle,
        .adsbygoogle,
        .google-auto-placed,
        .adsbygoogle-noablate {
            display: none !important;
            visibility: hidden !important;
            pointer-events: none !important;
        }
    """)

    page.evaluate("""
        () => {
            document
                .querySelectorAll(
                    'iframe[id^="aswift_"], ' +
                    'iframe[title="Advertisement"], ' +
                    'ins.adsbygoogle, ' +
                    '.adsbygoogle, ' +
                    '.google-auto-placed, ' +
                    '.adsbygoogle-noablate'
                )
                .forEach(element => element.remove());
        }
    """)


def test_adicionar_e_excluir_produto(page: Page):

    # ==========================================
    # 1 - Abrir o site
    # ==========================================

    page.goto(
        "https://automationexercise.com",
        wait_until="domcontentloaded"
    )

    print("\n>>> Site aberto")

    # ==========================================
    # 2 - Bloquear propagandas
    # ==========================================

    bloquear_propagandas(page)

    print(">>> Propagandas bloqueadas")

    # ==========================================
    # 3 - Criar objeto Produtos
    # ==========================================

    produtos = Produtos(page)

    # ==========================================
    # 4 - Acessar página Produtos
    # ==========================================

    produtos.acessar_produtos()

    print(">>> Página Produtos aberta")

    # ==========================================
    # 5 - Adicionar produto ao carrinho
    # ==========================================

    produtos.adicionar_produto_ao_carrinho(
        indice_produto=1
    )

    print(">>> Produto adicionado ao carrinho")

    # ==========================================
    # 6 - Criar objeto Carrinho
    # ==========================================

    carrinho = Carrinho(page)

    # ==========================================
    # 7 - Acessar Carrinho
    # ==========================================

    print(">>> Antes de acessar o Carrinho")

    carrinho.acessar_carrinho()

    print(">>> Carrinho aberto")

    # ==========================================
    # 8 - Validar URL do Carrinho
    # ==========================================

    expect(page).to_have_url(
        "https://automationexercise.com/view_cart"
    )

    print(">>> URL do Carrinho confirmada")

    # ==========================================
    # 9 - Localizar produto no Carrinho
    # ==========================================

    produto_no_carrinho = page.locator(
        ".cart_quantity_delete"
    )

    # ==========================================
    # 10 - Validar produto no Carrinho
    # ==========================================

    expect(
        produto_no_carrinho.first
    ).to_be_visible(
        timeout=10000
    )

    print(">>> Produto encontrado no carrinho")

    # ==========================================
    # 11 - Excluir produto
    # ==========================================

    carrinho.excluir_produto()

    print(">>> Produto excluído")

    # ==========================================
    # 12 - Validar Carrinho vazio
    # ==========================================

    expect(
        produto_no_carrinho
    ).to_have_count(0)

    print(">>> Carrinho vazio")

    # ==========================================
    # 13 - Mensagem de carrinho vazio
    # ==========================================

    expect(
        page.get_by_text(
            "Cart is empty!"
        )
    ).to_be_visible(
        timeout=10000
    )

    print(">>> Mensagem 'Cart is empty!' encontrada")

    print("\n>>> TESTE FINALIZADO COM SUCESSO")