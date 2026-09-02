import os
import re
import pytest


ANUNCIOS = re.compile(
    r"(googlesyndication|doubleclick|googleadservices|adtrafficquality"
    r"|fundingchoicesmessages|google-analytics|googletagmanager)"
)


@pytest.fixture(scope="function")
def contexto(browser):

    video_dir = os.path.join(os.getcwd(), "Vídeo")
    os.makedirs(video_dir, exist_ok=True)

    contexto = browser.new_context(
        base_url="https://automationexercise.com/",
        record_video_dir=video_dir
    )

    contexto.route(
        ANUNCIOS,
        lambda route: route.abort()
    )

    yield contexto

    contexto.close()


@pytest.fixture(scope="function")
def page(contexto):

    pagina = contexto.new_page()

    yield pagina

    pagina.close()