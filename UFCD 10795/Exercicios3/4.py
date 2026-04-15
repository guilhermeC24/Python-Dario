num = int(input("Insira um número inteiro: "))

if num < 2:
    print("Não é primo")
else:
    primo = True
    i = 2

    while i * i <= num:
        if num % i == 0:
            primo = False
            break
        i += 1

    if primo:
        print("É primo")
    else:
        print("Não é primo")