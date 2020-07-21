class Carteira_Contabil:
    def __init__(self, Y):
        self.Y = Y
        self.Conta_Corrente = 0

    def deposito(self, Montante):
        self.Conta_Corrente += Montante
        return Montante

    def retirada(self, Montante):
        self.Conta_Corrente -= Montante
        return Montante

if __name__ == '__main__':
    CEF= Carteira_Contabil(13890870856)
    CEF.deposito(500)
    CEF.deposito(500)
    CEF.deposito(-80)
