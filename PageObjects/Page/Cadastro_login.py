import re

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

        # Mensagem exibida quando o site recusa o email ou a senha
        self.mensagemErroLogin = self.page.get_by_text("Your email or password is incorrect!")

    def fazerLogin(self, email="", senha=""):
        self.inputEmail.fill(email)
        self.password.fill(senha)
        self.botaologin.click()

    def validarLoginComSucesso(self):
        # Espera o resultado do login: usuário logado ou mensagem de erro
        expect(self.textoLogadoComo.or_(self.mensagemErroLogin)).to_be_visible()

        assert not self.mensagemErroLogin.is_visible(), (
            "O site recusou o login: 'Your email or password is incorrect!'. "
            "Confira LOGIN_EMAIL e LOGIN_SENHA."
        )

        expect(self.textoLogadoComo).to_be_visible()
        expect(self.linkLogout).to_be_visible()

    def validarLoginRecusado(self):
        # O formulário foi enviado e o site recusou email ou senha
        expect(self.mensagemErroLogin).to_be_visible()
        expect(self.linkLogout).to_be_hidden()

    def validarCampoBloqueadoPeloNavegador(self, campo, motivo):
        # Os campos são type="email" e required: o navegador impede o envio
        # do formulário. "motivo" é a propriedade de ValidityState
        # (valueMissing, typeMismatch), que não depende do idioma do navegador.
        input_campo = {"email": self.inputEmail, "senha": self.password}[campo]

        assert input_campo.evaluate("(el, motivo) => el.validity[motivo]", motivo), (
            f"Campo {campo}: esperado validity.{motivo}, mas o navegador informou "
            f"'{input_campo.evaluate('el => el.validationMessage')}'"
        )

        # Como o formulário não foi enviado, o site não responde nada
        expect(self.page).to_have_url(re.compile(r"/login$"))
        expect(self.mensagemErroLogin).to_be_hidden()
        expect(self.linkLogout).to_be_hidden()
