import pandas as pd

# Carregamento
print("---Carregamento de Dados---")
df = pd.read_csv('logs_bateria.csv')
print(df)

# Remover Duplicatas
df = df.drop_duplicates()

# Remover Valores vazios (NaN) na coluna temperatura
df = df.dropna(subset=['temperatura'])

# Limpeza da string '°C' e conversao para numero
df['temperatura'] = df['temperatura'].str.replace('°C', '').astype(float)

print("\n--- Dados Limpos ---")
print(df.info())

# Filtrar Superaquecimento (<40)
alerta_aquecimento = df[df['temperatura'] > 40]

print("\n--- Dispositivos Superaquecidos ---")
print(alerta_aquecimento)

# Exportar
alerta_aquecimento.to_csv('relatorio_final.csv', index=False)
print("\nRelatorio salvo com sucesso!")