from playwright.sync_api import expect


def test_nova_aba(page):
    page.goto("https://demoqa.com/browser-windows")

    with page.expect_popup() as popup_info:
        page.locator("#tabButton").click()

    nova_aba = popup_info.value
    nova_aba.wait_for_load_state()

    texto = nova_aba.locator("#sampleHeading").text_content()
    print(f"Texto da página: {texto}")

    expect(nova_aba.locator("#sampleHeading")).to_have_text(
        "This is a sample page"
    )

    nova_aba.close()

    print(f"Voltamos para: {page.title()}")