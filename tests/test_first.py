def test_google(page):
    page.goto("https://www.google.com")
    page.pause()   # Pausa aqui
    page.get_by_role("button", name="Pesquisar Google").click()
    assert "Google" in page.title()