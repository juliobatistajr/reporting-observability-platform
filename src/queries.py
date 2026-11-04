import os
import pandas as pd

from banco import conectar
from sql_reader import ler_sql


def obter_internados():

    sql = ler_sql("internados.sql")

    conexao = conectar()

    cursor = conexao.cursor()

    schema = os.getenv("ORACLE_SCHEMA")
    if schema:
        if not schema.replace("_", "").isalnum() or not schema[0].isalpha():
            raise ValueError("ORACLE_SCHEMA inválido")
        cursor.execute(f"ALTER SESSION SET CURRENT_SCHEMA = {schema.upper()}")

    df = pd.read_sql(
        sql,
        con=conexao
    )

    cursor.close()
    conexao.close()

    return df

def obter_altas():

    sql = ler_sql("altas.sql")

    conexao = conectar()

    cursor = conexao.cursor()

    schema = os.getenv("ORACLE_SCHEMA")
    if schema:
        if not schema.replace("_", "").isalnum() or not schema[0].isalpha():
            raise ValueError("ORACLE_SCHEMA inválido")
        cursor.execute(f"ALTER SESSION SET CURRENT_SCHEMA = {schema.upper()}")

    df = pd.read_sql(
        sql,
        con=conexao
    )

    cursor.close()
    conexao.close()

    return df