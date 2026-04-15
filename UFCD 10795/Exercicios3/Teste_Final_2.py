clientes = []
numcli = 1

op = 0

while op != 4:
    print("\n1 - Inserir cliente")
    print("2 - Listar clientes")
    print("3 - Procurar cliente")
    print("4 - Sair")

    op = int(input("Opção: "))

    #INSERIR CLIENTE
    if op == 1:

        #validar nome
        nome = input("Nome: ")
        while nome.strip() == "":
            nome = input("Nome inválido. Nome: ")

        #validar morada
        morada = input("Morada: ")
        while morada.strip() == "":
            morada = input("Morada inválida. Morada: ")

        #validar tlf
        tel = input("Telefone: ")
        while not tel.isdigit():
            tel = input("Telefone inválido. Telefone: ")

        #validar nif
        nif = input("NIF: ")
        while not (nif.isdigit() and len(nif) == 9):
            nif = input("NIF inválido (9 dígitos). NIF: ")

        #validar compra
        compra = float(input("Valor da compra: "))
        while compra < 0:
            compra = float(input("Valor inválido. Valor da compra: "))

        #calcular dívida final (sem função)
        if compra >= 100 and compra <= 200:
            desconto = compra * 0.05
        elif compra > 200 and compra < 500:
            desconto = compra * 0.10
        elif compra >= 500:
            desconto = compra * 0.15
        else:
            desconto = 0

        divfin = compra - desconto

        #criar cliente
        cliente = [numcli, nome, morada, tel, nif, compra, divfin]
        clientes.append(cliente)

        print("Cliente inserido com nº:", numcli)
        numcli += 1

    #LISTAR CLIENTES
    elif op == 2:

        #percorrer todos os clientes
        for c in clientes:
            print("\nNº:", c[0])
            print("Nome:", c[1])
            print("Morada:", c[2])
            print("Tel:", c[3])
            print("NIF:", c[4])
            print("Compra:", c[5])
            print("Divida Final:", c[6])

            #pausar cliente a cliente
            op2 = input("Continuar? (s/n): ")
            if op2 == "n":
                break

    #PROCURAR CLIENTE
    elif op == 3:

        #validar num do cliente
        n = input("Número do cliente: ")
        while not n.isdigit():
            n = input("Número inválido. Número do cliente: ")
        n = int(n)

        #procurar no vetor
        encontrado = False
        for c in clientes:
            if c[0] == n:
                print("\nNº:", c[0])
                print("Nome:", c[1])
                print("Morada:", c[2])
                print("Tel:", c[3])
                print("NIF:", c[4])
                print("Compra:", c[5])
                print("Divida Final:", c[6])
                encontrado = True
                break

        if not encontrado:
            print("Cliente não encontrado")

    elif op == 4:
        print("A sair..")

    else:
        print("Opção inválida.")