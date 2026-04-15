num = int(input("Insira um número: "))
div = 0

for i in range(1, num + 1):
    if num % i == 0:
        div += 1

print("Número de divisores:", div)