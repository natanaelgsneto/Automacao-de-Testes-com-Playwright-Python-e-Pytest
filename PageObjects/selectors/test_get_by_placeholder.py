def test_get_by_roles(page):
    page.goto("https://automationexercise.com/login")
    page.pause()
    page.get_by_placeholder('Name')
    #no playwight inspector clicar em Step Over e fecha a janela do playwight
