class Tote:
    def __init__(self,v=10,i=1):
        self.valor = v
        self.incremento = i
        self.valor_exponencial = v
    def incrementa(self):
        self.valor = self.valor + self.incremento
    def verifica(self):
        if self.valor > 12:
            print("ultrapassou 12")
        else:
            print("Não ultrapassou 12")
    def exponencial(self,e):
        self.valor_exponencial = self.valor**e
    def incrementa_quadrado(self):
        self.incrementa()
        self.exponencial(2)

#Herança
#Criação de outro metodo __init__ 
class Calculos(Tote):
          def __init__(self,d=5):
              super().__init__(v=10,i=1)
              self.divisor = d
          def decrementa(self):
              self.valor = self.valor - self.incremento
          def divide(self):
              self.valor = self.valor/self.divisor

c = Calculos()      

c.decrementa()
c.valor
print(c.valor)

#c.divide()
#c.valor
#print(c.valor)

#c.incrementa()
#c.valor
#print(c.valor)