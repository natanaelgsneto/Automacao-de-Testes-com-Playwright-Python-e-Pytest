def test_get_by_roles(page):
    page.goto("https://www.automationexercise.com")
    page.get_by_role("link", name="Signup / Login").click()
    page.pause()
    #no playwight inspector clicar em Step Over e fecha a janela do playwight

