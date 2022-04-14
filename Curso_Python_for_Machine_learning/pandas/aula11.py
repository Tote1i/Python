import pandas as pd
from pandas_ods_reader import read_ods

teste = read_ods('/home/tote/Documentos/VScode/1/Curso_Python_for_Machine_learning/pandas/teste.ods',1)

teste2 = pd.read_csv('/home/tote/Documentos/VScode/1/Curso_Python_for_Machine_learning/pandas/athlete_events.csv')

print (teste2.head())