from datetime import datetime

from excel import (
    carregar_grupos,
    obter_convenios_grupo,
    obter_destinatarios_grupo
)

from processador import (
    obter_dados_convenio
)

from email_builder import (
    gerar_html_convenio,
    gerar_html_grupo
)

from email_sender import (
    enviar_email
)

from logger import (
    escrever_log
)

from lock_manager import (
    lock_existe,
    criar_lock,
    remover_lock
)

from anomaly_detector.historico import (
    salvar_execucao
)

inicio_execucao = datetime.now()

#
# LOCK DE EXECUÇÃO
#
if lock_existe():

    print(
        "🚫 Processo já está em execução."
    )

    exit()

criar_lock()

try:

    print("Iniciando processamento DEV...")

    escrever_log("=" * 60)
    escrever_log("INÍCIO DA EXECUÇÃO")
    escrever_log("=" * 60)

    grupos = carregar_grupos()

    total_grupos = 0
    total_erros = 0

    for _, grupo in grupos.iterrows():

        cd_grupo = grupo["CD_GRUPO_ENVIO"]

        try:

            print()
            print("=" * 80)

            print(
                f"Processando Grupo {cd_grupo}"
            )

            escrever_log(
                f"Grupo {cd_grupo} - Iniciado"
            )

            convenios = obter_convenios_grupo(
                cd_grupo
            )

            blocos_html = []

            for _, linha in convenios.iterrows():

                convenio = linha["DS_CONVENIO"]

                print(
                    f"   Convênio: {convenio}"
                )

                internados, altas = (
                    obter_dados_convenio(
                        convenio
                    )
                )

                html_convenio = (
                    gerar_html_convenio(
                        convenio,
                        internados,
                        altas
                    )
                )

                blocos_html.append(
                    html_convenio
                )

            html_final = gerar_html_grupo(
                blocos_html
            )

            assunto = (
                f"[DEV] Relatório Operacional "
                f"- Grupo {cd_grupo} "
                f"- {datetime.now():%d/%m/%Y}"
            )

            #
            # DEV
            #
            to = [
                "empresa@destino.com.br"
            ]

            cc = []

            enviar_email(
                to,
                cc,
                assunto,
                html_final
            )

            total_grupos += 1

            escrever_log(
                f"Grupo {cd_grupo} - SUCESSO"
            )

        except Exception as erro:

            escrever_log(
                f"Grupo {cd_grupo} - ERRO - {erro}"
            )

            print(
                f"Erro Grupo {cd_grupo}: {erro}"
            )

            total_erros += 1

    escrever_log(
        f"Grupos Processados: {total_grupos}"
    )

    escrever_log(
        "FIM DA EXECUÇÃO"
    )

    escrever_log("=" * 60)

    #
    # Define o status final da execução
    #
    status_execucao = "SUCESSO"

    if total_grupos > 0 and total_erros > 0:

        status_execucao = "SUCESSO_PARCIAL"

    elif total_grupos == 0 and total_erros > 0:

        status_execucao = "FALHA"

    salvar_execucao(
        {
            "data_execucao":
                datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),

            "grupos_processados":
                total_grupos,

            "duracao_segundos":
                int(
                    (
                        datetime.now()
                        -
                        inicio_execucao
                    ).total_seconds()
                ),

            "status":
                status_execucao
        }
    )

    print()

    print(
        f"✅ Grupos processados: "
        f"{total_grupos}"
    )

    print(
        f"✅ Status final: "
        f"{status_execucao}"
    )

    print(
        "✅ Processamento concluído."
    )

finally:

    remover_lock()