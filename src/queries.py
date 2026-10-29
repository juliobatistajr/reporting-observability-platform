import pandas as pd

from banco import conectar
from sql_reader import ler_sql


def obter_internados():

    sql = ler_sql("internados.sql")

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        ALTER SESSION SET CURRENT_SCHEMA = TASY
    """)

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

    cursor.execute("""
        ALTER SESSION SET CURRENT_SCHEMA = TASY
    """)

    df = pd.read_sql(
        sql,
        con=conexao
    )

    cursor.close()
    conexao.close()

    return df