import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://automationexercise.com/login")
    page.get_by_role("link", name=" Signup / Login").click()
    page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address").click()
    page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address").fill("nata@")
    page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address").press("ArrowLeft")
    page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address").fill("natan@")
    page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address").press("ArrowRight")
    page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address").fill("natan@gmail.com")
    page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address").press("Tab")
    page.get_by_role("textbox", name="Password").fill("natan@123")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text("Your email or password is")).to_be_visible()
    #para rodar: uv run pytest Exercicios/execises2.py -v -s --headed
