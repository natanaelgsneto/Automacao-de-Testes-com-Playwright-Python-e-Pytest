def test_click(page):
    page.goto("https://automationexercise.com")
    page.pause()
    #no playwight inspector clicar duas vezes em Step Over e fecha a janela do playwight

    page.get_by_role("link", name="Website for Automation").click(x={"10"},y={"11"})

