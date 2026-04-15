op = 0

while op != 3:
    print("\n1 - Analisar números")
    print("2 - Calculadora")
    print("3 - Sair")
    op = int(input("Opção: "))

    #1
    if op == 1:
        num = int(input("Insira um número de 1 a 30000: "))

        while num < 1 or num > 30000:
            num = int(input("Valor inválido. Insira de 1 a 30000: "))

        cont = 0

        for n in range(num, 0, -1):
            print("\nNúmero:", n)

            #divisores
            div = 0
            soma = 0

            for i in range(1, n + 1):
                if n % i == 0:
                    div += 1
                    if i != n:
                        soma += i

            print("Divisores:", div)

            #primo
            if div == 2:
                print("É primo")
            else:
                print("Não é primo")

            #perfeito
            if soma == n:
                print("É perfeito")
            else:
                print("Não é perfeito")

            cont += 1

            if cont % 10 == 0:
                op2 = input("Continuar? (s/n): ")
                if op2 == "n":
                    break

    #2
    elif op == 2:
        op_calc = input("Operação ( + , - , * , / , tabuada ): ")

        if op_calc == "tabuada":
            num = int(input("Número da tabuada de 1 a 1000: "))

            while num < 1 or num > 1000:
                num = int(input("Valor inválido: "))

            cont = 0

            for a in range(1, num + 1):
                for b in range(1, num + 1):
                    print(a, "x", b, "=", a * b)
                    cont += 1

                    if cont % 20 == 0:
                        op3 = input("Continuar? (s/n): ")
                        if op3 == "n":
                            break
                else:
                    continue
                break

        else:
            a = float(input("Primeiro número: "))
            b = float(input("Segundo número: "))

            if op_calc == "+":
                print("Resultado:", a + b)
            elif op_calc == "-":
                print("Resultado:", a - b)
            elif op_calc == "*":
                print("Resultado:", a * b)
            elif op_calc == "/":
                print("Resultado:", a / b)