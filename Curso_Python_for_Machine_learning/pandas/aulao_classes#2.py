class Tote:
    def __init__(self,v:int,i:int):
        self.valor = v
        self.incremento = i
    def incrementa(self):
        self.valor = self.valor + self.incremento

a = Tote(10,1)
a.incrementa()
print(a.valor)