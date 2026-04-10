var1 = int(input("Insira uma nota (0-100)\nR: "))

match var1:
    case _ if var1 > -1 and var1 < 50:
        print("Insuficiente")
    case _ if var1 > 49 and var1 < 70:
        print("Suficiente")
    case _ if var1 > 69 and var1 < 90:
        print("Bom")
    case _ if var1 > 89:
        print("Excelente")
    case _:
        print("Valor inválido ou não está no intervalo 0-100.")