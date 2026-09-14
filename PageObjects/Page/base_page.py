from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def acessar_home(self):
        self.page.goto("/")

    def acessar_produtos(self):
        self.page.goto("/products")

    def acessar_carrinho(self):
        self.page.goto("/view_cart")

    def acessar_cadastro_login(self):
        self.page.goto("/login")