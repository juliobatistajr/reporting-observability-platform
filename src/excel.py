import pandas as pd

ARQUIVO_EXCEL = r"config\CONVENIOS_EMAIL.xlsx"


def carregar_parametros():

    df = pd.read_excel(
        ARQUIVO_EXCEL,
        sheet_name="Parametros"
    )

    parametros = {}

    for _, linha in df.iterrows():

        parametros[
            linha["PARAMETRO"]
        ] = linha["VALOR"]

    return parametros


def carregar_destinatarios():

    return pd.read_excel(
        ARQUIVO_EXCEL
    )


def carregar_grupos():

    df = carregar_destinatarios()

    return (
        df[
            ["CD_GRUPO_ENVIO"]
        ]
        .drop_duplicates()
        .sort_values(
            "CD_GRUPO_ENVIO"
        )
    )


def obter_convenios_grupo(
    cd_grupo_envio
):

    df = carregar_destinatarios()

    return (
        df[
            df["CD_GRUPO_ENVIO"]
            == cd_grupo_envio
        ][
            [
                "CD_CONVENIO",
                "DS_CONVENIO"
            ]
        ]
        .drop_duplicates()
        .sort_values(
            "DS_CONVENIO"
        )
    )


def obter_destinatarios_grupo(
    cd_grupo_envio
):

    df = carregar_destinatarios()

    df_grupo = df[
        df["CD_GRUPO_ENVIO"]
        == cd_grupo_envio
    ]

    to = (
        df_grupo[
            df_grupo["TIPO_DESTINO"]
            == "TO"
        ]["EMAIL"]
        .dropna()
        .unique()
        .tolist()
    )

    cc = (
        df_grupo[
            df_grupo["TIPO_DESTINO"]
            == "CC"
        ]["EMAIL"]
        .dropna()
        .unique()
        .tolist()
    )

    return to, cc