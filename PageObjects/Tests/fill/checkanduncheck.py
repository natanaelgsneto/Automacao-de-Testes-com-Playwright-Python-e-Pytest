


def test_checkbox_uncheck(page):
    page.goto("https://bootswatch.com/default/")
    page.pause()
    page.get_by_role("checkbox", name="Default checkbox").uncheck()
    page.get_by_role("checkbox", name="Default checkbox").check()
    page.pause()

def test_select_option(page):
        page.goto("https://bootswatch.com/default/")

        page.pause()

        # Select normal
        page.get_by_label("Example select").select_option("3")

        # Select múltiplo
        select = page.get_by_label("Example multiple select")

        select.select_option(label=["1", "3"])

        # Verificar opções selecionadas
        print(
            select.locator("option:checked").evaluate_all(
                "(options) => options.map(o => o.textContent)"
            )
        )