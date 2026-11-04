"""Demonstração offline: gera HTML com dados inteiramente fictícios.

Não conecta ao Oracle nem envia e-mails.
"""
from pathlib import Path

import pandas as pd

from src.email_builder import gerar_html_convenio, gerar_html_grupo


def executar_demo():
    internados = pd.DataFrame([{
        "SETOR": "Setor Exemplo", "PACIENTE": "Pessoa Fictícia A",
        "PRONTUARIO": "DEMO-001", "ATENDIMENTO": "AT-001",
        "DATA_ATENDIMENTO": "2026-01-01", "MATRICULA": "EX-100",
        "MEDICO": "Profissional Exemplo", "LEITO": "A-01",
    }])
    altas = pd.DataFrame([{
        "SETOR": "Setor Exemplo", "PACIENTE": "Pessoa Fictícia B",
        "PRONTUARIO": "DEMO-002", "ATENDIMENTO": "AT-002",
        "DATA_ATENDIMENTO": "2026-01-02", "DATA_ALTA": "2026-01-03",
        "MATRICULA": "EX-200", "MEDICO_ESPECIALIDADE": "Profissional / Área",
        "TIPO_ALTA": "Concluído", "LEITO": "A-02",
    }])

    bloco = gerar_html_convenio("Grupo Demonstrativo", internados, altas)
    html = gerar_html_grupo([bloco])
    destino = Path(__file__).resolve().parent / "output" / "demo_report.html"
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(html, encoding="utf-8")
    print(f"Relatório demonstrativo gerado em: {destino}")
    return destino


if __name__ == "__main__":
    executar_demo()
