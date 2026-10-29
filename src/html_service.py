def carregar_template():

    with open(
        "templates/email_template.html",
        "r",
        encoding="utf-8"
    ) as arquivo:

        return arquivo.read()