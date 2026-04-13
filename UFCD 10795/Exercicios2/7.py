nota1 = int(input("Insira a 1º nota: "))
nota2 = int(input("Insira a 2º nota: "))
nota3 = int(input("Insira a 3º nota: "))

media = (nota1*2 + nota2*3 + nota3*5) / 10

print("Média:", round(media, 1))

if media >= 6:
    print("Aprovado")
if media < 6:
    print("Reprovado")