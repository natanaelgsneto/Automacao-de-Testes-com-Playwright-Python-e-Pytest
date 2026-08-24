from playwright.sync_api import expect


def test_nova_aba(page):
    page.goto('https://demoqa.com/browser-windows')

    with page.expect_popup() as popup_info:
        page.get_by_text("New Tab").click()

    nova_aba = popup_info.value

    page.pause()

    nova_aba.wait_for_load_state()

    print(f"Título da nova aba: {nova_aba.title()}")

    expect(nova_aba.locator("body")).to_have_text("This is a sample page")

    nova_aba.close()

    print(f"Voltamos para: {page.title()}")