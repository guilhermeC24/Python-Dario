cliente = "João"
compra = int(input("Insira o valor da compra: "))

desconto = 0

if compra <= 200:
    desconto = compra * 0.10
if compra > 200 and compra <= 500:
    desconto = compra * 0.15
if compra > 500:
    desconto = compra * 0.20

total = compra - desconto

print("Nome:", cliente)
print("Compra:", f"{compra:.2f}€")
print("Desconto:", f"{desconto:.2f}€")
print("Total a pagar:", f"{total:.2f}€")