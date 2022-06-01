#carregar libs
import pandas as pd
import plotly.express as px
import numpy as np
import plotly.graph_objects as go

#carregar dados para analise, processamento e  visualização de dados.
URL = 'https://raw.githubusercontent.com/Felipe500/Trabalho-visualizacao-de-dados/main/dados/HIST_PAINEL_COVIDBR_2022_Parte1_16mai2022.csv'
df = pd.read_csv(URL, sep=';', parse_dates=['data'])

#definir campo 'casosAcumulado' como inteiro
df['casosAcumulado'] = df['casosAcumulado'].astype(int)

#criar novos campos para facilitar a consulta e construção da representação gráfica
df['ano'] = df['data'].dt.year
df['mes'] = df['data'].dt.month

#Fazendo uma consulta no dataset e reunindo dados para analise
#filtrando por região, ano e mes
#agrupando por estado e mes, aonde o numero de casosNovos e obitosNovos são os maiores dados
#https://github.com/Felipe500/Trabalho-visualizacao-de-dados/blob/a0d4924ec85678e9c1d9679003c687e11b2b6fda/dados/HIST_PAINEL_COVIDBR_2022_Parte1_16mai2022.csv
nordeste_mes_5 = df.query('regiao == "Nordeste" and ano == 2022 and mes == 5').groupby(['estado',
                                    'mes'])['casosNovos', 'obitosNovos'].max().reset_index()

#colocando Nan por 0 para facilitar a analise das informações
nordeste_mes_5 = nordeste_mes_5.replace(np.nan, 0)
nordeste_mes_5

titulo = 'Numero de casos e obitos do Nordeste no mês de maio de 2022'
fig2 = go.Figure()
fig2.add_trace(go.Bar(x=nordeste_mes_5['estado'], y=nordeste_mes_5['casosNovos'],
                      text=nordeste_mes_5['casosNovos'], name='CASOS'))
fig2.add_trace(go.Bar(x=nordeste_mes_5['estado'], y=nordeste_mes_5['obitosNovos'],
                      text=nordeste_mes_5['obitosNovos'], name='OBITOS'))
fig2.update_layout(title_text=titulo)
fig2.show()
#construir grafico



