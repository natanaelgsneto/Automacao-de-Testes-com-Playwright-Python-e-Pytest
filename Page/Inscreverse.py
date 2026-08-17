from playwright.sync_api import Page
from Page.Cadastro_login import CadastroLogin


class Inscreverse(CadastroLogin):
    def __init__(self, page: Page):
        super().__init__(page)

        # Formulario de conta
        self.checkbox_mr = page.get_by_role("radio", name="Mr.")
        self.checkbox_mrs = page.get_by_role("radio", name="Mrs.")
        self.input_nome = page.get_by_role("textbox", name="Name *", exact=True)
        self.input_senha = page.get_by_role("textbox", name="Password *")
        self.select_dia = page.locator("#days")
        self.select_mes = page.locator("#months")
        self.select_ano = page.locator("#years")
        self.checkbox_newsletter = page.get_by_text("Sign up for our newsletter!")
        self.checkbox_offers = page.get_by_text("Receive special offers from our partners!")

        # Formulario de endereco
        self.input_primeiro_nome = page.get_by_role("textbox", name="First name *")
        self.input_sobrenome = page.get_by_role("textbox", name="Last name *")
        self.input_empresa = page.get_by_role("textbox", name="Company", exact=True)
        self.input_endereco = page.locator("#address1")
        self.select_pais = page.get_by_label("Country *")
        self.input_estado = page.get_by_role("textbox", name="State *")
        self.input_cidade = page.locator("#city")
        self.input_zipcode = page.locator("#zipcode")
        self.input_numero_telefone = page.get_by_role("textbox", name="Mobile Number *")

        # Botoes
        self.botao_criar_conta = page.get_by_role("button", name="Create Account")
        self.botao_continuar = page.get_by_role("link", name="Continue")
        self.botao_deletar_conta = page.get_by_role("link", name="Delete Account")

    def preencher_informacoes_da_conta(self, titulo='', senha='', data_aniversario='',
                                       receive_special_offers_from=False, sign_up_for_our_newsletter=False):
        if titulo == 'Mr':
            self.checkbox_mr.check()
        elif titulo == 'Mrs':
            self.checkbox_mrs.check()

        if senha:
            self.input_senha.fill(senha)

        if data_aniversario:
            dia, mes, ano = data_aniversario.split('/')
            self.select_dia.select_option(dia.lstrip('0'))
            self.select_mes.select_option(mes.lstrip('0'))
            self.select_ano.select_option(ano)

        if sign_up_for_our_newsletter:
            self.checkbox_newsletter.check()

        if receive_special_offers_from:
            self.checkbox_offers.check()

    def preencher_informacoes_endereco(self, primeiro_nome='', sobrenome='', empresa='', endereco='', pais='',
                                       estado='', cidade='', zipcode='', numero_telefone=''):
        if primeiro_nome: self.input_primeiro_nome.fill(primeiro_nome)
        if sobrenome: self.input_sobrenome.fill(sobrenome)
        if empresa: self.input_empresa.fill(empresa)
        if endereco: self.input_endereco.fill(endereco)
        if pais: self.select_pais.select_option(pais)
        if estado: self.input_estado.fill(estado)
        if cidade: self.input_cidade.fill(cidade)
        if zipcode: self.input_zipcode.fill(zipcode)
        if numero_telefone: self.input_numero_telefone.fill(numero_telefone)