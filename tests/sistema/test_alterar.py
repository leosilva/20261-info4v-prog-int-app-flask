from random import randint
import unittest

from playwright.sync_api import sync_playwright


class TestAlterarUsuario(unittest.TestCase):
    def test_alterar_usuario(self):
        with sync_playwright() as playwright:
            navegador = playwright.chromium.launch(
                headless=True,
                slow_mo=1500)
            pagina = navegador.new_page()

            usuario = f"teste-alterar-{randint(0, 99999)}"
            usuario_atualizado = f"{usuario}-novo"
            email = f"{usuario}@example.com"
            email_atualizado = f"{usuario_atualizado}@example.com"

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

            # Abre a edição do usuário pela tela de listagem.
            pagina.locator("#menu-listar").click()
            usuario_listado = pagina.locator("li").filter(has_text=usuario)
            self.assertEqual(usuario_listado.count(), 1)
            usuario_listado.locator("a", has_text="Editar").click()

            self.assertIn("/editar/", pagina.url)
            self.assertEqual(
                pagina.locator("#titulo-cadastro").inner_text().strip(),
                "Editar Usuário")

            # Altera os dados e salva o usuário.
            pagina.locator("#username").fill(usuario_atualizado)
            pagina.locator("#email").fill(email_atualizado)
            pagina.locator("#salvar").click()
            self.assertEqual(pagina.url, "http://127.0.0.1:5000/")

            # Confirma os dados alterados na listagem.
            pagina.locator("#menu-listar").click()
            usuario_atualizado_listado = pagina.locator("li").filter(
                has_text=usuario_atualizado)
            self.assertEqual(usuario_atualizado_listado.count(), 1)
            self.assertIn(
                email_atualizado,
                usuario_atualizado_listado.inner_text())

            navegador.close()
