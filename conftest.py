import pytest
import os
import re

# Domínios de anúncio/rastreamento que quebram os testes do automationexercise.com.
# Os iframes "aswift_N" e o interstitial "#google_vignette" vêm daqui e interceptam
# os cliques. Abortar essas requisições elimina a instabilidade.
ANUNCIOS = re.compile(
    r"(googlesyndication|doubleclick|googleadservices|adtrafficquality"
    r"|fundingchoicesmessages|google-analytics|googletagmanager)"
)


@pytest.fixture(scope="function")
def contexto(browser):
    video_dir = os.path.join(os.getcwd(), "Vídeo")

    # Abre um navegador/contexto totalmente novo a cada teste
    contexto = browser.new_context(
        base_url='https://automationexercise.com/',
        record_video_dir=video_dir
    )
    # Bloqueia os anúncios em todas as páginas do contexto
    contexto.route(ANUNCIOS, lambda route: route.abort())
    yield contexto
    # yield Fecha tudo após o teste terminar
    contexto.close()


@pytest.fixture(scope="function")
def page(contexto):
    # yield Abre uma nova página limpa para o teste
    pagina = contexto.new_page()
    yield pagina
    # Fecha a página após o teste
    pagina.close()

