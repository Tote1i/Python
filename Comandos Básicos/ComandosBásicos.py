
#Exemplo1


idade = int(input('Qual a sua idade: '))
print ('Sua idade é %d anos\n' %idade)

#Exemplo2
conta = 17/3

print('O resultado da conta é {:.2f}\n\n'.format(conta))

#Exemplo3

ano = int(input('Em que ano voce nasceu? '))

idade = 2022 - ano

if idade >= 26:
    print('Voce eh adulto!\n\n')
else:
    print('Voce nao eh adulto!\n\n')

#Exemplo4
palavra = 'UFMT'
for i in palavra:
    print(i)

#Exemplo5
numero = int(input('Informe um número: '))
fatorial = numero
contador = 1

while (numero-contador)>1:
    fatorial = fatorial*(numero-contador)
    contador += 1
print('{0}! = {1}\n'.format(numero,fatorial))

#Exemplo6
def temletraU():
    frase = input('Digite uma frase: ')
    if 'u' in frase:
        print('Você utilizou a letra u.\n\n')
    else:
        print('Você não utilizou a letra u.\n\n')    
    
#chamar a função :
temletraU()

#Exemplo7
def somaQuadrados(a,b):
    somaQ = a**2 + b**2
    print('A soma dos quadrados {0} e {1} é {2}'.format(a,b,somaQ))

somaQuadrados(5,2)
