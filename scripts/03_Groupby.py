import pandas as pd

caminho_arquivo = './data/games.xlsx'
df = pd.read_excel(caminho_arquivo)

# 1. Agrupar por 'Genre'.
# 2. Selecionar a coluna que queremos calcular ('Global_Sales').
# 3. Aplicar a função de soma (.sum()).

# Agrupa o dataframe pela coluna 'X'
# e calcula a SOMA da coluna 'Y' para cada grupo
# dataframe.groupby('coluna_para_agrupar')['coluna_para_calcular'].sum()
vendas_por_genero = df.groupby('Genre')['Global_Sales'].sum()

# Para visualizar melhor, vamos ordenar o resultado
vendas_por_genero_ordenado = vendas_por_genero.sort_values(ascending=False)

print("---------- Total de Vendas Globais por Gênero ----------")
print(vendas_por_genero_ordenado)