#Python para Machine Learnig aula 8
#Função map()

#função normal
ms = [40,20,50,10,60]
km = []

for i in ms:
    km.append(i*3.6)
print(km)

#função map
km2 = list(map(lambda x: x*3.6,ms))
print (km2)