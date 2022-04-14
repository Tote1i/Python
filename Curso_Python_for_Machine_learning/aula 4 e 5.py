#Python para Machine Learnig aula 4 e 5
#Tuplas e Dicionarios
#Tupla é uma lista imutavel (ocupa menos memoria)
#Sabe-se que é uma tupla quando a variável é acompanhada de parenteses e virgula, tuple = (1,3,2)

#Dicionario

dictionary = {'Curso' : 'Python para ML',
              'Produtor' : 'Tote',
              'Preço' : '700,00',}
print (dictionary ,'\n')

a = dictionary ['Produtor']

print (a,'\n')

#Adicionando nova chave de valor

dictionary['Pré_requisito'] = 'Python básico'

print (dictionary)