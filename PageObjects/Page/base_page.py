class base_page:

    def __init__(self, page):
        self.page = page
        self.page.goto("https://automationexercise.com/")

        self.botaohome = page.get_by_role("link", name="Home")
        self.products = page.get_by_role("link", name="Products")
        self.carrinho = page.get_by_role("link", name="Cart")
        self.botaoCadastrar_login = page.get_by_role(
            "link", name=" Signup / Login"
        )

    def home(self):
        self.page.goto("https://automationexercise.com/")

    def acessarCarrinho(self):
        self.carrinho.click()

    def acessarLogin(self):
        self.botaoCadastrar_login.click()