def test_google(page):
    page.goto("https://www.google.com")
    page.pause()   # Pausa aqui
    page.get_by_role("button", name="Pesquisar Google").click()
    assert "Google" in page.title()
    #no playwight inspector clicar em Step Over e fecha a janela do playwight
