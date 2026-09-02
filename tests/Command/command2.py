def test_click(page):
    page.goto("https://automationexercise.com")
    page.pause()

    # No Playwright Inspector, clique em Resume para continuar.
    page.get_by_role("link", name="Website for Automation").click()

    #para rodar no cmd:
    #uv    run    pytest    tests / Command / command2.py - -headed
    #Faça    estas    verificações:    1.    Verifique    a    configuração    do    PyCharm

    #Vá    em:    Run → Edit    Configurations...

    #Na    configuração    do    pytest, veja    se    em    Additional    pytest  options  existe:  --headed
    #Se    não    existir, adicione    e    clique    em    Apply    e    OK.

    #2.    Execute    pelo    terminal    na    pasta    do    projeto    Abra  um  terminal  na  pasta  do   projeto  e   execute:  cd "C:\Users\NatanaelNote\PycharmProjects\Automacao-de-Testes-com-Playwright-Python-e-Pytest"  uv  run  pytest  tests / Command / command2.py - -headed - s