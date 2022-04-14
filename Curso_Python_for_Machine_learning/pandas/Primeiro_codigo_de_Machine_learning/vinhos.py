import pandas as pd
dados = pd.read_csv('/home/tote/Documentos/VScode/1/Curso_Python_for_Machine_learning/pandas/Primeiro_codigo_de_Machine_learning/archive/wine_dataset.csv')

dados['style'] = dados['style'].replace('red',0)
dados['style'] = dados['style'].replace('white',1)

#separando as variaveis entre preditoras e variavel alvo
y = dados['style']
x = dados.drop("style", axis = 1)

from sklearn.model_selection import train_test_split

#criando os conjuntos de dados de treino e teste:
x_treino,x_teste,y_treino,y_teste = train_test_split(x,y,test_size = 0.3)

from sklearn.ensemble import ExtraTreesClassifier
#Criação do modelo:
modelo = ExtraTreesClassifier(n_estimators=100)
modelo.fit(x_treino,y_treino)

#Imprimindo resultados
resultado = modelo.score(x_teste,y_teste)
print("Acurácia:",resultado)

#Previsões com base nos dados coletados
 
#gabarito
print(y_teste[200:203])

#valores
print(x_teste[200:203])

previsoes = modelo.predict(x_teste[200:203])
print (previsoes)