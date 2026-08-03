from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:

    # 1. Acessa o site
    page.goto(
        "https://automationexercise.com",
        wait_until="domcontentloaded"
    )

    # Abre o Playwright Inspector
    page.pause()


    # 2. Valida categoria Women
    expect(
        page.get_by_role("heading", name="Women")
    ).to_be_visible()


    # 3. Localiza o produto Madame Top For Women
    product = page.locator(".single-products").filter(
        has_text="Madame Top For Women"
    ).first


    # 4. Faz hover no produto
    product.hover()


    # Abre Inspector para visualizar o hover
    page.pause()


    # 5. Clica em Add to cart
    product.locator(".add-to-cart").first.click(force=True)


    # 6. Localiza o modal
    modal = page.locator("#cartModal")


    # 7. Aguarda modal aparecer
    expect(modal).to_have_class(
        "modal show",
        timeout=5000
    )


    # 8. Valida modal visível
    expect(modal).to_be_visible()


    # Inspector para conferir o modal
    page.pause()


    # 9. Valida título do modal
    expect(
        modal.locator(".modal-title")
    ).to_have_text("Added!")


    # 10. Valida mensagem do modal
    expect(
        modal
    ).to_contain_text(
        "Your product has been added to cart."
    )


    # 11. Valida botão Continue Shopping
    continue_button = modal.get_by_role(
        "button",
        name="Continue Shopping"
    )

    expect(
        continue_button
    ).to_be_visible()


    # 12. Valida link View Cart
    expect(
        modal.get_by_role(
            "link",
            name="View Cart"
        )
    ).to_be_visible()


    # 13. Fecha modal
    continue_button.click()


    # 14. Confirma modal fechado
    expect(modal).not_to_be_visible()