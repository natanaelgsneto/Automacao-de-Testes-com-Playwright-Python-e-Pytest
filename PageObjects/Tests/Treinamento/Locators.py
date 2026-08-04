from playwright.sync_api import Page, expect


def test_hover(page: Page):
    # 1. Navega aguardando o carregamento do DOM
    page.goto('https://automationexercise.com', wait_until='domcontentloaded')

    # 2. Localiza o produto e faz o hover
    product = page.locator('.single-products:visible').filter(has_text='Madame Top For Women')
    product.hover()

    # 3. Clica no botão "Add to cart" do overlay
    product.locator('.product-overlay a:has-text("Add to cart")').click()

    # 4. Localiza o modal do carrinho
    modal = page.locator('#cartModal')
    expect(modal).to_be_visible()

    # 5. Localiza e clica no botão "Continue Shopping"
    btn_continue = modal.locator('button:has-text("Continue Shopping")')
    expect(btn_continue).to_be_visible()
    btn_continue.click()

    # 6. Valida que o modal foi fechado
    expect(modal).not_to_be_visible()