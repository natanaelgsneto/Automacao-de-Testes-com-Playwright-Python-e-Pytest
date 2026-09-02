from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:

    # 1. Abrir o site
    page.goto("https://automationexercise.com/")
    page.pause()
    # 2. Entrar em Signup / Login
    page.get_by_role("link", name="Signup / Login").click()

    # 3. Criar novo usuário
    page.get_by_role("textbox", name="Name").fill("roberto")

    page.locator("form").filter(
        has_text="Signup"
    ).get_by_placeholder("Email Address").fill(
        "roberto123456789@gmail.com"
    )

    page.get_by_role("button", name="Signup").click()

    # 4. Confirmar que chegou na tela de criação da conta
    expect(
        page.get_by_text("Enter Account Information")
    ).to_be_visible()

    # 5. Informações da conta
    page.get_by_text("Mr.").click()

    page.get_by_role("textbox", name="Password *").fill("Roberto@123")

    # 6. Data de nascimento
    page.locator("#days").select_option("16")
    page.locator("#months").select_option("11")
    page.locator("#years").select_option("1993")

    # 7. Newsletter
    page.get_by_text("Sign up for our newsletter!").click()
    page.get_by_text("Receive special offers from").click()

    # 8. Dados pessoais
    page.get_by_role("textbox", name="First name *").fill("Roberto")
    page.get_by_role("textbox", name="Last name *").fill("Silva")

    # 9. Empresa
    page.get_by_role(
        "textbox",
        name="Company",
        exact=True
    ).fill("TI")

    # 10. Endereço
    page.get_by_role(
        "textbox",
        name="Address * (Street address, P."
    ).fill("Rua Teste")

    page.get_by_role(
        "textbox",
        name="Address 2"
    ).fill("teste")

    # 11. País
    page.get_by_label("Country *").select_option("Israel")

    # 12. Estado
    page.get_by_role(
        "textbox",
        name="State *"
    ).fill("PB")

    # 13. Cidade
    page.get_by_role(
        "textbox",
        name="City * Zipcode *"
    ).fill("JOAO PESSOA")

    # 14. CEP
    page.locator("#zipcode").fill("58071590")

    # 15. Telefone
    page.get_by_role(
        "textbox",
        name="Mobile Number *"
    ).fill("83987080608")

    # 16. Criar conta
    page.get_by_role(
        "button",
        name="Create Account"
    ).click()

    # 17. Verificar criação da conta
    expect(
        page.get_by_text("Account Created!")
    ).to_be_visible()

    # 18. Continuar
    page.get_by_role(
        "link",
        name="Continue"
    ).click()

    # 19. Deletar conta
    page.get_by_role(
        "link",
        name="Delete Account"
    ).click()

    # 20. Verificar exclusão
    expect(
        page.get_by_text("Account Deleted!")
    ).to_be_visible()

    # 21. Continuar
    page.get_by_role(
        "link",
        name="Continue"
    ).click()