def test_google(page):
    page.goto("https://www.google.com")

    page.pause()

    assert "Google" in page.title() #para terminar o teste tem que fechar o Playwright Inspector
    #no playwight inspector clicar em Step Over e fecha a janela do playwight
def test_locator(page):
    page.goto("https://automationexercise.com/login")
    page.pause()
    page.locator("//*[@id='form']/div/div/div[1]/div/form/button").click()

