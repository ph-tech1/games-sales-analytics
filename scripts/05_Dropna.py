import pandas as pd

# Chamando a tabela
caminho_arquivo = './data/games.xlsx'
df = pd.read_excel(caminho_arquivo)

# Filtrando quais plataformas por soma total das vendas e a media
vendas_por_plataforma = df.groupby('Platform')['Global_Sales'].agg(['sum', 'mean'])

# Ordenando em ordem decrescente pela coluna 'sum'
vendas_por_plataforma_ordenado = vendas_por_plataforma.sort_values(by='sum', ascending=False)

# Mostrando o resultado
print("---------- Vendas Totais e Médias por Plataforma ----------")
print(vendas_por_plataforma_ordenado)

# Remove todas as linhas que têm um valor NaN na coluna 'Year'
dataframe_limpo = df.dropna(subset=['Year'])