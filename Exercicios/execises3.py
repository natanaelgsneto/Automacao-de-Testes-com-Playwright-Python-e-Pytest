from playwright.sync_api import Page, expect


def test_cart(page: Page) -> None:
    """Adiciona o Blue Top duas vezes ao carrinho e valida a tabela do carrinho."""

    # 1. Abre a home (base_url vem do contexto no conftest.py)
    page.goto("/")

    # 2. Acessa a página de produtos
    page.get_by_role("link", name="Products").click()
    expect(page.get_by_role("heading", name="All Products")).to_be_visible()

    # 3. Localiza o card do produto "Blue Top"
    # Obs: o "Add to cart" é um <a> sem href, então NÃO tem role "link".
    # Por isso usamos o seletor CSS da classe. O .first pega o botão visível
    # do card (o segundo fica no overlay que só aparece no hover).
    blue_top = page.locator(".product-image-wrapper").filter(has_text="Blue Top").first
    add_to_cart = blue_top.locator("a.add-to-cart").first
    modal = page.locator("#cartModal")

    # 4. Adiciona o produto ao carrinho duas vezes
    for _ in range(2):
        add_to_cart.click()
        expect(modal).to_be_visible()
        expect(modal.get_by_text("Your product has been added to cart.")).to_be_visible()
        modal.get_by_role("button", name="Continue Shopping").click()
        expect(modal).to_be_hidden()

    # 5. Abre o carrinho
    page.locator('a[href="/view_cart"]').first.click()

    # 6. Valida o cabeçalho da tabela
    cabecalho = page.locator("#cart_info_table .cart_menu")
    for coluna in ["Item", "Description", "Price", "Quantity", "Total"]:
        expect(cabecalho).to_contain_text(coluna)

    # 7. Valida a linha do produto (Blue Top = product-id 1)
    linha = page.locator("#product-1")
    expect(linha.locator(".cart_description a")).to_have_text("Blue Top")
    expect(linha.locator(".cart_price p")).to_have_text("Rs. 500")
    expect(linha.locator(".cart_quantity button")).to_have_text("2")
    expect(linha.locator(".cart_total_price")).to_have_text("Rs. 1000")

    # para rodar: uv run pytest Exercicios/execises3.py -v -s --headed
