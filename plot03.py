import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


URL = 'https://raw.githubusercontent.com/Felipe500/Trabalho-visualizacao-da-informacao/main/dados/HIST_PAINEL_COVIDBR_2022_Parte1_16mai2022.csv'
df = pd.read_csv(URL, sep=';', parse_dates=['data'])

df['casosAcumulado'] = df['casosAcumulado'].astype(int)

df['ano'] = df['data'].dt.year
df['mes'] = df['data'].dt.month


nordeste = df.query('regiao == "Nordeste" and ano == 2022')

#substuindo Nan por 0
nordeste = nordeste.replace(np.nan, 0)

#agupar valores de casos por estado, ano e mês.
dt_agrupado_nordeste = nordeste.groupby(['estado','mes'])['casosNovos', 'obitosNovos'].max().reset_index()

itens_estados = dt_agrupado_nordeste['estado'].unique()


itens_estados = dt_agrupado_nordeste['estado'].unique()
labels = ['JANEIRO', 'FEVEREIRO', 'MARCO', 'ABRIL', 'MAIO']
print(itens_estados)
# Plot time series
for estado in itens_estados:
  set_estado = dt_agrupado_nordeste.loc[dt_agrupado_nordeste['estado']==estado]
  plt.plot(set_estado['mes'], set_estado['casosNovos'], label=estado,
          linewidth=3, marker="o",  linestyle="--")

plt.title('NÚMERO DE CASOS DE COVID NOS ESTADOS DO NORDESTE EM 2022')
plt.xlabel('MESES')

plt.ylabel('N° CASOS')
plt.legend()
plt.tight_layout()
plt.show()