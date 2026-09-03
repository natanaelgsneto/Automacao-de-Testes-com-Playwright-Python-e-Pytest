def test_dbclick(page):
    page.goto("https://automationexercise.com/login")
    page.pause()
    page.locator('.login-form h2').dblclick()