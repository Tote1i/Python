#Python para Machine Learnig aula 6
#Manipulando strings

#Imprimindo caracteres especificos de uma string
def ex1():
    frase = 'Estou gostando do curso'
    print (frase [1:9])

ex1()

def ex2():
    frase = 'Estou gostando do curso'
    print(frase [2:13:2])
ex2()

#Contar quantas letras aparecem na str
def ex3():
    frase = 'Estou gostando do curso'
    print(frase.count('u'))
ex3()

#Comprimento da string
def ex4():
    frase = 'Estou gostando do curso'
    print(len(frase))
ex4()

#Trocar uma palavra por outra
def ex5():
    frase = 'Estou gostando do curso'
    print(frase.replace('curso', 'aprendizado'))
ex5()