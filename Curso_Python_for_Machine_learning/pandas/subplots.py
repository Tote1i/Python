import matplotlib.pyplot as plt
import numpy as np

#Criação de gráfico padrão
x = np.arange(-1000,1000,1)
y = x**2
plt.plot(x,y)
#plt.show()

#Subplots
y1 = x**2
y2 = x**3
y3 = -x**2
y4 = -x**3

plt.subplot(2,2,1) #(2,2)quantas linhas e colunas, (1)quadrante ocupado
plt.plot(x,y1)
plt.subplot(2,2,2)
plt.plot(x,y2)
plt.subplot(2,2,3)
plt.plot(x,y3)
plt.subplot(2,2,4)
plt.plot(x,y4)
#plt.show()

#Definir o tamanho da figura
figura = plt.figure(figsize =(10,10))

figura.add_subplot(2,2,1)
plt.plot(x,y1)
figura.add_subplot(1,2,2)
plt.plot(x,y2)
figura.add_subplot(2,2,3)
plt.plot(x,y3)
#plt.show()

#Fzendo o msm usando for
#criar uma lista
y = [y1,y2,y3,y4]

figura = plt.figure(figsize=(10,10))

for i in range(4):
    figura.add_subplot(2,2,i+1)
    plt.plot(x,y[i])
#plt.show()    

