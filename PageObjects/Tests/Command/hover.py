from playwright.sync_api import Page


def test_hover(page: Page):
    # 1. Navega aguardando a estrutura base do DOM (evita timeout com anúncios/analytics)
    page.goto('https://automationexercise.com', wait_until='domcontentloaded')

    # 2. Pausa a execução para abrir o Playwright Inspector
    page.pause()

    # 3. Localiza e interage com o elemento após retomar no Inspector
    product_card = page.locator('.single-products:visible').filter(has_text='Madame Top For Women')
    product_card.hover()
    product_card.locator('a:has-text("Add to cart")').first.click()