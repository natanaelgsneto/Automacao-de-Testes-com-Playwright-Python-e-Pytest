import json

from playwright.sync_api import Page, expect


# ============================================================
# TESTE 1 — Observar o tráfego de rede
# ============================================================

def test_observar_trafego_de_rede(page: Page):

    # Mostra no terminal cada requisição enviada pelo navegador
    page.on(
        "request",
        lambda request: print(
            f">> {request.method} {request.url}"
        )
    )

    # Mostra no terminal cada resposta recebida
    page.on(
        "response",
        lambda response: print(
            f"<< {response.status} {response.url}"
        )
    )

    # Acessa a página de produtos
    page.goto("http://localhost:5000/produtos")


# ============================================================
# TESTE 2 — Verificar a requisição real de login
# ============================================================

def test_login_dispara_requisicao_real(page: Page):

    # Lista que vai armazenar as requisições de login
    requisicoes_login = []

    # Observa as requisições
    page.on(
        "request",
        lambda request:
            requisicoes_login.append(request)
            if "/api/login" in request.url
            else None
    )

    # Abre a tela de login
    page.goto("http://localhost:5000/login")

    # Preenche o e-mail
    page.fill(
        "#input-email",
        "cliente@loja.com"
    )

    # Preenche a senha
    page.fill(
        "#input-senha",
        "senha123"
    )

    # Clica no botão de entrar
    page.click("#botao-entrar")

    # Espera o redirecionamento para produtos
    page.wait_for_url("**/produtos")

    # Deve ter acontecido exatamente uma requisição para login
    assert len(requisicoes_login) == 1

    # A requisição de login deve utilizar POST
    assert requisicoes_login[0].method == "POST"


# ============================================================
# TESTE 3 — Observar somente as requisições da API
# ============================================================

def test_observar_apenas_api(page: Page):

    # Função chamada para cada requisição
    def logar_apenas_api(request):

        # Verifica se a URL contém "/api/"
        if "/api/" in request.url:

            # Mostra somente as requisições da API
            print(
                f">> {request.method} {request.url}"
            )

    # Registra o observador de requisições
    page.on(
        "request",
        logar_apenas_api
    )

    # Acessa a página de produtos
    page.goto("http://localhost:5000/produtos")


# ============================================================
# TESTE 4 — Interceptar uma requisição
# ============================================================

def test_interceptar_requisicao(page: Page):

    # Função chamada quando uma requisição da API
    # for interceptada
    def interceptar(request):

        # Mostra a requisição interceptada
        print(
            f"INTERCEPTADO: "
            f"{request.method} "
            f"{request.url}"
        )

        # Continua a requisição normalmente
        request.continue_()

    # Intercepta as URLs que possuem /api/
    page.route(
        "**/api/**",
        interceptar
    )

    # Acessa a página de produtos
    page.goto("http://localhost:5000/produtos")


# ============================================================
# TESTE 5 — Mockar uma resposta da API
# ============================================================

def test_mockar_resposta_da_api(page: Page):

    # Função executada quando a API de produtos
    # for interceptada
    def interceptar(route):

        # Substitui a resposta real da API
        route.fulfill(

            # Status HTTP da resposta
            status=200,

            # Informa que a resposta é JSON
            content_type="application/json",

            # Corpo da resposta
            body='{"produtos":[{"id":1,"nome":"Produto Mock","preco":99.90}]}'
        )

    # Intercepta a API de produtos
    page.route(
        "**/api/produtos",
        interceptar
    )

    # Acessa a página de produtos
    page.goto("http://localhost:5000/produtos")


# ============================================================
# FUNÇÃO AUXILIAR — Fazer login
# ============================================================

def fazer_login(page: Page):

    # Abre a tela de login
    page.goto("http://localhost:5000/login")

    # Preenche o e-mail
    page.fill(
        "#input-email",
        "cliente@loja.com"
    )

    # Preenche a senha
    page.fill(
        "#input-senha",
        "senha123"
    )

    # Clica no botão de entrar
    page.click("#botao-entrar")

    # Espera chegar à página de produtos
    page.wait_for_url("**/produtos")


# ============================================================
# TESTE 6 — Mockar lista vazia de produtos
# ============================================================

def test_mock_lista_vazia_de_produtos(page: Page):

    # Primeiro faz login
    fazer_login(page)

    # Função que substituirá a resposta da API
    def mock_produtos_vazios(route):

        # Retorna uma lista vazia
        route.fulfill(

            # Status HTTP 200 = sucesso
            status=200,

            # Tipo da resposta
            content_type="application/json",

            # Corpo da resposta
            body="[]"
        )

    # Intercepta a API de produtos
    page.route(
        "**/api/produtos",
        mock_produtos_vazios
    )

    # Recarrega a página.
    # Agora a requisição da API será interceptada.
    page.reload()

    # Verifica que nenhum produto foi exibido
    expect(
        page.locator('[data-testid^="produto-"]')
    ).to_have_count(0)


# ============================================================
# TESTE 7 — Mockar produto customizado
# ============================================================

def test_mock_produto_customizado(page: Page):

    # Primeiro faz login
    fazer_login(page)

    # Cria um produto falso
    produtos_fake = [

        {
            "id": 1,

            "nome": "Produto Fake Caríssimo",

            "preco": 9999.99,

            "estoque": 1,

            "imagem": "/static/img/produto-1.svg",
        }

    ]

    # Função que substituirá a resposta da API
    def mock_catalogo_customizado(route):

        # Envia nossa lista de produtos falsos
        route.fulfill(

            # Status HTTP 200
            status=200,

            # Tipo da resposta
            content_type="application/json",

            # Converte a lista Python para JSON
            body=json.dumps(produtos_fake)
        )

    # Intercepta a API de produtos
    page.route(
        "**/api/produtos",
        mock_catalogo_customizado
    )

    # Recarrega a página
    page.reload()

    # Deve existir exatamente 1 produto
    expect(
        page.locator('[data-testid^="produto-"]')
    ).to_have_count(1)

    # O produto falso deve aparecer na tela
    expect(
        page.get_by_text("Produto Fake Caríssimo")
    ).to_be_visible()