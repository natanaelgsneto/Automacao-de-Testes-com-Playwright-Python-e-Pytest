from playwright.sync_api import Page, expect


class Produtos:

    def __init__(self, page: Page):

        self.page = page

        self.botao_produtos = page.locator(
            'a[href="/products"]'
        )

        self.produtos = page.locator(
            ".features_items .product-image-wrapper"
        )

        self.botao_continuar_comprando = page.locator(
            "#cartModal button.close-modal"
        )

    def acessar_produtos(self):

        self.botao_produtos.first.wait_for(
            state="visible",
            timeout=10000
        )

        self.botao_produtos.first.click(
            force=True
        )

        self.page.wait_for_url(
            "**/products",
            timeout=10000
        )

        print(">>> Página Produtos aberta")

    def adicionar_produto_ao_carrinho(self, indice_produto=0):
        produto = self.produtos.nth(indice_produto)

        produto.scroll_into_view_if_needed()

        produto.hover()

        botao_adicionar = produto.locator(
            ".add-to-cart"
        ).first

        expect(
            botao_adicionar
        ).to_be_visible(
            timeout=10000
        )

        botao_adicionar.click()

        print(">>> Add to cart clicado")

        # ==============================
        # Modal
        # ==============================

        modal = self.page.locator(
            "#cartModal"
        )

        expect(
            modal
        ).to_be_visible(
            timeout=10000
        )

        print(">>> Modal do carrinho aberto")

        # ==============================
        # Confirmar produto adicionado
        # ==============================

        expect(
            modal
        ).to_contain_text(
            "Added!"
        )

        print(">>> Produto confirmado no modal")

        # ==============================
        # Continue Shopping
        # ==============================

        botao_continuar = modal.locator(
            "button.close-modal"
        )

        botao_continuar.click(
            force=True
        )

        print(">>> Continue Shopping clicado")

        expect(
            modal
        ).not_to_be_visible(
            timeout=10000
        )

        print(">>> Modal fechado")