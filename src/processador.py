from queries import obter_internados
from queries import obter_altas


def obter_dados_convenio(convenio):

    df_internados = obter_internados()

    df_altas = obter_altas()

    internados = df_internados[
        df_internados["CONVENIO"] == convenio
    ]

    altas = df_altas[
        df_altas["CONVENIO"] == convenio
    ]

    return internados, altas