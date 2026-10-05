import re

from playwright.sync_api import expect

from Page.base_page import BasePage


class DetalhesProduto(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.campo_quantidade = self.page.get_by_role("spinbutton")
        self.botao_adicionar_ao_carrinho = self.page.get_by_role("button", name="Add to cart")

    def validar_detalhes_do_produto(
        self,
        id_produto: int,
        nome: str,
        categoria: str,
        preco: str,
        disponibilidade: str,
        condicao: str,
        marca: str
    ):
        expect(self.page).to_have_url(re.compile(rf"/product_details/{id_produto}$"))

        expect(self.page.get_by_role("heading", name=nome)).to_be_visible()
        expect(self.page.get_by_text(f"Category: {categoria}")).to_be_visible()
        expect(self.page.get_by_text(preco, exact=True)).to_be_visible()
        expect(self.page.get_by_text(f"Availability: {disponibilidade}")).to_be_visible()
        expect(self.page.get_by_text(f"Condition: {condicao}")).to_be_visible()
        expect(self.page.get_by_text(f"Brand: {marca}")).to_be_visible()

        expect(self.campo_quantidade).to_have_value("1")
        expect(self.botao_adicionar_ao_carrinho).to_be_visible()
