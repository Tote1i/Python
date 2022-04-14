#Aulão Python sobre Classes, Objetos, Métodos, Herança, Construtor

#classes e metodos
class Tote:
    def incrementa(self,v,i):
        self.valor = v
        self.incremento = i
        self.resultado = self.valor + self.incremento
        return self.resultado

a = Tote() 
b = a.incrementa(10,1)    
print(b)
print(a.valor)