import time
from playwright.sync_api import Page, expect
from Page.Inscreverse import Inscreverse


def test_registrar_novo_usuario(page: Page):
    page.route("**/*google*", lambda route: route.abort())
    page.route("**/*doubleclick*", lambda route: route.abort())

    inscrever = Inscreverse(page)
    page.goto("https://automationexercise.com", wait_until="domcontentloaded")

    inscrever.botao_cadastro_login.click()
    expect(page.get_by_text('New User Signup!', exact=True)).to_be_visible()

    email_unico = f"teste_{int(time.time())}@teste.com"

    inscrever.realizar_cadastro(
        nome='Fulano',
        email=email_unico
    )

    expect(page.get_by_text('Enter Account Information', exact=True)).to_be_visible()

    inscrever.preencher_informacoes_da_conta(
        titulo='Mr',
        senha='senhaSegura123',
        data_aniversario='10/05/1995',
        sign_up_for_our_newsletter=True,
        receive_special_offers_from=True
    )

    inscrever.preencher_informacoes_endereco(
        primeiro_nome='Fulano',
        sobrenome='Silva',
        empresa='Minha Empresa',
        endereco='Rua Teste 123',
        pais='United States',
        estado='California',
        cidade='Los Angeles',
        zipcode='90001',
        numero_telefone='123456789'
    )

    inscrever.botao_criar_conta.click()

    # Valida usando role de heading
    expect(page.get_by_role("heading", name="ACCOUNT CREATED!")).to_be_visible()


def test_deletar_novo_usuario(page: Page):
    page.route("**/*google*", lambda route: route.abort())
    page.route("**/*doubleclick*", lambda route: route.abort())

    inscrever = Inscreverse(page)
    page.goto("https://automationexercise.com", wait_until="domcontentloaded")

    # 1. Cria usuário temporário
    inscrever.botao_cadastro_login.click()
    email_unico = f"deletar_{int(time.time())}@teste.com"

    inscrever.realizar_cadastro(nome='UsuarioDeletar', email=email_unico)
    inscrever.preencher_informacoes_da_conta(titulo='Mr', senha='senhaSegura123')
    inscrever.preencher_informacoes_endereco(
        primeiro_nome='Deletar',
        sobrenome='Teste',
        endereco='Rua Deletar',
        pais='United States',
        estado='State',
        cidade='City',
        zipcode='12345',
        numero_telefone='999999999'
    )
    inscrever.botao_criar_conta.click()

    # 2. Continua para a home
    inscrever.botao_continuar.click()

    # 3. Executa a exclusão da conta
    expect(inscrever.botao_deletar_conta).to_be_visible()
    inscrever.botao_deletar_conta.click()

    # Valida usando role de heading
    expect(page.get_by_role("heading", name="ACCOUNT DELETED!")).to_be_visible()