def test_click(page):
    page.goto("https://automationexercise.com")
    page.pause()
    #no playwight inspector clicar duas vezes em Step Over e fecha a janela do playwight

    page.get_by_role("link", name="(5) H&M").click()
    page.get_by_role("link", name="(5) H&M").click(modifiers=['Con']).click()
#valores que podem ser atribuidos aos modifiers  (Alt|Control|ControlOrMeta|Meta|Shift)
