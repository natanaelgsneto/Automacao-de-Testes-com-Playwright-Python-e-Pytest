from Page.base_page import BasePage


class Produtos(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.card_produto = page.locator('.single-products')
        self.botao_adicionar_carrinho = page.locator('.overlay-content:visible .btn')
        self.botao_continuar_comprando = page.get_by_role("button", name="Continue Shopping")

        # Mapeia o link "Cart" no menu superior da página
        self.botao_carrinho = page.get_by_role("link", name="Cart")

    def acessar_produtos(self):
        self.page.goto("https://automationexercise.com/products", wait_until="domcontentloaded")

    def adicionar_produto_ao_carrinho(self, indice_produto: int):
        self.card_produto.nth(indice_produto).hover()
        self.botao_adicionar_carrinho.nth(indice_produto).click()