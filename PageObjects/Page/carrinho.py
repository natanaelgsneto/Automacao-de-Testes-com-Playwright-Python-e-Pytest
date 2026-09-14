from playwright.sync_api import Page, expect


class Carrinho:
    def __init__(self, page: Page):
        self.page = page

    def validar_carrinho(
        self,
        indice_produto: str,
        cabecalho_descricao_produto: str,
        descricao_produto: str,
        preco_produto: str,
        preco_total_produto: str
    ):
        produto = self.page.locator(
            "#cart_info_table tbody tr"
        ).nth(int(indice_produto))

        expect(produto).to_be_visible()

        expect(produto).to_contain_text(
            cabecalho_descricao_produto
        )

        expect(produto).to_contain_text(
            descricao_produto
        )

        expect(produto).to_contain_text(
            preco_produto
        )

        expect(produto).to_contain_text(
            preco_total_produto
        )