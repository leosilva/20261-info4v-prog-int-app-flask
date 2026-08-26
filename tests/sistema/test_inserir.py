from random import randint
import unittest

from playwright.sync_api import sync_playwright

class TestMenuInserir(unittest.TestCase):
    def test_inserir_usuario(self):
        with sync_playwright() as playwright:
            navegador = playwright.chromium.launch(
                headless=False, 
                slow_mo=1500)
            # Abre o navegador
            pagina = navegador.new_page()

            # Página inicial e menu Inserir.
            pagina.goto("http://127.0.0.1:5000/")
            pagina.locator("#menu-cadastrar").click()
            self.assertEqual(pagina.url, 
                             "http://127.0.0.1:5000/cadastrar")

            # Preenchimento do formulário.
            usuario = f"teste-{randint(0,99999)}"
            pagina.locator("#username").fill(usuario)
            pagina.locator("#email").fill(f"{usuario}@example.com")

            # Salvar e verificar o redirecionamento para a página inicial.
            pagina.locator("#salvar").click()
            self.assertEqual(pagina.url, "http://127.0.0.1:5000/")

            navegador.close()