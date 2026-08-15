from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://automationexercise.com/")

    # Entrar em Signup / Login
    page.get_by_role("link", name="Signup / Login").click()

    # Formulário de cadastro
    page.get_by_placeholder("Name").fill("roberto")

    page.locator("form").filter(
        has_text="Signup"
    ).get_by_placeholder("Email Address").fill(
        "roberto123456789@gmail.com"
    )

    page.get_by_role("button", name="Signup").click()

    # Verifica se chegou na página de criação da conta
    expect(
        page.get_by_text("Enter Account Information")
    ).to_be_visible()

    # Gênero
    page.locator("#id_gender1").check()

    # Senha
    page.get_by_label("Password").fill("Roberto@123")

    # Data de nascimento
    page.locator("#days").select_option("10")
    page.locator("#months").select_option("5")
    page.locator("#years").select_option("1990")

    # Nome
    page.get_by_label("First name").fill("Roberto")
    page.get_by_label("Last name").fill("Silva")

    # Endereço principal
    page.locator("#address1").fill("Rua Teste")

    # Estado
    page.get_by_label("State").fill("Paraiba")

    # Cidade
    page.get_by_label("City").fill("Joao Pessoa")

    # CEP
    page.get_by_label("Zipcode").fill("58000000")

    # Telefone
    page.get_by_label("Mobile Number").fill("83999999999")

    page.pause()