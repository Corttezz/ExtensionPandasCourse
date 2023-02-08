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