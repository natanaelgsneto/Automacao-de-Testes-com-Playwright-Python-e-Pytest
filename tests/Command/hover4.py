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
    page.pause()
    # para rodar no cmd:
    # uv    run    pytest    tests / Command / hover4.py - -headed
    # Faça    estas    verificações:    1.    Verifique    a    configuração    do    PyCharm

    # Vá    em:    Run → Edit    Configurations...

    # Na    configuração    do    pytest, veja    se    em    Additional    pytest  options  existe:  --headed
    # Se    não    existir, adicione    e    clique    em    Apply    e    OK.

    # 2.    Execute    pelo    terminal    na    pasta    do    projeto    Abra  um  terminal  na  pasta  do   projeto  e   execute:  cd "C:\Users\NatanaelNote\PycharmProjects\Automacao-de-Testes-com-Playwright-Python-e-Pytest"  uv  run  pytest  tests / Command / hover4.py - -headed - s