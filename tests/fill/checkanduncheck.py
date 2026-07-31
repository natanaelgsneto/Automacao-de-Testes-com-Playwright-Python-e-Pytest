


def test_checkbox_uncheck(page):
    page.goto("https://bootswatch.com/default/")
    page.pause()
    page.get_by_role("checkbox", name="Default checkbox").uncheck()
    page.get_by_role("checkbox", name="Default checkbox").check()
    page.pause()
