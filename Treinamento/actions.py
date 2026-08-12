class BasePage:
    def __init__(self, page):
        self.page = page
        self.botao_home = page.get_by_role("link", name="Home")
        self.botao_produtos = page.get_by_role("link", name="Products")
        self.botao_carrinho = page.get_by_role("link", name="Cart")
        self.botao_cadastro_login = page.get_by_role("link", name="Signup / Login")

     def acessarhome(self):
        self.goto("https://automationexercise.com/")
     def acessarcarrinho(self):
        self.botao_carrinho.click()