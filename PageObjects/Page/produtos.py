from playwright.sync_api import Page, expect


class Produtos:
    def __init__(self, page: Page):
        self.page = page

        self.botao_continuar_comprando = page.locator(
            "#cartModal .close-modal"
        )

        self.botao_carrinho = page.get_by_role(
            "link",
            name="Cart"
        )

    def acessar_produtos(self):
        self.page.goto("/products")

    def adicionar_produto_ao_carrinho(self, indice_produto: str):
        produto = self.page.locator(".single-products").nth(
            int(indice_produto)
        )

        produto.hover()

        produto.locator(
            ".product-overlay a.add-to-cart"
        ).click(force=True)

        expect(
            self.botao_continuar_comprando
        ).to_be_visible()

    def continuar_comprando(self):
        self.botao_continuar_comprando.click()

    def acessar_carrinho(self):
        self.botao_carrinho.click()