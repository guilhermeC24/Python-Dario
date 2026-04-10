nota = int(input("Insira uma nota (0-100)\nR: "))

match nota:
    case _ if nota > -1 and nota < 50:
        print("Insuficiente")
    case _ if nota > 49 and nota < 70:
        print("Suficiente")
    case _ if nota > 69 and nota < 90:
        print("Bom")
    case _ if nota > 89:
        print("Excelente")
    case _:
        print("Valor inválido ou não está no intervalo 0-100.")