import pandas as pd
from pandas_ods_reader import read_ods

dados = pd.read_csv('/home/tote/Documentos/VScode/1/Curso_Python_for_Machine_learning/pandas/athlete_events.csv')

#renomeando colunas

dados.rename(columns={'Name':'Nome','Sex':'Sexo','Age':'Idade'}, inplace = True)

print(dados.head())

#contabilizando valores

dados['Medal'].value_counts()

#aula17
#excluindo colunas
dados.drop('ID', axis = 1, inplace = True)
