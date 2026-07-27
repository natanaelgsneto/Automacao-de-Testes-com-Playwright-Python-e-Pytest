def test_get_by_roles(page):
    page.goto("https://bootswatch.com/default/")
    page.pause()
    page.locator("#navbarColor01").get_by_role('button', name='dropdown').click()
    #no playwight inspector clicar em Step Over
