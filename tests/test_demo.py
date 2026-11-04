"""Testes locais do fluxo demonstrativo, sem Oracle e sem SMTP."""
import tempfile
import unittest
from pathlib import Path

from demo import executar_demo
from src.html_service import carregar_template


class TestPortfolioDemo(unittest.TestCase):
    def test_template_has_placeholders(self):
        template = carregar_template()
        self.assertIn("{{TABELA_INTERNADOS}}", template)
        self.assertIn("{{TABELA_ALTAS}}", template)

    def test_demo_generates_synthetic_html(self):
        caminho = executar_demo()
        try:
            conteudo = caminho.read_text(encoding="utf-8")
            self.assertIn("Pessoa Fictícia A", conteudo)
            self.assertIn("Pessoa Fictícia B", conteudo)
            self.assertNotIn("{{TABELA_INTERNADOS}}", conteudo)
        finally:
            caminho.unlink(missing_ok=True)


if __name__ == "__main__":
    unittest.main()
