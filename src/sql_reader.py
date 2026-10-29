def ler_sql(nome_arquivo):

    caminho = f"sql/{nome_arquivo}"

    with open(
        caminho,
        "r",
        encoding="utf-8"
    ) as arquivo:

        return arquivo.read()