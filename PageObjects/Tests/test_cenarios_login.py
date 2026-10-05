import pytest

from Page.Cadastro_login import CadastroLogin


# Email com formato válido, mas sem conta no site
EMAIL_NAO_CADASTRADO = "naoexiste.pageobjects.2026@teste.com"


# 1. Login com credenciais válidas
def test_login_com_credenciais_validas(page, credenciais_login):
    email, senha = credenciais_login
    login = CadastroLogin(page)

    login.acessar_cadastro_login()
    login.fazerLogin(email=email, senha=senha)

    login.validarLoginComSucesso()


# 2 e 3. Email não cadastrado e senha incorreta: o site recebe o formulário
# e responde "Your email or password is incorrect!"
@pytest.mark.parametrize(
    "email, senha",
    [
        pytest.param(EMAIL_NAO_CADASTRADO, "123456", id="email-nao-cadastrado"),
        # email=None usa a conta válida de LOGIN_EMAIL com uma senha errada
        pytest.param(None, "senhaIncorreta123", id="senha-incorreta"),
    ],
)
def test_login_recusado_pelo_site(page, request, email, senha):
    if email is None:
        email, _ = request.getfixturevalue("credenciais_login")

    login = CadastroLogin(page)

    login.acessar_cadastro_login()
    login.fazerLogin(email=email, senha=senha)

    login.validarLoginRecusado()


# 2 e 4. Email com formato inválido e campos vazios: o navegador bloqueia
# o envio (type="email" e required), então o site não chega a responder
@pytest.mark.parametrize(
    "email, senha, campo, motivo",
    [
        pytest.param("emailinvalido", "123456", "email", "typeMismatch", id="email-sem-arroba"),
        pytest.param("email@", "123456", "email", "typeMismatch", id="email-sem-dominio"),
        pytest.param("", "", "email", "valueMissing", id="campos-vazios-email"),
        pytest.param("", "", "senha", "valueMissing", id="campos-vazios-senha"),
    ],
)
def test_login_bloqueado_pelo_navegador(page, email, senha, campo, motivo):
    login = CadastroLogin(page)

    login.acessar_cadastro_login()
    login.fazerLogin(email=email, senha=senha)

    login.validarCampoBloqueadoPeloNavegador(campo, motivo)
