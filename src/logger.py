from datetime import datetime
from pathlib import Path


LOG_DIR = Path("logs")

LOG_DIR.mkdir(exist_ok=True)


def escrever_log(mensagem):

    arquivo_log = (
        LOG_DIR /
        f"{datetime.now():%Y-%m-%d}.log"
    )

    with open(
        arquivo_log,
        "a",
        encoding="utf-8"
    ) as arquivo:

        arquivo.write(
            f"{datetime.now():%d/%m/%Y %H:%M:%S} - "
            f"{mensagem}\n"
        )