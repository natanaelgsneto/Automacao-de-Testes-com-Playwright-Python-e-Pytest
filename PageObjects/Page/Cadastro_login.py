from playwright.sync_api import expect

from Page.base_page import BasePage

class CadastroLogin(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.inputEmail = self.page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address")
        self.password = self.page.get_by_role("textbox", name="Password")
        self.botaologin = self.page.get_by_role("button", name="Login")

        # Elementos exibidos no menu após o login
        self.textoLogadoComo = self.page.get_by_text("Logged in as")
        self.linkLogout = self.page.get_by_role("link", name="Logout")

    def fazerLogin(self, email="", senha=""):
        self.inputEmail.fill(email)
        self.password.fill(senha)
        self.botaologin.click()

    def validarLoginComSucesso(self):
        expect(self.textoLogadoComo).to_be_visible()
        expect(self.linkLogout).to_be_visible()
