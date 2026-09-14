from playwright.sync_api import Page


class Produtos:
    def __init__(self, page: Page):
        self.page = page

        self.botao_continuar_comprando = page.get_by_role(
            "button",
            name="Continue Shopping"
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
        produto.get_by_text("Add to cart").first.click()