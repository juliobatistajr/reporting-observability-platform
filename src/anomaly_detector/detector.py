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
    if ultima_execucao["status"] != "SUCESSO":

        anomalias.append(
            "A execução apresentou falhas."
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