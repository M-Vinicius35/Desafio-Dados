import json
import random

dados_streaming = []

planos = [
    {"tipo": "Básico", "preco": 25.90, "telas": 1},
    {"tipo": "Padrão", "preco": 39.90, "telas": 2},
    {"tipo": "Premium", "preco": 55.90, "telas": 4}
]

nomes = ["João", "Maria", "Pedro", "Ana", "Lucas", "Carla", "Beatriz", "Felipe"]

for i in range(1, 21):
    plano_escolhido = random.choice(planos)
    usuario = {
        "id": i,
        "nome": random.choice(nomes),
        "pais": "Brasil",
        "detalhes_assinatura": {
            "plano": plano_escolhido["tipo"],
            "valor_mensal": plano_escolhido["preco"],
            "qtd_telas": plano_escolhido["telas"],
            "status": random.choice(["Ativo", "Ativo", "Cancelado"])
        }
    }
    dados_streaming.append(usuario)

with open('assinantes.json', 'w') as f:
    json.dump(dados_streaming, f)

print("Ficheiro 'assinantes.json' gerado!")