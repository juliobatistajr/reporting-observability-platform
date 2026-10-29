import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

ARQUIVO_HISTORICO = (
    BASE_DIR /
    "historico_execucoes.json"
)


def carregar_historico():

    if not ARQUIVO_HISTORICO.exists():

        return []

    with open(
        ARQUIVO_HISTORICO,
        "r",
        encoding="utf-8"
    ) as arquivo:

        return json.load(
            arquivo
        )


def salvar_execucao(
    registro
):

    historico = carregar_historico()

    historico.append(
        registro
    )

    with open(
        ARQUIVO_HISTORICO,
        "w",
        encoding="utf-8"
    ) as arquivo:

        json.dump(
            historico,
            arquivo,
            indent=4,
            ensure_ascii=False
        )