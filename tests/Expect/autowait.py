from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:

    # 1. Acessa o site
    page.goto(
        "https://automationexercise.com",
        wait_until="domcontentloaded"
    )

    # Espera a página carregar
    page.wait_for_load_state("networkidle")

    # Inspector
    page.pause()


    # 2. Valida categoria Women
    women = page.get_by_role("heading", name="Women")

    women.wait_for(
        state="visible",
        timeout=5000
    )

    expect(women).to_be_visible()


    # 3. Localiza produto Madame Top For Women
    product = page.locator(".single-products").filter(
        has_text="Madame Top For Women"
    ).first


    # Espera produto aparecer
    product.wait_for(
        state="visible",
        timeout=5000
    )


    # Hover
    product.hover()


    # Inspector após hover
    page.pause()


    # 4. Botão Add to cart
    add_cart = product.locator(".add-to-cart").first


    # Espera botão ficar disponível
    add_cart.wait_for(
        state="visible",
        timeout=5000
    )


    add_cart.click(force=True)


    # Inspector após clique
    page.pause()


    # 5. Modal
    modal = page.locator("#cartModal")


    # Espera modal aparecer
    modal.wait_for(
        state="visible",
        timeout=5000
    )


    # 6. Valida modal
    expect(modal).to_be_visible()


    # 7. Valida título
    expect(
        modal.get_by_role("heading", name="Added!")
    ).to_be_visible()


    # 8. Valida texto
    expect(modal).to_contain_text(
        "Your product has been added to cart.",
        timeout=5000
    )


    # 9. Botão Continue Shopping
    btn_continue = modal.get_by_role(
        "button",
        name="Continue Shopping"
    )


    btn_continue.wait_for(
        state="visible",
        timeout=5000
    )


    expect(btn_continue).to_be_visible()


    # Inspector antes de fechar
    page.pause()


    # 10. Fecha modal
    btn_continue.click()


    # 11. Espera modal desaparecer
    modal.wait_for(
        state="hidden",
        timeout=5000
    )


    expect(modal).not_to_be_visible()

    # ==========================================================
    # OPÇÃO --headed
    # ==========================================================

    # O parâmetro --headed serve para abrir o navegador
    # durante a execução do teste.
    #
    # Com --headed:
    # - O Chrome/Chromium abre na tela
    # - Você consegue acompanhar os cliques, preenchimentos e ações
    # - É útil para aprender, depurar erros e usar o Playwright Inspector
    #
    # Exemplo:
    # uv run pytest Command/hover.py --headed

    # Sem --headed:
    # - O teste roda em modo invisível (headless)
    # - O navegador executa em segundo plano
    # - É mais usado em automação de testes no CI/CD
    #
    # Exemplo:
    # uv run pytest Command/hover.py