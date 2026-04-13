dia = input("Insira um dia da semana ('xxxx-Feira' ou 'Sábado' etc...)\nR: ")

match dia:
    case "Segunda-Feira" | "Terça-Feira" | "Quarta-Feira" | "Quinta-Feira" | "Sexta-Feira":
        print("Dia útil")
    case "Sábado" | "Domingo":
        print("Fim de semana")
    case _:
        print("Esse dia não existe ou está mal escrito.")