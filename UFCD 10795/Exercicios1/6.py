dados = {
    "status": input("Status do servidor ('ok'/'erro'): "),
    "tempo_resposta": int(input("Tempo de resposta (ms): "))
}

match dados:
    case {"status": "ok", "tempo_resposta": t} if t > 200:
        print("Servidor lento")
    case {"status": "ok", "tempo_resposta": _}:
        print("Servidor ativo")
    case {"status": "erro", "tempo_resposta": _}:
        print("Servidor indisponível")
    case _:
        print("Estado desconhecido")