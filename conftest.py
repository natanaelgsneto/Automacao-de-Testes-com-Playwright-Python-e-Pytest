import os
import pytest
import pytest_html
from slugify import slugify


# ============================================================
# CONFIGURAÇÕES
# ============================================================

BASE_URL = "https://automationexercise.com/"
STORAGE_FILE = "playwright/auth/state.json"
VIDEO_DIR = "videos"
SCREENSHOT_DIR = "imagens"
TRACE_DIR = "trace"


# ============================================================
# FIXTURE DO CONTEXTO
# ============================================================

@pytest.fixture(scope="session")
def contexto(browser):
    # Cria as pastas necessárias
    os.makedirs(VIDEO_DIR, exist_ok=True)
    os.makedirs(SCREENSHOT_DIR, exist_ok=True)
    os.makedirs(TRACE_DIR, exist_ok=True)

    # Se existir estado de autenticação, utiliza
    if os.path.isfile(STORAGE_FILE):

        contexto = browser.new_context(
            base_url=BASE_URL,
            record_video_dir=VIDEO_DIR,
            storage_state=STORAGE_FILE
        )

    else:

        contexto = browser.new_context(
            base_url=BASE_URL,
            record_video_dir=VIDEO_DIR
        )

    # Inicia o trace
    contexto.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )

    yield contexto

    # ========================================================
    # FINALIZAÇÃO
    # ========================================================

    # Salva o trace
    contexto.tracing.stop(
        path=os.path.join(TRACE_DIR, "trace.zip")
    )

    # Salva estado de autenticação
    if not os.path.isfile(STORAGE_FILE):

        os.makedirs(
            os.path.dirname(STORAGE_FILE),
            exist_ok=True
        )

        contexto.storage_state(
            path=STORAGE_FILE
        )

    # Fecha o contexto
    contexto.close()


# ============================================================
# FIXTURE DA PÁGINA
# ============================================================

@pytest.fixture(scope="session")
def page(contexto):

    pagina = contexto.new_page()

    pagina.set_default_timeout(10000)

    pagina.set_default_navigation_timeout(30000)

    yield pagina

    pagina.close()


# ============================================================
# SCREENSHOT AUTOMÁTICO EM CASO DE FALHA
# ============================================================

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    # Compatibilidade com pytest-html
    extras = getattr(report, "extras", [])

    # Só captura depois da execução do teste
    if report.when == "call":

        xfail = hasattr(report, "wasxfail")

        try:

            # Captura somente quando o teste falhar
            if report.failed and not xfail:

                # Nome seguro para o arquivo
                nome = slugify(item.nodeid)

                screen_file = os.path.join(
                    SCREENSHOT_DIR,
                    f"{nome}.png"
                )

                # Recupera a fixture page
                pagina = item.funcargs.get("page")

                if pagina:

                    pagina.screenshot(
                        path=screen_file,
                        full_page=True
                    )

                    # Adiciona a imagem ao relatório HTML
                    extras.append(
                        pytest_html.extras.png(screen_file)
                    )

        except Exception as e:

            print(
                f"Erro ao capturar imagem: {e}"
            )

    report.extras = extras