saldo = int(input("Insira o saldo: "))
cheque = int(input("Insira o cheque: "))

if cheque > saldo:
    print("Cheque não pode ser descontado")
else:
    saldo = saldo - cheque
    print("Cheque descontado, saldo atualizado:", saldo)