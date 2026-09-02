def test_dbclick(page):
    page.goto(
        "https://automationexercise.com/login",
        timeout=60000,
        wait_until="domcontentloaded"
    )

    page.pause()

    page.locator(".login-form h2").dblclick()

    # para rodar no cmd:
    # uv    run    pytest    tests / dbclick / dbclick.py - -headed
    # Faça    estas    verificações:    1.    Verifique    a    configuração    do    PyCharm

    # Vá    em:    Run → Edit    Configurations...

    # Na    configuração    do    pytest, veja    se    em    Additional    pytest  options  existe:  --headed
    # Se    não    existir, adicione    e    clique    em    Apply    e    OK.

    # 2.    Execute    pelo    terminal    na    pasta    do    projeto    Abra  um  terminal  na  pasta  do   projeto  e   execute:  cd "C:\Users\NatanaelNote\PycharmProjects\Automacao-de-Testes-com-Playwright-Python-e-Pytest"  uv  run  pytest  tests / dbclick/dbclick.py - -headed - s