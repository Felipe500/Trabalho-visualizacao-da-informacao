"""
=============================
Grouped bar chart with labels
=============================

This example shows a how to create a grouped bar chart and how to annotate
bars with labels.
"""

import matplotlib.pyplot as plt
import numpy as np


labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [20, 34, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means, width, label='Men')
rects2 = ax.bar(x + width/2, women_means, width, label='Women')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(x, labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()

#############################################################################
#
# .. admonition:: References
#
#    The use of the following functions, methods, classes and modules is shown
#    in this example:
#
#    - `matplotlib.axes.Axes.bar` / `matplotlib.pyplot.bar`
#    - `matplotlib.axes.Axes.bar_label` / `matplotlib.pyplot.bar_label`
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



import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(19680801)

dt = 0.01
t = np.arange(0, 30, dt)
nse1 = np.random.randn(len(t))                 # white noise 1
nse2 = np.random.randn(len(t))                 # white noise 2

# Two signals with a coherent part at 10Hz and a random part
s1 = np.sin(2 * np.pi * 10 * t) + nse1
s2 = np.sin(2 * np.pi * 10 * t) + nse2

fig, axs = plt.subplots(2, 1)
axs[0].plot(t, s1, t, s2)
axs[0].set_xlim(0, 2)
axs[0].set_xlabel('time')
axs[0].set_ylabel('s1 and s2')
axs[0].grid(True)

cxy, f = axs[1].cohere(s1, s2, 256, 1. / dt)
axs[1].set_ylabel('coherence')

fig.tight_layout()
plt.show()