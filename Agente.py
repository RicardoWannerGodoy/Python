from Carteira_Contabil import Carteira_Contabil
from Comercio import Comercio

class Agente:
    def __init__(self, Y):
        self.Y = Y
        self.Carteira_Contabil = Carteira_Contabil(0)
        self.satisfacao = 0

if __name__ == '__main__':
    Perini = Comercio('Supermercado')
    ClienteGold = Agente(0)
    ClienteVIP= Agente(1)
    ClienteVIP.Carteira_Contabil.deposito(1000)
    Perini.Carteira_Contabil.deposito(ClienteVIP.Carteira_Contabil.retirada(Perini.custo))

