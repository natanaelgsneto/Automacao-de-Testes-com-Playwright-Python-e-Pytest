from playwright.sync_api import Page


def test_hover(page: Page):
    page.goto('https://automationexercise.com', wait_until='domcontentloaded')

    page.pause()

    product_card = page.locator('.single-products:visible').filter(has_text='Madame Top For Women')
    product_card.hover()

    # Clica especificamente no botão do overlay (o segundo botão com o texto)
    product_card.locator('.product-overlay a:has-text("Add to cart")').click()
