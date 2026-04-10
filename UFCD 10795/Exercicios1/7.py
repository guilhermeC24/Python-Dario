produto = {
    "categoria": input("Categoria do produto: "),
    "preco": float(input("Preço do produto: "))
}

match produto:
    case {"categoria": "eletrônico", "preco": p} if p > 1000:
        print("Produto de luxo")
    case {"categoria": "eletrônico", "preco": p} if p <= 1000:
        print("Produto comum")
    case {"categoria": "alimento", "preco": _}:
        print("Produto alimentar")
    case _:
        print("Categoria desconhecida")