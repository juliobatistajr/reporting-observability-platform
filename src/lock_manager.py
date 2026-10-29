from pathlib import Path


ARQUIVO_LOCK = Path(
    "output/processo.lock"
)


def lock_existe():

    return ARQUIVO_LOCK.exists()


def criar_lock():

    ARQUIVO_LOCK.touch()


def remover_lock():

    if ARQUIVO_LOCK.exists():

        ARQUIVO_LOCK.unlink()