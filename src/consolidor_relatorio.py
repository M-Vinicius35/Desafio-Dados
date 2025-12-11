import pandas as pd
import glob

print("--- Iniciando Consolidação ---")

#Listar todos os arquivos que começam com 'vendas_' e terminam com '.csv'
#O asterisco (*) significa "qualquer coisa aqui no meio"
lista_arquivos = glob.glob('data/vendas_*.csv')

print(f"Arquivos encontrados: {len(lista_arquivos)}")

#Criar uma lista vazia para guardar as tabelas
tabelas_lidas = []

#Loop para cada arquivo da pasta
for arquivo in lista_arquivos:
    print(f"Lendo: {arquivo}...")
    
    #Lê o arquivo atual
    df_temp = pd.read_csv(arquivo)
    
    #Criar uma coluna dizendo de qual arquivo veio
    #ajuda a rastrear erros depois
    df_temp['origem_arquivo'] = arquivo
    
    #Adiciona na lista
    tabelas_lidas.append(df_temp)

#Concatenar
#pd.concat é mais rápido do que ficar juntando uma por uma dentro do loop
print("Juntando tudo...")
df_final = pd.concat(tabelas_lidas, ignore_index=True)

#Visualizar e Salvar
print("\n--- Relatório Final Consolidado ---")
print(df_final)

df_final.to_excel('output/Relatorio_Mensal.xlsx', index=False)
print("\nArquivo 'Relatorio_Mensal.xlsx' gerado com sucesso!")