cont = 0
soma = 0

while cont < 30:
    num = int(input("Insira o número par de 1 a 50: "))

    if num >= 1 and num <= 50 and num % 2 == 0:
        soma += num
        cont += 1

media = soma / 30
print("Média:", media)