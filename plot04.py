#carregar libs
import matplotlib.pyplot as plt
import pandas as pd
import squarify
import numpy as np

#carregar dados para analise, processamento e  visualização de dados.
URL = 'https://raw.githubusercontent.com/Felipe500/Trabalho-visualizacao-da-informacao/main/dados/HIST_PAINEL_COVIDBR_2022_Parte1_16mai2022.csv'
df = pd.read_csv(URL, sep=';', parse_dates=['data'])

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

volume = nordeste_mes_5['casosNovos']
labels = nordeste_mes_5['estado']
l =[]
for index in range(len(labels)):
    l.append(labels[index]+"\n N° casos "+str(volume[index]))

plt.rc('font', size=12)
squarify.plot(sizes=volume, label=l, pad=True,
               alpha=0.3)
plt.axis('off')
plt.title("Região nordeste do Brasil", pad=True, loc='left')
plt.show()