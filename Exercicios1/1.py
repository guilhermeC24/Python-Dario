var1 = input("Insira um dia da semana ('xxxx-Feira' ou 'Sábado' etc...)\nR: ")

match var1:
    case "Segunda-Feira":
        print("Dia útil")
    case "Terça-Feira":
        print("Dia útil")
    case "Quarta-Feira":
        print("Dia útil")
    case "Quinta-Feira":
        print("Dia útil")
    case "Sexta-Feira":
        print("Dia útil")
    case "Sábado":
        print("Fim de semana")
    case "Domingo":
        print("Fim de semana")
    case _:
        print("Esse dia não existe ou está mal escrito.")