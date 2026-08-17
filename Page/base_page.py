from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.botao_cadastro_login = page.get_by_role("link", name="Signup / Login")

    def acessar_home(self):
        self.page.goto("https://automationexercise.com")