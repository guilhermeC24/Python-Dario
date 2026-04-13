num1 = int(input("Insira o 1º número: "))
num2 = int(input("Insira o 2º número: "))
num3 = int(input("Insira o 3º número: "))

menor = num1
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

maior = num1
if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3

if num1 != menor and num1 != maior:
    meio = num1
elif num2 != menor and num2 != maior:
    meio = num2
else:
    meio = num3

print("Crescente:", menor, meio, maior)
print("Decrescente:", maior, meio, menor)