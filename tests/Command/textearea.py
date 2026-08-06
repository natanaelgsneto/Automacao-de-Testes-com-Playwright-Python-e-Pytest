def test_press(page):
    page.goto("https://bootswatch.com/default/")
    page.pause()

    page.get_by_placeholder("name@example.com").fill("teste@teste.com")
    page.get_by_placeholder("name@example.com").press("Tab")

    # Digita lentamente
    page.keyboard.type("1234", delay=500)

    page.wait_for_timeout(5000)
def test_press(page):
    page.goto("https://bootswatch.com/default/")
    page.pause()

    page.get_by_role(
        "textbox",
        name="Example textarea"
    ).type("ESCREVENDO TEXTO", delay=150)
    textarea = page.get_by_role(
        "textbox",
        name="Example textarea"
    )

    # Deixa o campo vermelho
    textarea.evaluate(
        "(element) => element.style.backgroundColor = 'red'"
    )
#para rodar no cmd:
    #uv    run    pytest    tests / Command / testearea.py - -headed
    #Faça    estas    verificações:    1.    Verifique    a    configuração    do    PyCharm

    #Vá    em:    Run → Edit    Configurations...

    #Na    configuração    do    pytest, veja    se    em    Additional    pytest  options  existe:  --headed
    #Se    não    existir, adicione    e    clique    em    Apply    e    OK.

    #2.    Execute    pelo    terminal    na    pasta    do    projeto    Abra  um  terminal  na  pasta  do   projeto  e   execute:  cd "C:\Users\NatanaelNote\PycharmProjects\Automacao-de-Testes-com-Playwright-Python-e-Pytest"  uv  run  pytest  tests / Command / textearea.py - -headed - s