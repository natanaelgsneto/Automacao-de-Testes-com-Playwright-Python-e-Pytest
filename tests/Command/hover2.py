from playwright.sync_api import Page


def test_hover(page: Page):
    page.goto('https://automationexercise.com', wait_until='domcontentloaded')

    page.pause()

    product_card = page.locator('.single-products:visible').filter(has_text='Madame Top For Women')
    product_card.hover()

    # Clica especificamente no botão do overlay (o segundo botão com o texto)
    product_card.locator('.product-overlay a:has-text("Add to cart")').click()

#para rodar no cmd:
    #uv    run    pytest    tests / Command / hover2.py - -headed
    #Faça    estas    verificações:    1.    Verifique    a    configuração    do    PyCharm

    #Vá    em:    Run → Edit    Configurations...

    #Na    configuração    do    pytest, veja    se    em    Additional    pytest  options  existe:  --headed
    #Se    não    existir, adicione    e    clique    em    Apply    e    OK.

    #2.    Execute    pelo    terminal    na    pasta    do    projeto    Abra  um  terminal  na  pasta  do   projeto  e   execute:  cd "C:\Users\NatanaelNote\PycharmProjects\Automacao-de-Testes-com-Playwright-Python-e-Pytest"  uv  run  pytest  tests / Command / hover2.py - -headed - s