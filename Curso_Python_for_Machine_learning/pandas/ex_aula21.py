#relação entre duas variaveis
#criar relação da altura e peso dos atletas masculinos

import pandas as pd
from pandas_ods_reader import read_ods
dados = pd.read_csv('/home/tote/Documentos/VScode/1/Curso_Python_for_Machine_learning/pandas/athlete_events.csv')

import matplotlib.pyplot as plt
import numpy as np

#Selecionando apenas atletas masculinos
masculino = dados.loc[dados['Sex']=='M']

print(masculino.head())

#Selecionando altura e peso

peso = masculino['Weight']

altura = masculino['Height']

#Criando grafico
plt.scatter(peso,altura)
plt.show()
