#Python para Machine Learnig aula 9
#List Comprehension


#função normal
ms = [40,20,50,10,60]
km = []

for i in ms:
    km.append(i*3.6)
print(km)

#função comprehension
km = [x*3.6 for x in ms]
print(km)

caracteres = [i for i in 'Tote']
print(caracteres)