from datetime import datetime

from html_service import carregar_template


def gerar_html_convenio(
    convenio,
    df_internados,
    df_altas
):

    html = carregar_template()

    #
    # INTERNADOS
    #
    if len(df_internados) > 0:

        df_internados_html = (
            df_internados[
                [
                    "SETOR",
                    "PACIENTE",
                    "PRONTUARIO",
                    "ATENDIMENTO",
                    "DATA_ATENDIMENTO",
                    "MATRICULA",
                    "MEDICO",
                    "LEITO"
                ]
            ]
            .rename(
                columns={
                    "SETOR": "Setor",
                    "PACIENTE": "Paciente",
                    "PRONTUARIO": "Prontuário",
                    "ATENDIMENTO": "Atendimento",
                    "DATA_ATENDIMENTO": "Entrada",
                    "MATRICULA": "Carteirinha",
                    "MEDICO": "Médico",
                    "LEITO": "Leito"
                }
            )
        )

        tabela_internados = df_internados_html.to_html(
            index=False
        )

    else:

        tabela_internados = """
        <p>
        Não há pacientes internados para o convênio nesta data.
        </p>
        """

    #
    # ALTAS
    #
    if len(df_altas) > 0:

        df_altas_html = (
            df_altas[
                [
                    "SETOR",
                    "PACIENTE",
                    "PRONTUARIO",
                    "ATENDIMENTO",
                    "DATA_ATENDIMENTO",
                    "DATA_ALTA",
                    "MATRICULA",
                    "MEDICO_ESPECIALIDADE",
                    "TIPO_ALTA",
                    "LEITO"
                ]
            ]
            .rename(
                columns={
                    "SETOR": "Setor",
                    "PACIENTE": "Paciente",
                    "PRONTUARIO": "Prontuário",
                    "ATENDIMENTO": "Atendimento",
                    "DATA_ATENDIMENTO": "Entrada",
                    "DATA_ALTA": "Alta",
                    "MATRICULA": "Carteirinha",
                    "MEDICO_ESPECIALIDADE": "Médico / Especialidade",
                    "TIPO_ALTA": "Motivo Alta",
                    "LEITO": "Leito"
                }
            )
        )

        tabela_altas = df_altas_html.to_html(
            index=False
        )

    else:

        tabela_altas = """
        <p>
        Não há pacientes com alta para o convênio nesta data.
        </p>
        """

    html = html.replace(
        "{{CONVENIO}}",
        convenio
    )

    html = html.replace(
        "{{TABELA_INTERNADOS}}",
        tabela_internados
    )

    html = html.replace(
        "{{TABELA_ALTAS}}",
        tabela_altas
    )

    html = html.replace(
        "{{DATA_GERACAO}}",
        datetime.now().strftime(
            "%d/%m/%Y %H:%M"
        )
    )

    return html


def gerar_html_grupo(
    blocos_html
):

    html_final = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Censo Convênios</title>
    </head>
    <body>
    """

    for indice, bloco in enumerate(blocos_html):

        html_final += bloco

        if indice < len(blocos_html) - 1:

            html_final += """
            <br>
            <hr>
            <br>
            """

    html_final += """
    </body>
    </html>
    """

    return html_final