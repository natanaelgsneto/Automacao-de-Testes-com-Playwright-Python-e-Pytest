from pathlib import Path

from playwright.sync_api import expect


ARQUIVO_SESSAO = Path("auth/state.json")

def test_criar_sessao_autenticada(browser):
    ARQUIVO_SESSAO.parent.mkdir(parents=True, exist_ok=True)

    context = browser.new_context(
        base_url="https://automationexercise.com/"
    )

    page = context.new_page()

    # Abre a página de login
    page.goto("/login")

    # Localiza somente o formulário de login
    formulario_login = page.locator("form").filter(
        has_text="Login"
    )

    formulario_login.get_by_placeholder(
        "Email Address"
    ).fill("albberto2@gmail.com")

    formulario_login.get_by_placeholder(
        "Password"
    ).fill("Silvinha2")

    formulario_login.get_by_role(
        "button",
        name="Login"
    ).click()

    # Confirma que o login funcionou
    expect(
        page.get_by_role("link", name="Logout")
    ).to_be_visible()

    # Salva cookies e localStorage
    context.storage_state(path=str(ARQUIVO_SESSAO))

    context.close()