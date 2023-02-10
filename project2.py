##Segundo exemplo de manipulação de dados usando Python Pandas
##Veremos inserção de dados, remoção de colunas, merge, gráficos
#Data 9 e 10 de fevereiro de 2023

# Importando biblioteca pandas no Python
import pandas as pd
import pandas as pd
from IPython.display import display


combustiveis_df = pd.read_excel("ca-2021-02.xlsx")
display(combustiveis_df.head())

#Inserção simples de dado
combustiveis_df['Ativo'] = True

display(combustiveis_df.head())

# Criar uma coluna "Obs" que tenha nela escrito "MELHOR CIDADE" quando a coluna Municipio for igual a SAO PAULO
combustiveis_df['Obs'] = ["MELHOR CIDADE" if municipio == 'SAO PAULO' else None for municipio in combustiveis_df['Municipio']]
display(combustiveis_df.loc[combustiveis_df['Municipio'].isin(['SAO PAULO','INDAIATUBA', 'CAMPINAS', 'SALTO']), ['Municipio', 'Obs']])

# (por Leandro Rodrigues)
# como preencher uma coluna 'Valor de Venda - Status' que verifica o seguinte:
# se o valor de venda for maior que 6,5 reais, ele fala que tá Caro..caso contrário, está barato
import numpy as np

combustiveis_df['Status do Valor de Venda'] = np.where(combustiveis_df['Valor de Venda'] > 6.5, 'Caro', 'Barato')
display(combustiveis_df[['Revenda', 'Valor de Venda', 'Status do Valor de Venda']])