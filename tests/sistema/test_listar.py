from random import randint
import unittest

from playwright.sync_api import sync_playwright


class TestMenuListar(unittest.TestCase):
    def test_listar_usuarios(self):
        with sync_playwright() as playwright:
            navegador = playwright.chromium.launch(
                headless=True,
                slow_mo=1500)
            pagina = navegador.new_page()

            # Cadastra um usuário para garantir que ele estará disponível na lista.
            usuario = f"teste-listar-{randint(0, 99999)}"

            pagina.goto("http://127.0.0.1:5000/")
            pagina.locator("#menu-cadastrar").click()
            self.assertEqual(
                pagina.url,
                "http://127.0.0.1:5000/cadastrar")

            pagina.locator("#username").fill(usuario)
            pagina.locator("#email").fill(f"{usuario}@example.com")
            pagina.locator("#salvar").click()
            self.assertEqual(pagina.url, "http://127.0.0.1:5000/")

            # Acessa a listagem de usuários.
            pagina.locator("#menu-listar").click()
            self.assertEqual(
                pagina.url,
                "http://127.0.0.1:5000/listar")
            self.assertEqual(
                pagina.locator("h2").inner_text(),
                "Lista de Usuários")

            usuario_listado = pagina.locator("li").filter(has_text=usuario)
            self.assertEqual(usuario_listado.count(), 1)
            self.assertIn(f"{usuario}@example.com", usuario_listado.inner_text())

            navegador.close()
