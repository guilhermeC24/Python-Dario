num = int(input("Insira um número: "))
cont = 0

for n in range(1, num + 1):
    soma = 0
    for i in range(1, n):
        if n % i == 0:
            soma += i

    if soma == n:
        cont += 1

print("Quantidade de números perfeitos:", cont)