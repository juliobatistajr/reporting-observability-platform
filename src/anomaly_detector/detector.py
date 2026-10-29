from historico import carregar_historico


historico = carregar_historico()

print()

print("ANÁLISE DE EXECUÇÕES")

print("=" * 50)

print(
    f"Total de execuções: "
    f"{len(historico)}"
)

if len(historico) == 0:

    print()

    print(
        "⚠ Nenhum histórico encontrado."
    )

else:

    ultima_execucao = historico[-1]

    #
    # Validação dos campos obrigatórios
    #
    campos_obrigatorios = [
        "data_execucao",
        "grupos_processados",
        "duracao_segundos",
        "status"
    ]

    campos_ausentes = []

    for campo in campos_obrigatorios:

        if campo not in ultima_execucao:

            campos_ausentes.append(
                campo
            )

    if len(campos_ausentes) > 0:

        print()

        print(
            "🚨 HISTÓRICO INVÁLIDO"
        )

        print()

        print(
            "Campos obrigatórios ausentes:"
        )

        for campo in campos_ausentes:

            print(
                f"- {campo}"
            )

        exit()

    #
    # Validação do status
    #
    status_validos = [
        "SUCESSO",
        "SUCESSO_PARCIAL",
        "FALHA"
    ]

    if ultima_execucao["status"] not in status_validos:

        print()

        print(
            "🚨 HISTÓRICO INVÁLIDO"
        )

        print()

        print(
            f"Status inválido: "
            f"{ultima_execucao['status']}"
        )

        exit()

    #
    # Validação de tipos
    #
    if not isinstance(
        ultima_execucao["grupos_processados"],
        int
    ):

        print()

        print(
            "🚨 HISTÓRICO INVÁLIDO"
        )

        print()

        print(
            "grupos_processados deve ser um número inteiro."
        )

        exit()

    if not isinstance(
        ultima_execucao["duracao_segundos"],
        (int, float)
    ):

        print()

        print(
            "🚨 HISTÓRICO INVÁLIDO"
        )

        print()

        print(
            "duracao_segundos deve ser numérico."
        )

        exit()

    #
    # Validação de valores negativos
    #
    if ultima_execucao["grupos_processados"] < 0:

        print()

        print(
            "🚨 HISTÓRICO INVÁLIDO"
        )

        print()

        print(
            "Quantidade de grupos não pode ser negativa."
        )

        exit()

    if ultima_execucao["duracao_segundos"] < 0:

        print()

        print(
            "🚨 HISTÓRICO INVÁLIDO"
        )

        print()

        print(
            "Duração da execução não pode ser negativa."
        )

        exit()

    print()

    print(
        f"Última execução: "
        f"{ultima_execucao['data_execucao']}"
    )

    print(
        f"Grupos processados: "
        f"{ultima_execucao['grupos_processados']}"
    )

    print(
        f"Duração (s): "
        f"{ultima_execucao['duracao_segundos']}"
    )

    print(
        f"Status: "
        f"{ultima_execucao['status']}"
    )

    print()

    anomalias = []

    #
    # Regra 1
    # Quantidade de grupos
    #
    if ultima_execucao["grupos_processados"] < 17:

        anomalias.append(
            "Quantidade de grupos inferior ao esperado."
        )

    #
    # Regra 2
    # Tempo de execução
    #
    if ultima_execucao["duracao_segundos"] > 120:

        anomalias.append(
            "Tempo de execução acima do esperado."
        )

    #
    # Regra 3
    # Status da execução
    #
    if ultima_execucao["status"] == "SUCESSO_PARCIAL":

        anomalias.append(
            "Execução concluída parcialmente. Alguns grupos apresentaram falha."
        )

    elif ultima_execucao["status"] == "FALHA":

        anomalias.append(
            "Falha crítica. Nenhum grupo foi processado com sucesso."
        )

    #
    # Resultado Final
    #
    if len(anomalias) == 0:

        print(
            "✅ Nenhuma anomalia detectada."
        )

    else:

        print(
            "🚨 ANOMALIA DETECTADA"
        )

        print()

        for anomalia in anomalias:

            print(
                f"- {anomalia}"
            )

    print()

    print(
        "✅ Histórico carregado com sucesso."
    )