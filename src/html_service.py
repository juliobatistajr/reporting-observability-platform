from pathlib import Path

TEMPLATE_PATH = Path(__file__).resolve().parent.parent / "templates" / "email_template.html"


def carregar_template():
    return TEMPLATE_PATH.read_text(encoding="utf-8")
