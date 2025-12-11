import pandas as pd
import json

with open('assinantes.json', 'r') as f:
    dados_brutos = json.load(f)
    
df = pd.json_normalize(dados_brutos)

# Filtrar apenas ass ativas
df_ativos = df[df['detalhes_assinatura.status'] == 'Ativo']

# Filtrar apenas ass Premium
df_premium = df_ativos[df_ativos['detalhes_assinatura.plano'] == 'Premium']

# Calcular o Faturamento Total
total_faturamento = df_premium['detalhes_assinatura.valor_mensal'].sum()

print(f"\n--- Resultado da Analise ---")
print(f"Utilizadores Premium ativos: {len(df_premium)}")
print(f"Faturamento Mensal (Premium): R$ {total_faturamento:.2f}")

# Exportar para o Excel
colunas_finais = ['nome', 'detalhes_assinatura.plano', 'detalhes_assinatura.valor_mensal']
df_premium[colunas_finais].to_excel('Faturamento_premium.xlsx', index=False)

print("\nRealatorio Excel gerado com sucesso")