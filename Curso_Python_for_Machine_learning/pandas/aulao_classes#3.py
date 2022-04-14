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

a = Tote()
a.incrementa()
a.valor
print(a.valor)

a.verifica()
print(a.verifica)

a.exponencial(3)
a.valor_exponencial
print(a.valor_exponencial)