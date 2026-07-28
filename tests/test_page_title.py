def test_google(page):
    page.goto("https://www.google.com")

    page.pause()

    assert "Google" in page.title() #para terminar o teste tem que fechar o Playwright Inspector