# Importando biblioteca pandas no Python
import pandas as pd
from IPython.display import display

combustiveis_df = pd.read_excel("ca-2021-02.xlsx")

# Usa o print para ver o dataframe!
print(combustiveis_df)

#Exibe as primeiras 5 linhas
display(combustiveis_df.head())

# Quero, na verdade, exibir as primeiras 15 linhas
display(combustiveis_df.head(15))

# Comandos dataframe.shape e dataframe.describe()
print(combustiveis_df.shape)

#describe() mostra as estatisticas mais básicas
display(combustiveis_df.describe())

# filtrar apenas por uma coluna
display(combustiveis_df["Revenda"])

#Aqui criamos um novo dataframe apenas com as colunas que eu quero

ca_df = combustiveis_df[['Revenda', 'Municipio', 'Valor de Compra']]
display(ca_df)

#Exibe a 4a. linha.
display(ca_df.loc[3])

#Exibe da 10a. linha até a 20a. linha
display(ca_df.loc[9:19])

# Criar um dataframe gas_df contendo 
# apenas as 4 colunas (Revenda, Municipio, Produto, Valor de Venda)
# somente com combustível sendo GASOLINA e exibir na tela
gas_df = ca_df.loc[ca_df['Produto'] == 'GASOLINA']
display(gas_df)

display(gas_df['Valor de Venda'].max())

#DataFrame.loc[] com múltiplas condições para filtragem
#Quais são os preços, postos que vendem ETANOL na minha cidade (INDAIATUBA) 
#ordenado do menor valor de venda para o maior
etanol_indaiatuba_df = ca_df.loc[(ca_df['Produto'] == 'ETANOL') & (ca_df['Municipio'] == 'INDAIATUBA')]
display(etanol_indaiatuba_df.sort_values(by='Valor de Venda'))

# Qual a média de preços dos combustíveis GASOLINA e GASOLINA ADITIVADA do Bairro MOOCA em SÃO PAULO?
display(combustiveis_df.loc[(combustiveis_df['Bairro'] == 'MOOCA') & (combustiveis_df['Municipio'] == 'SAO PAULO') & ((combustiveis_df['Produto'] == 'GASOLINA') | (combustiveis_df['Produto'] == 'GASOLINA ADITIVADA')), ['Valor de Venda']].mean())

# Qual a média de preços dos combustíveis GASOLINA e GASOLINA ADITIVADA do Bairro MOOCA em SÃO PAULO?
display(combustiveis_df.loc[(combustiveis_df['Bairro'] == 'MOOCA') & 
                            (combustiveis_df['Municipio'] == 'SAO PAULO') & 
                            ((combustiveis_df['Produto'] == 'GASOLINA') | (combustiveis_df['Produto'] == 'GASOLINA ADITIVADA')), 
                            ['Valor de Venda']].mean())

# Qual a média de preços dos combustíveis GASOLINA e GASOLINA ADITIVADA do Bairro MOOCA em SÃO PAULO?
display(combustiveis_df.loc[(combustiveis_df['Bairro'] == 'MOOCA') & 
                            (combustiveis_df['Municipio'] == 'SAO PAULO') & 
                            (combustiveis_df['Produto'].isin(["GASOLINA", "GASOLINA ADITIVADA"])), 
                            ['Valor de Venda']].mean())

# Como mostrar média de valor de venda POR COMBUSTÍVEL Brasil todo?
media_por_combustivel_df = ca_df[['Produto', 'Valor de Venda']].groupby(by='Produto').mean().round(2)
display(media_por_combustivel_df)

# Quero adicionar uma coluna de valor booleano no combustiveis_df
# chamada "Ativo" que, por padrão, vai ser True para 
# TODAS as linhas
combustiveis_df['Ativo'] = True
print(combustiveis_df.info())
display(combustiveis_df.head())

# Exportar para Excel o dataframe com etanol em Indaiatuba....
etanol_indaiatuba_df.to_excel('etanol_indaiatuba.xlsx', sheet_name='Etanol em Indaiatuba')