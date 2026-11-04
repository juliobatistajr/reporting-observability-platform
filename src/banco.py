import os
import oracledb

from oracle_config import USUARIO, SENHA, HOST, PORTA, SERVICO


def conectar():
    """Conecta ao Oracle com credenciais definidas no .env local."""
    obrigatorios = {
        "ORACLE_USER": USUARIO,
        "ORACLE_PASSWORD": SENHA,
        "ORACLE_HOST": HOST,
        "ORACLE_PORT": PORTA,
        "ORACLE_SERVICE": SERVICO,
    }
    ausentes = [chave for chave, valor in obrigatorios.items() if not valor]
    if ausentes:
        raise ValueError("Configuração Oracle ausente: " + ", ".join(ausentes))

    # Thin mode funciona sem Instant Client. Thick mode é opcional.
    instant_client = os.getenv("ORACLE_CLIENT_LIB_DIR")
    if instant_client and oracledb.is_thin_mode():
        oracledb.init_oracle_client(lib_dir=instant_client)

    dsn = f"{HOST}:{PORTA}/{SERVICO}"
    return oracledb.connect(user=USUARIO, password=SENHA, dsn=dsn)
