from page.BasePage import BasePage


class CadastroLogin(BasePage):

    def __init__(self, page):
        super().__init__(page)
        # Altere esta linha para usar o seletor baseado no data-qa oficial do site:
        self.input_email_login = page.locator("[data-qa='login-email']")

        self.input_senha_login = page.get_by_role("textbox", name="Password")
        self.botao_login = page.get_by_role("button", name="Login")
        self.input_nome_cadastro = page.get_by_role("textbox", name="Name")
        self.input_email_cadastro = page.locator("form").filter(
            has_text="Signup").get_by_placeholder("Email Address")
        self.botao_inscrever = page.get_by_role("button", name="Signup")

    def fazer_login(self, email='', senha=''):
        self.input_email_login.fill(email)
        self.input_senha_login.fill(senha)
        self.botao_login.click()

    def realizar_cadastro(self, nome='', email=''):
        self.input_nome_cadastro.fill(nome)
        self.input_email_cadastro.fill(email)
        self.botao_inscrever.click()