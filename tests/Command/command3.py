def test_click(page):
    page.goto("https://automationexercise.com")
    page.pause()
    #no playwight inspector clicar duas vezes em Step Over e fecha a janela do playwight

    page.get_by_role("link", name="(5) H&M").click()
    page.get_by_role("link", name="(5) H&M").click(modifiers=['Con']).click()
#valores que podem ser atribuidos aos modifiers  (Alt|Control|ControlOrMeta|Meta|Shift)
#para rodar no cmd:
    #uv    run    pytest    tests / Command / command3.py - -headed
    #Faça    estas    verificações:    1.    Verifique    a    configuração    do    PyCharm

    #Vá    em:    Run → Edit    Configurations...

    #Na    configuração    do    pytest, veja    se    em    Additional    pytest  options  existe:  --headed
    #Se    não    existir, adicione    e    clique    em    Apply    e    OK.

    #2.    Execute    pelo    terminal    na    pasta    do    projeto    Abra  um  terminal  na  pasta  do   projeto  e   execute:  cd "C:\Users\NatanaelNote\PycharmProjects\Automacao-de-Testes-com-Playwright-Python-e-Pytest"  uv  run  pytest  tests / Command / command3.py - -headed - s