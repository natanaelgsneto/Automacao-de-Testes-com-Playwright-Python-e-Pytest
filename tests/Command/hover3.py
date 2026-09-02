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
    # para rodar no cmd:
    # uv    run    pytest    tests / Command / hover3.py - -headed
    # Faça    estas    verificações:    1.    Verifique    a    configuração    do    PyCharm

    # Vá    em:    Run → Edit    Configurations...

    # Na    configuração    do    pytest, veja    se    em    Additional    pytest  options  existe:  --headed
    # Se    não    existir, adicione    e    clique    em    Apply    e    OK.

    # 2.    Execute    pelo    terminal    na    pasta    do    projeto    Abra  um  terminal  na  pasta  do   projeto  e   execute:  cd "C:\Users\NatanaelNote\PycharmProjects\Automacao-de-Testes-com-Playwright-Python-e-Pytest"  uv  run  pytest  tests / Command / hover3.py - -headed - s