def test_google(page):
    page.goto("https://www.google.com")

    page.pause()

    assert "Google" in page.title() #para terminar o teste tem que fechar o Playwright Inspector
    #no playwight inspector clicar em Step Over e fecha a janela do playwight
def test_title(page):
    page.goto("https://bootswatch.com/default/")
    page.pause()
    page.get_by_title("Source Title").nth(0).click()

