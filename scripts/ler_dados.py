# ----------------------------------------------------------------
# Documentação do Módulo
# ----------------------------------------------------------------
# Objetivo:
#   Este script é o ponto de partida do projeto 'games-sales-analytics'.
#   Ele é responsável por carregar o conjunto de dados de vendas de jogos
#   e realizar uma exploração inicial para entender sua estrutura.
#
# Funcionalidades:
#   1. Carrega os dados de um arquivo Excel para um DataFrame do Pandas.
#   2. Exibe as 5 primeiras linhas do DataFrame.
#   3. Mostra um resumo técnico do DataFrame (tipos de dados, valores nulos).
#   4. Apresenta as principais estatísticas descritivas das colunas numéricas.
# ----------------------------------------------------------------

# Passo 1: Importar a biblioteca Pandas
# O 'import pandas as pd' é uma convenção. Estamos importando a biblioteca
# e dando a ela um "apelido" mais curto, 'pd', para facilitar a escrita do código.
import pandas as pd

# Passo 2: Carregar os dados do arquivo Excel
# Vamos usar a função 'read_excel' do Pandas para ler nosso arquivo.
# O caminho '../data/games.xlsx' significa:
#   '../' -> "volte uma pasta" (da pasta /scripts para a raiz do projeto)
#   'data/' -> "entre na pasta data"
#   'games.xlsx' -> "leia este arquivo"
# O resultado (nossa tabela de dados) será armazenado na variável 'df' (DataFrame).
caminho_arquivo = './data/games.xlsx'
df = pd.read_excel(caminho_arquivo)

# Passo 3: Explorar os dados com as funções principais
# Usamos 'print()' para mostrar os resultados no terminal.

# --- .head() ---
# Mostra as primeiras 5 linhas do DataFrame. É ótimo para ter uma
# visão rápida das colunas e do formato dos dados.
print("---------- Visualização das 5 Primeiras Linhas ----------")
print(df.head())
print("\n" + "="*50 + "\n") # Apenas para separar as seções

# --- .info() ---
# Fornece um resumo técnico do DataFrame. Mostra o número de linhas,
# as colunas, a quantidade de valores não-nulos em cada uma e o tipo
# de dado (ex: número, texto, data). É fundamental para identificar
# dados faltantes!
print("---------- Informações Gerais do DataFrame ----------")
df.info()
print("\n" + "="*50 + "\n") # Apenas para separar as seções

# --- .describe() ---
# Gera estatísticas descritivas para as colunas numéricas.
# Inclui contagem, média, desvio padrão, valor mínimo, máximo e
# os quartis. Ajuda a entender a distribuição e a escala dos dados.
print("---------- Estatísticas Descritivas dos Dados Numéricos ----------")
print(df.describe())