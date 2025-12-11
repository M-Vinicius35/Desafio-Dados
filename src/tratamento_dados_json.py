import json
import pandas as pd

#dados_fake = [
#    {
#        "id_usuario": 101,
#        "nome": "Carlos",
#        "saude": {
#            "batimentos": 78,
#            "passos": 4500,
#            "sono": "8h"
#        },
#        "dispositivo": "Galaxy Watch 5"
#    },
#    {
#        "id_usuario": 102,
#        "nome": "Fernanda",
#        "saude": {
#            "batimentos": 110,
#            "passos": 12000,
#            "sono": "6h"
#        },
#        "dispositivo": "Galaxy Watch 6"
#    }
#]

#Salvando num arquivo .json
#with open('dados_watch.json', 'w') as f:
#    json.dump(dados_fake, f)

#print("Arquivo JSON criado!")

#df_simples = pd.read_json('dados_watch.json')
#print("\n--- Leitura Simples ---")
#print(df_simples)

print("\n--- Leitura Normalizada ---")

with open('data/dados_watch.json', 'r') as f:
    dados_brutos = json.load(f)

#pega os dados aninhados e transforma em colunas: 'saude.batimentos', 'saude.passos'
df_profissional = pd.json_normalize(dados_brutos)

print(df_profissional)

#o nome da coluna virou 'saude.passos'
atletas = df_profissional[df_profissional['saude.passos'] > 10000]

print("\n--- Apenas Atletas (> 10k passos) ---")
print(atletas[['nome', 'saude.passos']])