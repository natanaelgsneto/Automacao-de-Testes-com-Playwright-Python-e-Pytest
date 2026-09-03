from playwright.sync_api import sync_playwright
from Page.Cadastro_login import Cadastro_login
with sync_playwright() as p:
    # O headless=False FORÇA o navegador a abrir na sua tela
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()

    # Executa o seu Page Object
    login = Cadastro_login(page)
    login.acessarLogin()
    login.fazerLogin(email="ngsneto@gmail.com", senha="123")

    # Mantém aberto por 5 segundos antes de fechar
    page.wait_for_timeout(5000)
    browser.close()