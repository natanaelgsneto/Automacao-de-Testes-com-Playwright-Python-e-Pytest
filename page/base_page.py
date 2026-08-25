from playwright.sync_api import Page


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def acessar_home(self):
        self.page.goto("https://automationexercise.com/")

    def acessar_produtos(self):
        self.page.goto("https://automationexercise.com/products")

    def acessar_carrinho(self):
        self.page.goto("https://automationexercise.com/view_cart")

    def acessar_login(self):
        self.page.goto("https://automationexercise.com/login")