import pytest
import os


@pytest.fixture(scope="function")
def contexto(browser):
    video_dir = os.path.join(os.getcwd(), "Vídeo")

    # Abre um navegador/contexto totalmente novo a cada teste
    contexto = browser.new_context(
        base_url='https://automationexercise.com/',
        record_video_dir=video_dir
    )
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

