import oracledb

oracledb.init_oracle_client(
    lib_dir=r"C:\Users\julio.junior1\Downloads\instantclient-basic-windows.x64-23.26.3.0.0\instantclient_23_26"
)

from oracle_config import (
    USUARIO,
    SENHA,
    HOST,
    PORTA,
    SERVICO
)


def conectar():

    dsn = f"{HOST}:{PORTA}/{SERVICO}"

    conexao = oracledb.connect(
        user=USUARIO,
        password=SENHA,
        dsn=dsn
    )

    return conexao