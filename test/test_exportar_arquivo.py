from pathlib import Path

from playwright.sync_api import Page


def test_baixar_arquivos(page: Page) -> None:

    # ==========================================================
    # 1. ABRIR TRANSFERNOW
    # ==========================================================

    page.goto(
        "https://www.transfernow.net/pt"
    )

    page.wait_for_load_state(
        "domcontentloaded"
    )

    page.pause()

    # ==========================================================
    # 2. CLICAR EM COMEÇAR
    # ==========================================================

    page.get_by_role(
        "button",
        name="Começar"
    ).click()

    page.pause()

    # ==========================================================
    # 3. LOCALIZAR O ARQUIVO
    # ==========================================================

    arquivo = (
        Path(__file__).resolve().parent.parent
        / "Store"
        / "test_importar_arquivo"
        / "teste123.txt"
    )

    assert arquivo.exists(), (
        f"Arquivo não encontrado: {arquivo}"
    )

    print(
        f"Arquivo encontrado: {arquivo}"
    )

    # ==========================================================
    # 4. ENVIAR ARQUIVO
    # ==========================================================

    page.locator(
        'input[type="file"]'
    ).nth(1).set_input_files(
        str(arquivo)
    )

    page.pause()

    # ==========================================================
    # 5. CRIAR UM LINK
    # ==========================================================

    page.get_by_role(
        "button",
        name="Criar um link"
    ).click()

    page.pause()

    # ==========================================================
    # 6. PREENCHER E-MAIL
    # ==========================================================

    page.get_by_role(
        "textbox",
        name="Seu e-mail"
    ).fill(
        "ngsneto@gmail.com"
    )

    page.pause()

    # ==========================================================
    # 7. OBTER LINK
    # ==========================================================

    page.get_by_role(
        "button",
        name="Obter um link"
    ).click()

    page.wait_for_timeout(
        2000
    )

    page.pause()

    # ==========================================================
    # 8. PEGAR O LINK REAL DE DOWNLOAD
    # ==========================================================

    link_download = page.locator(
        "#hintDownloadExternalLink"
    )

    link_download.wait_for(
        state="visible"
    )

    url_download = link_download.get_attribute(
        "href"
    )

    assert url_download, (
        "Link de download não encontrado"
    )

    print(
        f"Link de download: {url_download}"
    )

    # ==========================================================
    # 9. ABRIR O LINK EM NOVA PÁGINA
    # ==========================================================

    page1 = page.context.new_page()

    page1.goto(
        url_download
    )

    page1.wait_for_load_state(
        "domcontentloaded"
    )

    print(
        f"Página de download: {page1.url}"
    )

    page1.pause()

    # ==========================================================
    # 10. CRIAR PASTA DE DOWNLOAD
    # ==========================================================

    pasta_download = Path(
        r"C:\Users\NatanaelNote\PycharmProjects\UploadDownload\Store\Download"
    )

    pasta_download.mkdir(
        parents=True,
        exist_ok=True
    )

    # ==========================================================
    # 11. AGUARDAR "BAIXAR TUDO"
    # ==========================================================

    botao_baixar = page1.get_by_role(
        "link",
        name="Baixar tudo"
    )

    botao_baixar.wait_for(
        state="visible"
    )

    print(
        "Botão 'Baixar tudo' encontrado."
    )

    page1.pause()

    # ==========================================================
    # 12. CAPTURAR DOWNLOAD
    # ==========================================================

    with page1.expect_download() as download_info:

        botao_baixar.click()

    # ==========================================================
    # 13. OBTER DOWNLOAD
    # ==========================================================

    download = download_info.value

    print(
        f"Download recebido: "
        f"{download.suggested_filename}"
    )

    # ==========================================================
    # 14. DEFINIR CAMINHO FINAL
    # ==========================================================

    caminho_arquivo = (
        pasta_download
        / download.suggested_filename
    )

    # ==========================================================
    # 15. SALVAR DOWNLOAD
    # ==========================================================

    download.save_as(
        str(caminho_arquivo)
    )

    print(
        f"Arquivo salvo em: {caminho_arquivo}"
    )

    # ==========================================================
    # 16. VALIDAR
    # ==========================================================

    assert caminho_arquivo.exists(), (
        f"Arquivo não encontrado: {caminho_arquivo}"
    )

    print(
        "=========================================="
    )
    print(
        "DOWNLOAD REALIZADO COM SUCESSO!"
    )
    print(
        "=========================================="
    )

    page1.pause()