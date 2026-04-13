num1 = int(input("Insira o 1º número: "))
num2 = int(input("Insira o 2º número: "))

if num1 < num2:
    print("Crescente:", num1, ",", num2)
else:
    print("Crescente:", num2, ",", num1)

if num1 > num2:
    print("Decrescente:", num1, ",", num2)
else:
    print("Decrescente:", num2, ",", num1)