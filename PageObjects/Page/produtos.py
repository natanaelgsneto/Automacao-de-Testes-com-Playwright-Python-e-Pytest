import re

from playwright.sync_api import Page, expect


class Produtos:
    def __init__(self, page: Page):
        self.page = page

        self.botao_continuar_comprando = page.locator(
            "#cartModal .close-modal"
        )

        self.botao_carrinho = page.get_by_role(
            "link",
            name="Cart"
        )

        # Listagem e busca de produtos
        self.titulo_todos_produtos = page.get_by_role("heading", name="All Products")
        self.titulo_produtos_buscados = page.get_by_role("heading", name="Searched Products")
        self.links_ver_produto = page.get_by_role("link", name="View Product")
        self.campo_busca = page.get_by_placeholder("Search Product")

        # O botão de busca é só um ícone, sem nome acessível: o id é o único
        # identificador estável. Apertar Enter no campo não dispara a busca.
        self.botao_buscar = page.locator("#submit_search")

    def acessar_produtos(self):
        self.page.goto("/products")

    def adicionar_produto_ao_carrinho(self, indice_produto: str):
        produto = self.page.locator(".single-products").nth(
            int(indice_produto)
        )

        produto.hover()

        produto.locator(
            ".product-overlay a.add-to-cart"
        ).click(force=True)

        expect(
            self.botao_continuar_comprando
        ).to_be_visible()

    def continuar_comprando(self):
        self.botao_continuar_comprando.click()

    def acessar_carrinho(self):
        self.botao_carrinho.click()

    def buscar_produto(self, termo: str):
        self.campo_busca.fill(termo)
        self.botao_buscar.click()

    def ver_produto(self, nome_produto: str):
        # O card do produto não tem role; filtra o card pelo nome exato
        # e clica no link "View Product" dele
        card = self.page.locator(".product-image-wrapper").filter(
            has=self.page.get_by_text(nome_produto, exact=True)
        )
        card.get_by_role("link", name="View Product").click()

    def validar_lista_de_produtos(self):
        expect(self.titulo_todos_produtos).to_be_visible()
        expect(self.campo_busca).to_be_visible()
        expect(self.links_ver_produto).not_to_have_count(0)

    def validar_resultado_da_busca(self, termo: str, produto_esperado: str):
        expect(self.page).to_have_url(re.compile(rf"/products\?search={re.escape(termo)}$"))
        expect(self.titulo_produtos_buscados).to_be_visible()

        # O nome aparece no card e na camada de hover (oculta); o primeiro é o visível
        expect(self.page.get_by_text(produto_esperado, exact=True).first).to_be_visible()

    def validar_busca_sem_resultados(self):
        # O site não mostra mensagem: só o título e nenhum card de produto
        expect(self.titulo_produtos_buscados).to_be_visible()
        expect(self.links_ver_produto).to_have_count(0)