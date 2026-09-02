from pathlib import Path
from playwright.sync_api import Page, expect


def test_importar_arquivos(page: Page) -> None:

    # Caminho do arquivo que será enviado
    arquivo = (
        Path(__file__).resolve().parent.parent
        / "Store"
        / "test_importar_arquivo"
        / "teste123.txt"
    )

    # Verifica se o arquivo existe
    assert arquivo.exists(), f"Arquivo não encontrado: {arquivo}"

    print(f"Arquivo encontrado: {arquivo}")

    # Site de teste
    page.goto("https://the-internet.herokuapp.com/upload")

    # Localiza o campo de upload e envia o arquivo
    page.locator("#file-upload").set_input_files(str(arquivo))

    # Clica em Upload
    page.locator("#file-submit").click()

    # Aguarda a página
    page.wait_for_load_state("domcontentloaded")

    # Verifica se o upload foi realizado
    expect(page.locator("h3")).to_have_text("File Uploaded!")

    # Verifica o nome do arquivo
    expect(page.locator("#uploaded-files")).to_have_text("teste123.txt")

    print("Upload realizado com sucesso!")

    page.pause()