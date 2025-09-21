import pandas as pd

caminho_arquivo = './data/games.xlsx'
df = pd.read_excel(caminho_arquivo)

# A variável 'df' guarda nossa tabela completa de jogos

# Passo 1: Ordenar a tabela inteira do maior para o menor, usando a coluna 'xxxx'
tabela_ordenada_NA = df.sort_values(by='NA_Sales', ascending=False)

tabela_ordenada_EU = df.sort_values(by='EU_Sales', ascending=False)

tabela_ordenada_JP = df.sort_values(by='JP_Sales', ascending=False)

# Passo 2: Da tabela já ordenada, pegar apenas as 10 primeiras linhas
top_10_NA = tabela_ordenada_NA.head(10)
top_10_EU = tabela_ordenada_EU.head(10)
top_10_JP = tabela_ordenada_JP.head(10)

#print(top_10)

print('---------- Top 10 Jogos na América do Norte ----------')
print(top_10_NA[['Rank', 'Name', 'Platform', 'Year', 'NA_Sales']])

print('---------- Top 10 Jogos na União Europeia ---------')
print(top_10_EU[['Rank', 'Name', 'Platform', 'Year', 'EU_Sales']])

print('---------- Top 10 Jogos no Japão ----------')
print(top_10_JP[['Rank', 'Name', 'Platform', 'Year', 'JP_Sales']])
