from playwright.sync_api import Page, expect


class Carrinho:

    def __init__(self, page: Page):

        self.page = page

        self.botao_carrinho = page.locator(
            'a[href="/view_cart"]'
        ).first

        self.botao_excluir = page.locator(
            ".cart_quantity_delete"
        )

    def acessar_carrinho(self):

        self.botao_carrinho.wait_for(
            state="visible",
            timeout=10000
        )

        self.botao_carrinho.click(
            force=True
        )

        self.page.wait_for_url(
            "**/view_cart",
            timeout=10000
        )

        print(">>> Carrinho aberto")

    def excluir_produto(self):

        botao = self.botao_excluir.first

        expect(
            botao
        ).to_be_visible(
            timeout=10000
        )

        botao.click(
            force=True
        )

        self.page.wait_for_timeout(
            1000
        )

        print(">>> Produto excluído")