cont = 0
num = 2

while cont < 10:
    primo = True
    i = 2

    while i * i <= num:
        if num % i == 0:
            primo = False
            break
        i += 1

    if primo:
        print(num)
        cont += 1

    num += 1