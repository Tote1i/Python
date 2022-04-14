
#Python para Machine Learnig aula 2
#listas
#Exemplo1
import random
cidades = ['Piranhas, Rio Verde, Iporá']
escolhida = random.choice(cidades)
print('A cidade escolhida é', escolhida)


#Exemplo2
a = [1,2,3]
#adicionando um elemento a lista 'a'
a.append(24)

b = [7,8,9]

for item in b:
    a.append(item)
print(a)    
