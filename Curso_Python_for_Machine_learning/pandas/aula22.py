import pandas as pd
from pandas_ods_reader import read_ods
dados = pd.read_csv('/home/tote/Documentos/VScode/1/Curso_Python_for_Machine_learning/pandas/athlete_events.csv')

#Como lidar com dados faltantes (NaN) em um Dataset

#novo dataframe sem dados faltantes
dados2 = dados.dropna()

#True se o dado for faltante, False se nao
enulo = dados.isnull()

#mostra quantos dados faltantes cada variavel tem
faltantes = dados.isnull().sum()

faltantes_percentual = (dados.isnull().sum() /len(dados['ID']))*100
print(faltantes_percentual)

#substituir os dados por algo
dados['Medal'].fillna('Nenhuma',inplace = True)