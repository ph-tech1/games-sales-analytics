import pandas as pd

caminho_arquivo = './data/games.xlsx'
df = pd.read_excel(caminho_arquivo)

print("---------- Visualização das 5 Primeiras Linhas ----------")
print(df.head())
print("\n" + "="*50 + "\n") # Apenas para separar as seções

print("---------- Informações Gerais do DataFrame ----------")
df.info()
print("\n" + "="*50 + "\n") 

print("---------- Estatísticas Descritivas dos Dados Numéricos ----------")
print(df.describe())