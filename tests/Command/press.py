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