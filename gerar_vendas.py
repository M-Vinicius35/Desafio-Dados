import pandas as pd
import numpy as np

# Criando 5 arquivos de vendas
for i in range(1, 6):
    dados = {
        'data': [f'2025-01-0{i}'],
        'produto': ['Celular Samsung'],
        'valor': [np.random.randint(1000, 5000)], # Valor aleatório
        'loja': ['Amazonas Shopping']
    }
    df = pd.DataFrame(dados)
    nome_arquivo = f'vendas_dia_{i}.csv'
    df.to_csv(nome_arquivo, index=False)
    print(f"Criado: {nome_arquivo}")