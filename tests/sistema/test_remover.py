from random import randint
import unittest

from playwright.sync_api import sync_playwright


class TestRemoverUsuario(unittest.TestCase):
    def test_remover_usuario(self):
        with sync_playwright() as playwright:
            navegador = playwright.chromium.launch(
                headless=True,
                slow_mo=1500)
            pagina = navegador.new_page()

            usuario = f"teste-remover-{randint(0, 99999)}"
            email = f"{usuario}@example.com"

            # Cadastra um usuário para iniciar o cenário do teste.
            pagina.goto("http://127.0.0.1:5000/")
            pagina.locator("#menu-cadastrar").click()
            self.assertEqual(
                pagina.url,
                "http://127.0.0.1:5000/cadastrar")

            pagina.locator("#username").fill(usuario)
            pagina.locator("#email").fill(email)
            pagina.locator("#salvar").click()
            self.assertEqual(pagina.url, "http://127.0.0.1:5000/")

            # Localiza o usuário na listagem e remove-o.
            pagina.locator("#menu-listar").click()
            usuario_listado = pagina.locator("li").filter(has_text=usuario)
            self.assertEqual(usuario_listado.count(), 1)
            usuario_listado.locator("a", has_text="Remover").click()

            self.assertIn("/remover/", pagina.url)

            # Confirma que o usuário não aparece mais na listagem.
            pagina.locator("#menu-listar").click()
            usuario_removido = pagina.locator("li").filter(has_text=usuario)
            self.assertEqual(usuario_removido.count(), 0)

            navegador.close()
