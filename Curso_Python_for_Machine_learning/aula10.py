#Python para Machine Learnig aula 10
#Aprenda a usar Numpy (Biblioteca matemática)

import numpy

a = numpy.array([1,2,3])
print(a,"\n")

b = numpy.array([(1,2,3), (2,3,4), (4,5,6)])
print(b,"\n")

c = numpy.zeros((4,3))  #dimensão da matriz ;   matriz composta por zeros
print(c,"\n")

d = numpy.ones((3,5))   #matriz composta por um
print(d,"\n")

e = numpy.eye((4))        #diagonal principal composta por um
print(e,"\n")


elemento_maior_da_matriz = b.max()
print (elemento_maior_da_matriz)


elemento_menor_da_matriz = b.min()
print (elemento_menor_da_matriz)

somar_todos_os_elementos = b.sum()
print (somar_todos_os_elementos)

media_dos_elementos = b.mean()
print (media_dos_elementos)

desvio_padrao = b.std()
print(desvio_padrao)