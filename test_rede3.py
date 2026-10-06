# ============================================================
# IMPORTAÇÃO
# ============================================================

# Importa a classe Page do Playwright.
# Page representa uma página/aba do navegador.
from playwright.sync_api import Page


# ============================================================
# TESTE 1 - OBSERVAR O TRÁFEGO DE REDE
# ============================================================

# Define o teste.
# O "page" é uma fixture fornecida pelo pytest-playwright.
def test_observar_trafego_de_rede(page: Page):

    # Registra um listener para observar todas as requisições.
    page.on(
        "request",

        # Executa esta função toda vez que uma requisição acontecer.
        # request.method -> método HTTP (GET, POST, etc.)
        # request.url    -> endereço da requisição
        lambda request: print(
            f">> {request.method} {request.url}"
        )
    )

    # Registra um listener para observar todas as respostas.
    page.on(
        "response",

        # response.status -> código HTTP (200, 302, 404...)
        # response.url    -> endereço da resposta
        lambda response: print(
            f"<< {response.status} {response.url}"
        )
    )

    # Acessa a página de produtos.
    page.goto("http://localhost:5000/produtos")


# ============================================================
# TESTE 2 - VERIFICAR A REQUISIÇÃO REAL DE LOGIN
# ============================================================

# Define o teste de login.
def test_login_dispara_requisicao_real(page: Page):

    # Cria uma lista vazia.
    # Vamos guardar nela as requisições feitas para /api/login.
    requisicoes_login = []

    # Observa todas as requisições realizadas pela página.
    page.on(
        "request",

        # Se a URL contiver "/api/login",
        # guarda a requisição na lista.
        #
        # Caso contrário, não faz nada.
        lambda r: requisicoes_login.append(r)
        if "/api/login" in r.url
        else None
    )

    # Abre a página de login.
    page.goto("http://localhost:5000/login")

    # Preenche o campo de e-mail.
    page.fill(
        "#input-email",
        "cliente@loja.com"
    )

    # Preenche o campo de senha.
    page.fill(
        "#input-senha",
        "senha123"
    )

    # Clica no botão de login.
    page.click("#botao-entrar")

    # Aguarda a navegação para a página de produtos.
    page.wait_for_url("**/produtos")

    # Verifica se aconteceu exatamente uma requisição para /api/login.
    assert len(requisicoes_login) == 1

    # Verifica se a requisição utilizou o método HTTP POST.
    assert requisicoes_login[0].method == "POST"


# ============================================================
# TESTE 3 - OBSERVAR SOMENTE REQUISIÇÕES DA API
# ============================================================

# Define o teste.
def test_observar_apenas_api(page: Page):

    # Cria uma função para analisar cada requisição.
    def logar_apenas_api(request):

        # Verifica se "/api/" está presente na URL.
        if "/api/" in request.url:

            # Se estiver, imprime método e URL.
            print(
                f">> {request.method} {request.url}"
            )

    # Registra nossa função como listener de requisições.
    page.on(
        "request",
        logar_apenas_api
    )

    # Abre a página de produtos.
    page.goto("http://localhost:5000/produtos")


# ============================================================
# TESTE 4 - INTERCEPTAR UMA REQUISIÇÃO
# ============================================================

# Define o teste de interceptação.
def test_interceptar_requisicao(page: Page):

    # Cria a função que será chamada quando
    # uma requisição da API for interceptada.
    def interceptar(request):

        # Mostra no terminal que a requisição foi interceptada.
        print(
            f"INTERCEPTADO: {request.method} {request.url}"
        )

        # Permite que a requisição continue normalmente.
        # Ou seja, ela segue para o servidor real.
        request.continue_()

    # Diz ao Playwright para interceptar
    # qualquer URL que contenha /api/.
    page.route(
        "**/api/**",

        # Função executada durante a interceptação.
        interceptar
    )

    # Abre a página de produtos.
    page.goto("http://localhost:5000/produtos")


# ============================================================
# TESTE 5 - MOCKAR A RESPOSTA DA API
# ============================================================

# Define o teste de mock.
def test_mockar_resposta_da_api(page: Page):

    # Cria a função responsável pela interceptação.
    def interceptar(route):

        # Em vez de deixar o servidor responder,
        # vamos fornecer uma resposta criada pelo teste.
        route.fulfill(

            # Define o código HTTP da resposta.
            status=200,

            # Informa que o conteúdo retornado é JSON.
            content_type="application/json",

            # Define o JSON que será devolvido.
            body=(
                '{"produtos":['
                '{"id":1,'
                '"nome":"Produto Mock",'
                '"preco":99.90}'
                ']}'
            )
        )

    # Intercepta especificamente a chamada para /api/produtos.
    page.route(
        "**/api/produtos",

        # Quando a URL for acessada,
        # executa a função "interceptar".
        interceptar
    )

    # Abre a página de produtos.
    # Quando a página solicitar /api/produtos,
    # o Playwright devolverá nosso JSON mockado.
    page.goto("http://localhost:5000/produtos")