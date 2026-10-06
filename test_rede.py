from playwright.sync_api import Page


def test_observar_trafego_de_rede(page: Page):
    page.on(
        "request",
        lambda request: print(f">> {request.method} {request.url}")
    )

    page.on(
        "response",
        lambda response: print(f"<< {response.status} {response.url}")
    )

    page.goto("http://localhost:5000/produtos")

    def test_login_dispara_requisicao_real(page: Page):
        requisicoes_login = []

        page.on(
            "request",
            lambda r: requisicoes_login.append(r)
            if "/api/login" in r.url
            else None
        )

        page.goto("http://localhost:5000/login")

        page.fill("#input-email", "cliente@loja.com")
        page.fill("#input-senha", "senha123")

        page.click("#botao-entrar")

        page.wait_for_url("**/produtos")

        assert len(requisicoes_login) == 1
        assert requisicoes_login[0].method == "POST"