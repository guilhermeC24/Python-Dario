i = 0

while i <= 255:
    print(i)
    i += 1

    if i % 20 == 0:
        op = input("Continuar? (s/n): ")
        if op == "n":
            break