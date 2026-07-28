def test_get_by_label(page):
    page.goto("https://bootswatch.com/default/")
    page.pause()
    page.get_by_label('Valid input',exact=True).fill('Teste')
    #no playwight inspector clicar em Step Over e fecha a janela do playwight
