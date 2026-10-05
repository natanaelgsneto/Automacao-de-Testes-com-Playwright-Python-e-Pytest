import os

import pytest
from playwright.sync_api import Playwright


@pytest.fixture
def credenciais_login():
    # Credenciais lidas das variáveis de ambiente (não ficam no código)
    email = os.environ.get("LOGIN_EMAIL")
    senha = os.environ.get("LOGIN_SENHA")

    if not email or not senha:
        pytest.fail("Defina as variáveis de ambiente LOGIN_EMAIL e LOGIN_SENHA")

    return email, senha


@pytest.fixture
def browser_context_args(
    browser_context_args,
    playwright: Playwright
):
    iphone = playwright.devices["iPhone 12"]

    return {
        **browser_context_args,
        **iphone,
    }