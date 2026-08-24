from playwright.sync_api import Page, expect

from Page.Carrinho.Produtos import Produtos
from Page.Carrinho.Carrinho import Carrinho


def bloquear_propagandas(page: Page):

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
    # 4 - Acessar Produtos
    # ==========================================

    produtos.acessar_produtos()

    print(">>> Página Produtos aberta")

    # ==========================================
    # 5 - ADICIONAR PRODUTO
    # ==========================================

    produtos.adicionar_produto_ao_carrinho(
        indice_produto=0
    )

    print(">>> PRODUTO ADICIONADO AO CARRINHO")

    # ==========================================
    # 6 - Criar objeto Carrinho
    # ==========================================

    carrinho = Carrinho(page)

    # ==========================================
    # 7 - Acessar Carrinho
    # ==========================================

    carrinho.acessar_carrinho()

    print(">>> Carrinho aberto")

    # ==========================================
    # 8 - Validar URL
    # ==========================================

    expect(page).to_have_url(
        "https://automationexercise.com/view_cart"
    )

    print(">>> URL do Carrinho confirmada")

    # ==========================================
    # 9 - Validar que o produto foi ADICIONADO
    # ==========================================

    produto_no_carrinho = page.locator(
        ".cart_quantity_delete"
    )

    expect(
        produto_no_carrinho.first
    ).to_be_visible(
        timeout=10000
    )

    print(">>> PRODUTO CONFIRMADO NO CARRINHO")

    # ==========================================
    # 10 - EXCLUIR PRODUTO
    # ==========================================

    carrinho.excluir_produto()

    print(">>> PRODUTO EXCLUÍDO DO CARRINHO")

    # ==========================================
    # 11 - Validar que o produto foi EXCLUÍDO
    # ==========================================

    expect(
        produto_no_carrinho
    ).to_have_count(0)

    print(">>> PRODUTO NÃO EXISTE MAIS NO CARRINHO")

    # ==========================================
    # 12 - Validar carrinho vazio
    # ==========================================

    expect(
        page.get_by_text(
            "Cart is empty!"
        )
    ).to_be_visible(
        timeout=10000
    )

    print(">>> CARRINHO VAZIO")

    # ==========================================
    # FINAL
    # ==========================================

    print("\n==========================================")
    print(">>> TESTE ADICIONAR E EXCLUIR PASSOU")
    print("==========================================")