import pandas as pd

# Chamando a tabela
caminho_arquivo = './data/games.xlsx'
df = pd.read_excel(caminho_arquivo)

# --- Limpeza dos Dados ---
# 1. Criamos um DataFrame limpo removendo as linhas onde o ano é nulo
df_limpo = df.dropna(subset=['Year'])

# 2. Na cópia limpa, convertemos a coluna 'Year' para inteiro
df_limpo['Year'] = df_limpo['Year'].astype(int)

# --- Análise com os Dados Limpos ---
# Agora usamos 'df_limpo' para a análise
vendas_por_ano = df_limpo.groupby('Year')['Global_Sales'].sum()
vendas_por_ano_ordenado = vendas_por_ano.sort_values(ascending=False)

print("---------- Ranking de Vendas Globais por Ano ----------")
print(vendas_por_ano_ordenado)

# Dica Bônus: Para ver apenas o ano campeão
print("\nO ano de ouro dos games foi:", vendas_por_ano_ordenado.index[0])