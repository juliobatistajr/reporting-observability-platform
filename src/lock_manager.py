from pathlib import Path

ARQUIVO_LOCK = Path(__file__).resolve().parent.parent / "output" / "processo.lock"


def lock_existe():
    return ARQUIVO_LOCK.exists()


def criar_lock():
    ARQUIVO_LOCK.parent.mkdir(parents=True, exist_ok=True)
    ARQUIVO_LOCK.touch(exist_ok=True)


def remover_lock():
    if ARQUIVO_LOCK.exists():
        ARQUIVO_LOCK.unlink()
