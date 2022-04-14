#Criação de box plot

import pandas as pd
from pandas_ods_reader import read_ods
dados = pd.read_csv('/home/tote/Documentos/VScode/1/Curso_Python_for_Machine_learning/pandas/athlete_events.csv')

import matplotlib.pyplot as plt

dados.boxplot(column = ['Age','Height'])
plt.show()