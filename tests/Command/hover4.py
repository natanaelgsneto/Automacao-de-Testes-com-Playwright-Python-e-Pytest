from playwright.sync_api import Page, expect


def test_hover(page: Page):
    # 1. Navega evitando o erro de timeout
    page.goto('https://automationexercise.com', wait_until='domcontentloaded')

    # 2. Localiza o produto e faz o hover
    product = page.locator('.single-products:visible').filter(has_text='Madame Top For Women')
    product.hover()

    # 3. Clica no botão "Add to cart" do overlay
    product.locator('.product-overlay a:has-text("Add to cart")').click()

    # --- VERIFICAÇÕES DO MODAL ---

    # Garante que o modal de confirmação está visível
    modal = page.locator('#cartModal')
    expect(modal).to_be_visible()

    # Valida o texto do título do modal ("Added!")
    expect(modal.locator('.modal-title')).to_have_text('Added!')

    # Valida o texto da mensagem no corpo do modal
    expect(modal.locator('.modal-body p').first).to_have_text('Your product has been added to cart.')

    # Valida se o botão "Continue Shopping" está visível
    btn_continue = modal.locator('button:has-text("Continue Shopping")')
    expect(btn_continue).to_be_visible()

    # Valida se o link "View Cart" está visível
    link_view_cart = modal.locator('a:has-text("View Cart")')
    expect(link_view_cart).to_be_visible()

    # (Opcional) Clica em Continue Shopping para fechar o modal
    btn_continue.click()