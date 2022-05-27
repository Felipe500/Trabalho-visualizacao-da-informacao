#carregar libs
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np

#carregar dados para analise, processamento e  visualização de dados.
df = pd.read_csv('dados/HIST_PAINEL_COVIDBR_2022_Parte1_16mai2022.csv', sep=';', parse_dates=['data'])

#definir campo 'casosAcumulado' como inteiro
df['casosAcumulado'] = df['casosAcumulado'].astype(int)

#criar novos campos para facilitar a consulta e construção da representação gráfica
df['ano'] = df['data'].dt.year
df['mes'] = df['data'].dt.month

#Fazendo uma consulta no dataset e reunindo dados para analise
#filtrando por região, ano e mes
#agrupando por estado e mes, aonde o numero de casosNovos e obitosNovos são os maiores dados
#
nordeste_mes_5 = df.query('regiao == "Nordeste" and ano == 2022 and mes == 5').groupby(['estado',
                                    'mes'])['casosNovos', 'obitosNovos'].max().reset_index()

#colocando Nan por 0 para facilitar a analise das informações
nordeste_mes_5 = nordeste_mes_5.replace(np.nan, 0)


import plotly.graph_objects as go
fig2 = go.Figure()
fig2.add_trace(go.Bar(x=nordeste_mes_5['estado'], y=nordeste_mes_5['casosNovos'], name='funding1'))
fig2.add_trace(go.Bar(x=nordeste_mes_5['estado'], y=nordeste_mes_5['obitosNovos'], name='funding1'))


#construir grafico
titulo = 'Numero de casos ao longo dos meses no nordeste'

fig = px.bar(nordeste_mes_5, x='mes', y='casosNovos',  color='estado',barmode='group',
             title=titulo,text_auto=True, orientation = "v")
fig.update_traces( textposition='outside')

fig.update_xaxes(
        title_text = "MAIO",
        title_font = {"size": 20},
        title_standoff = 25)


import numpy as np
import matplotlib.pyplot as plt
import squarify

volume = nordeste_mes_5['casosNovos']
labels = nordeste_mes_5['estado']
l =[]
print(len(labels))
for index in range(len(labels)):
    l.append(labels[index]+"\n N° casos "+str(volume[index]))

plt.rc('font', size=12)
squarify.plot(sizes=volume, label=l, pad=True,
               alpha=0.3)
plt.axis('off')
plt.title("Região nordeste do Brasil", pad=True, loc='left')
plt.show()