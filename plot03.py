import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np


df = pd.read_csv('dados/HIST_PAINEL_COVIDBR_2022_Parte1_16mai2022.csv', sep=';', parse_dates=['data'])
df.head()

df['casosAcumulado'] = df['casosAcumulado'].astype(int)

df['ano'] = df['data'].dt.year
df['mes'] = df['data'].dt.month
df.head()
df.describe()

colunas = df.keys()
print(colunas)

nordeste = df.query('regiao == "Nordeste" and ano == 2022')
nordeste_mes_5 = df.query('regiao == "Nordeste" and ano == 2022 and mes==5')
nordeste_mes_5.head()
#veja quais os anos estão filtrados
nordeste['ano'].unique()

nordeste = nordeste.replace(np.nan, 0)
nordeste.head()


#agupar valores de casos por estado, ano e mês.
dt_agrupado_nordeste = nordeste.groupby(['estado','mes'])['casosNovos', 'obitosNovos'].max().reset_index()
dt_agrupado_nordestsum = nordeste.groupby(['estado'])['casosNovos', 'obitosNovos'].sum().reset_index()
dt_agrupado_nordeste2 = nordeste_mes_5.groupby(['estado','mes'])['casosNovos', 'obitosNovos'].max().reset_index()
dt_agrupado_nordeste.head()


itens_estados = dt_agrupado_nordeste['estado'].unique()
print(itens_estados)


from typing import Text
#construir grafico
meses = [1,2,3,4,5]
titulo = 'Numero de casos ao longo dos meses no nordeste'
fig = px.bar(dt_agrupado_nordeste2, x='mes', y='casosNovos', color='estado',barmode='group', title=titulo)
fig.update_traces( textposition='outside')
fig.update_xaxes(type='category')

fig.show()
