from playwright.sync_api import Page, expect


class Carrinho:
    def __init__(self, page: Page):
        self.page = page
        self.itens_carrinho = page.locator("#cart_info_table tbody tr")

    def acessar_carrinho(self):
        self.page.get_by_role("link", name="Cart").click()

        # Confirma que a tabela do carrinho foi exibida
        expect(self.page.locator("#cart_info_table")).to_be_visible()

    def validar_carrinho(
        self,
        indice_produto: str,
        cabecalho_descricao_produto: str,
        descricao_produto: str,
        preco_produto: str,
        preco_total_produto: str
    ):
        # Localiza o produto pelo índice da linha
        produto = self.itens_carrinho.nth(int(indice_produto))

        # Valida o nome do produto
        expect(
            produto.locator(".cart_description h4 a")
        ).to_have_text(cabecalho_descricao_produto)

        # Valida a categoria/descrição do produto
        expect(
            produto.locator(".cart_description p")
        ).to_have_text(descricao_produto)

        # Valida o preço unitário
        expect(
            produto.locator(".cart_price p")
        ).to_have_text(preco_produto)

        # Valida o preço total da linha
        expect(
            produto.locator(".cart_total p")
        ).to_have_text(preco_total_produto)