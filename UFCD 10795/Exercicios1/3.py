pedido = {"tipo": "venda", "valor": 250}

match pedido["tipo"]:
    case _ if pedido["tipo"] == "compra":
        print(f"Compra de {pedido['valor']}€")
    case _ if pedido["tipo"] == "venda":
        print(f"Venda de {pedido['valor']}€")
    case _:
        print("Pedido inválido.")
