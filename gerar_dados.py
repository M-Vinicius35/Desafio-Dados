import pandas as pd
import numpy as np

# Simulando dados sujos que viriam de sensores
dados = {
    'id_dispositivo': ['S23_001', 'A54_992', 'S23_001', 'ZFold_55', 'S23_002', 'A14_111'],
    'status': ['Normal', 'Critical', 'Normal', 'Normal', 'Critical', 'Low'],
    'temperatura': ['35.5', '42.1°C', '35.5', '39.0', '45.2°C', None], # Note o "°C" e o valor vazio
    'nivel_bateria': [80, 15, 80, 60, 5, 12] # Note que a linha 1 e 3 são duplicadas
}

df = pd.DataFrame(dados)
df.to_csv('logs_bateria.csv', index=False)

print("Arquivo 'logs_bateria.csv' gerado com sucesso! Agora comece o desafio.")