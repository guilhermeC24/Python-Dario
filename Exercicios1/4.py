valor = input("Insira um valor (Ex: 1 ou 1.5):\nR: ")

match valor:
    case _ if valor.isdigit():
        print("Número inteiro")
    case _ if valor.replace(".", "", 1).isdigit():
        print("Número decimal")
    case _:
        print("Valor inválido.")
