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
    # para rodar no cmd:
    # uv    run    pytest    tests / Command / hover5.py - -headed
    # Faça    estas    verificações:    1.    Verifique    a    configuração    do    PyCharm

    # Vá    em:    Run → Edit    Configurations...

    # Na    configuração    do    pytest, veja    se    em    Additional    pytest  options  existe:  --headed
    # Se    não    existir, adicione    e    clique    em    Apply    e    OK.

    # 2.    Execute    pelo    terminal    na    pasta    do    projeto    Abra  um  terminal  na  pasta  do   projeto  e   execute:  cd "C:\Users\NatanaelNote\PycharmProjects\Automacao-de-Testes-com-Playwright-Python-e-Pytest"  uv  run  pytest  tests / Command / hover5.py - -headed - s