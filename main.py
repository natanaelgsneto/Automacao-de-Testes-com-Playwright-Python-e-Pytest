def test_google(page):

    page.goto("https://www.google.com")

    print(page.title())
    page.pause()
    assert "Google" in page.title()