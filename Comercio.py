import random
from Carteira_Contabil import Carteira_Contabil

class ComercioSupermercado:
    def __init__(self, Y):
        self.Y = Y
        self.Carteira_Contabil = Carteira_Contabil(0)
        self.Valor= round(random.random() * 10, 2)
        self.satisfacao = random.randint(0, 10)
        self.capacidade = random.randint(5, 100)

    def visita_clientes(self):
        if self.capacidade >= 0:
            self.capacidade -= 1
            return True
        else:
            return False

    def oferece_satisfacao(self):
        if self.capacidade <= 5:
            self.satisfacao -= 10
            return self.satisfacao
        elif self.capacidade < 50:
            return self.satisfacao
        else:
            self.satisfacao += 10
            return self.satisfacao

    def __repr__(self):
        return self.Y

if __name__ == '__main__':
    Pao_de_Mel = Comercio('Doces')
    Perini = Comercio('Supermercado')
    DellVale = Comercio('Sucos')
    DellVale.Carteira_Contabil.deposito(50000)
