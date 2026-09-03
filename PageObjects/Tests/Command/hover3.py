from playwright.sync_api import Page


def test_hover(page: Page):
    # 1. Carrega o site sem travar no tempo de limite (Timeout)
    page.goto('https://automationexercise.com', wait_until='domcontentloaded')

    # 2. Inspetor para depuração
    page.pause()

    # 3. Localiza o card do produto especifico
    product = page.locator('.single-products:visible').filter(has_text='Madame Top For Women')

    # 4. Faz o hover para revelar o overlay
    product.hover()

    # 5. Clica no botão "Add to cart" diretamente dentro do overlay desse produto
    product.locator('.product-overlay a:has-text("Add to cart")').click()