from pathlib import Path

from playwright.sync_api import expect


def test_importar_arquivos(page):

    # ==========================================================
    # CAMINHO DO ARQUIVO
    # ==========================================================

    arquivo = (
        Path(__file__).resolve().parent.parent
        / "Store"
        / "test_importar_arquivo"
        / "teste123.txt"
    )

    assert arquivo.exists(), f"Arquivo não encontrado: {arquivo}"

    # ==========================================================
    # ACESSA O TRANSFERNOW
    # ==========================================================

    page.goto("https://www.transfernow.net/pt")

    page.wait_for_load_state("domcontentloaded")

    # ==========================================================
    # COMEÇAR + INTERCEPTAR JANELA DE UPLOAD
    # ==========================================================

    with page.expect_file_chooser() as file_chooser_info:
        page.get_by_role(
            "button",
            name="Começar"
        ).click()

    file_chooser = file_chooser_info.value

    # Envia o arquivo diretamente
    file_chooser.set_files(str(arquivo))

    # ==========================================================
    # REDUZ O ZOOM
    # ==========================================================

    email = page.get_by_role(
        "textbox",
        name="Seu e-mail"
    )

    email.press("ControlOrMeta+-")
    email.press("ControlOrMeta+-")
    email.press("ControlOrMeta+-")

    # ==========================================================
    # ACEITAR E CONTINUAR
    # ==========================================================

    page.get_by_role(
        "button",
        name="Aceitar e Continuar"
    ).click()

    page.wait_for_timeout(2000)

    # ==========================================================
    # CRIAR UM LINK
    # ==========================================================

    page.get_by_role(
        "button",
        name="Criar um link"
    ).click()

    # ==========================================================
    # E-MAIL
    # ==========================================================

    page.get_by_role(
        "textbox",
        name="Seu e-mail"
    ).fill("teste@teste123.com")

    # ==========================================================
    # OBTER LINK
    # ==========================================================

    page.get_by_role(
        "button",
        name="Obter um link"
    ).click()

    # ==========================================================
    # VALIDAÇÃO FINAL
    # ==========================================================

    expect(
        page.get_by_text("Seu link está pronto!")
    ).to_be_visible(timeout=30000)