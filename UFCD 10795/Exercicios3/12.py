num = int(input("Insira um número: "))
cont = 0

for i in range(1, num):
    print(num, "+", i, "=", num + i)
    print(num, "-", i, "=", num - i)
    print(num, "*", i, "=", num * i)
    print(num, "/", i, "=", num / i)
    cont += 4

print("Total de operações:", cont)