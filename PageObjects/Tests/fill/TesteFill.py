from playwright.async_api import Page


def test_example(page: Page) -> None:

    page.goto("https://automationexercise.com/login")
    page.pause()
    page.get_by_role("textbox", name="Name").fill('Natanael', timeout=100000)
    page.locator("form").filter(has_text="Signup").get_by_placeholder("Email Address").fill('natanael@gmail.com')
    page.get_by_role("button", name="Signup").click()
