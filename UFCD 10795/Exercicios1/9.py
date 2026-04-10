req = {
    "metodo": input("Método (GET/POST): "),
    "conteudo": input("Conteúdo da requisição: ")
}

match req:
    case {"metodo": "GET", "conteudo": _}:
        print("Requisição GET recebida")
    case {"metodo": "POST", "conteudo": c} if c != "":
        print("Requisição POST com dados válidos")
    case {"metodo": "POST", "conteudo": ""}:
        print("Requisição POST sem dados")
    case _:
        print("Método não suportado")
