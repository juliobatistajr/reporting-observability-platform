from pathlib import Path

SQL_DIR = Path(__file__).resolve().parent.parent / "sql"


def ler_sql(nome_arquivo):
    caminho = SQL_DIR / Path(nome_arquivo).name
    return caminho.read_text(encoding="utf-8")
