import matplotlib.pyplot as plt
import datetime
import numpy as np
import pandas as pd



df = pd.read_csv('dados/HIST_PAINEL_COVIDBR_2022_Parte1_16mai2022.csv', sep=';', parse_dates=['data'])
df['casosAcumulado'] = df['casosAcumulado'].astype(int)

df['ano'] = df['data'].dt.year
df['mes'] = df['data'].dt.month

colunas = df.keys()


nordeste = df.query('regiao == "Nordeste" and ano == 2022')



#substuindo Nan por 0
nordeste = nordeste.replace(np.nan, 0)



#agupar valores de casos por estado, ano e mês.
dt_agrupado_nordeste = nordeste.groupby(['estado','mes'])['casosNovos', 'obitosNovos'].max().reset_index()
dt_agrupado_nordestsum = nordeste.groupby(['estado'])['casosNovos', 'obitosNovos'].sum().reset_index()



itens_estados = dt_agrupado_nordeste['estado'].unique()






# Convert data frame
piaui = dt_agrupado_nordeste.loc[dt_agrupado_nordeste['estado']=='CE']

df1=piaui['casosNovos']
df2=piaui['mes']
#df1.query('estado == PI')
print(df1)
df = pd.DataFrame({'date': np.array([datetime.datetime(2021,
                    12, i+1) for i in range(20)]),
                   'blogs_read': [4, 6, 5, 8, 15, 13, 18, 6, 5,
                  3, 15, 14, 19, 21, 15, 19, 25, 24, 16, 26]})

df = pd.DataFrame({'date': np.array([datetime.datetime(2021,
                     12, i+1)
 for i in range(20)]),
                   'blogs_unread': [1, 1, 2, 3, 3, 3, 4, 3, 2,
                    3, 4, 7, 5, 3, 2, 4, 3, 6, 1, 2]})

itens_estados = dt_agrupado_nordeste['estado'].unique()
labels = ['JANEIRO', 'FEVEREIRO', 'MARCO', 'ABRIL', 'MAIO']
print(itens_estados)
# Plot time series
for estado in itens_estados:
  set_estado = dt_agrupado_nordeste.loc[dt_agrupado_nordeste['estado']==estado]
  plt.plot(set_estado['mes'], set_estado['casosNovos'], label=estado,
          linewidth=3, marker="o",  linestyle="--")
  #plt.plot.set_xticks(set_estado['mes'], labels)

# Add title and labels

plt.title('NÚMERO DE CASOS DE COVID NOS ESTADOS DO NORDESTE EM 2022')
plt.xlabel('MESES')

plt.ylabel('N° CASOS')

# Add legend

plt.legend()

# Auto space

plt.tight_layout()

# Display plot

plt.show()