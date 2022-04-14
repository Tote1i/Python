import pandas as pd

alunos = {'Nome':['Ricardo','Tote','Pedro','Roberto'],
          'Nota': [4,9,5.5,6],
          'Aprovado':['Nao','Sim','Nao','Sim']}
alunosDF = pd.DataFrame(alunos)

print(alunosDF.shape)

print(alunosDF.describe())

print("\n",alunosDF['Nome'])

print("\n",alunosDF.loc[[2]])

print("\n",alunosDF.loc[alunosDF['Nome']=='Tote'])

#aula15
novoDF = alunosDF.loc[alunosDF['Nota']!=9]
print(novoDF)

