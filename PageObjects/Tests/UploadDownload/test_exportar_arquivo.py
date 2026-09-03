from pathlib import Path
from playwright.sync_api import Page


def test_baixar_arquivos(page: Page) -> None:

    # Abre a página de downloads
    page.goto("https://the-internet.herokuapp.com/download")

    # Aguarda o download
    with page.expect_download() as download_info:
        page.get_by_text("teste123.txt").click()

    # Obtém o download
    download = download_info.value

    # Pasta EXATA onde o arquivo será salvo
    pasta = Path(
        r"D:\Automacao-de-Testes-com-Playwright-Python-e-Pytest-execucao-avancada-de-relatorios\Store\Download"
    )

    # Cria a pasta caso não exista
    pasta.mkdir(parents=True, exist_ok=True)

    # Caminho final do arquivo
    caminho = pasta / download.suggested_filename

    # Salva o arquivo
    download.save_as(str(caminho))

    # Verifica se o arquivo foi salvo
    assert caminho.exists()

    print(f"Download realizado com sucesso: {caminho}")