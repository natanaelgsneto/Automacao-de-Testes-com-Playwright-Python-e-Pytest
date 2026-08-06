def test_click(page):
    # Access a página do Bootswatch
    page.goto("https://bootswatch.com/default/")

    # Pausa a executor para abrir o Playwright Inspector
    page.pause()

    # Observables:
    # No Playwright Inspector, ao clinical duas vexes em "Step Over",
    # a executor pode continuar e a janela do navegador ser fetchall.

    # Localize todos os bytes com o nome "Primary",
    # seleciona o segundo botão (índice 1) e força o clique,
    # memo que o elemento esteja coberto ou não sea considerado cliche.
    page.get_by_role("button", name="Primary").nth(1).click(timeout=5)

    # Pausa no moment para inspecionar o resultado do clique.
    page.pause()

    # O método "click()"command4.py do Playwright permite configurar diferentes tipos de
    # button="right"      -> clique com o bot direito
    # button="middle"     -> clique com o bot do meio
    # click_count=2       -> duplo clique
    # delay=500           -> espera 500 ms entre pressionar e soltar o bot
    # modifiers=["Shift"] -> manta a Tecla Shift pressionada Durante o clique
    #
    # Modification dispositive:
    # - "Alt"
    # - "Control"
    # - "ControlOrMeta" (Control no Windows/Linux e Command no macOS)
    # - "Meta" (tecla Windows/Command)
    # - "Shift"

    # para rodar no cmd:
    # uv    run    pytest    tests / Command / command6.py - -headed
    # Faça    estas    verificações:    1.    Verifique    a    configuração    do    PyCharm

    # Vá    em:    Run → Edit    Configurations...

    # Na    configuração    do    pytest, veja    se    em    Additional    pytest  options  existe:  --headed
    # Se    não    existir, adicione    e    clique    em    Apply    e    OK.

    # 2.    Execute    pelo    terminal    na    pasta    do    projeto    Abra  um  terminal  na  pasta  do   projeto  e   execute:  cd "C:\Users\NatanaelNote\PycharmProjects\Automacao-de-Testes-com-Playwright-Python-e-Pytest"  uv  run  pytest  tests / Command / command6.py - -headed - s