import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


URL = 'https://raw.githubusercontent.com/Felipe500/Trabalho-visualizacao-de-dados/main/dados/HIST_PAINEL_COVIDBR_2022_Parte1_16mai2022.csv'
df = pd.read_csv(URL, sep=';', parse_dates=['data'])

df['casosAcumulado'] = df['casosAcumulado'].astype(int)

df['ano'] = df['data'].dt.year
df['mes'] = df['data'].dt.month
df.head()
df.describe()

colunas = df.keys()


nordeste = df.query('regiao == "Nordeste" and ano == 2022')
#veja quais os anos estão filtrados


nordeste = nordeste.replace(np.nan, 0)



#agupar valores de casos por estado, ano e mês.
dt_agrupado_nordeste = nordeste.groupby(['estado'])['casosNovos', 'obitosNovos'].sum().reset_index()



itens_estados = dt_agrupado_nordeste['estado'].unique()
print(itens_estados)

# criar uma figura para grafico de barras
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(16, 9))
ax[0].pie(dt_agrupado_nordeste['casosNovos'], labels=itens_estados, autopct='%1.2f%%', shadow=True,
          startangle=190, textprops={'fontsize': 12});
ax[1].pie(dt_agrupado_nordeste['obitosNovos'], labels=itens_estados, autopct='%1.2f%%', shadow=True,
          startangle=190,  textprops={'fontsize': 12});
ax[0].set_title('PORCENTAGEM DOS CASOS NOVOS\n REGISTRADOS NO NORDESTE EM 2022')
ax[1].set_title('PORCENTAGEM DOS OBITOS\n  REGISRADOS NO NORDESTE EM 2022')

plt.show()
