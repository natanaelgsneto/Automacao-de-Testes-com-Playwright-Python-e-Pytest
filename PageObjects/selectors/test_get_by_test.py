def test_get_by_roles(page):
    page.goto('https:///automationexercise.com/')
    page.pause()
    page.get_by_text('Full-Fledged practice website for').first.click()

    #no playwight inspector clicar em Step Over e fecha a janela do playwight
