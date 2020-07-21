import random
from Comercio import Comercio
from Agente import Agente

class Simulação:
    def __init__(self):
        self.Comercios = list()
        self.clientes = list()
        self.criar_Comercios()
        self.criar_clientes()
        self.deposito_inicial()
        #self.run_model()

    def salvar_arquivo_dados(self):
        # TODO: por fazer
        # with open('arquivo1.csv', 'w') as handler as f:
       pass

    def criar_Comercios(self):
        for Y in range(10):
            self.Comercios.append(Comercio(Y))

    def criar_clientes(self):
        for Y in range(10):
            self.clientes.append(Agente(Y))

    def media_satisfacao(self):
        satisfacao_somada = 0
        for clientes in self.clientes:
            satisfacao_somada += clientes.Elogio
        return Elogio_somada / len(self.clientes)

    def media_custo(self):
        custo_somado = 0
        for Comercio in self.Comercios:
            custo_somado += Comercio.custo
        return custo_somado / len(self.Comercios)

    def media_Carteira_Contabil(self):
        saldo_Carteira_Contabil_clientes_somada = 0
        for clientes in self.clientes:
            saldo_Carteira_Contabil_clientes_somada += clientes.Carteira_Contabil.saldo
        saldo_Carteira_Contabil_Comercios_somada = 0
        for Comercios in self.Comercios:
           saldo_Carteira_Contabil_Comercios_somada += Comercios.Carteira_Contabil.saldo
        return ((saldo_Carteira_Contabil_clientes_somada + saldo_Carteira_Contabil_Comercios_somada) / len(self.clientes + self.Comercios))

    def deposito_inicial(self):
        for clientes in self.clientes:
            clientes.Carteira_Contabil.deposito(random.randint(10, 20))

    def run_model (self):
        for clientes in self.clientes:
            Comercio_escolhida = random.choice (self.Comercios)
            if clientes.Carteira_Contabil.Conta_Corrente >= 0:
                posso_ir = Comercio_escolhida.visita_clientes ()
                if posso_ir == True:
                    Comercio_escolhida.Carteira_Contabil.deposito(clientes.Carteira_Contabil.retirada(Comercio_escolhida.custo))
                    clientes.Elogio += Comercio_escolhida.Elogio
                    return clientes.Elogio
                else:
                    return False
            else:
                return False
        return self.media_Elogio(), self.media_custo(), self.media_Carteira_Contabil()

def gravar_arquivo(valor):
    with open('resultado.txt', 'w') as handler:
        handler.write(f'{valor}')
        return

if __name__ == '__main__':
    Ricardo_Godoy= Simulação()
    media = Ricardo_Godoy.run_model()
    media_Elogio = Ricardo_Godoy.media_Elogio()
    media_Valor= Ricardo_Godoy.media_custo()
    media_Carteira_Contabil = Ricardo_Godoy.media_Carteira_Contabil()
    gravar_arquivo(f'O valor da média da simulação é {media}\n'
                   f'O valor da média de satisfação é {media_Elogio}\n'
                   f'O valor da média de Valoré {media_custo}\n'
                   f'O valor da média de Carteira_Contabil é {media_Carteira_Contabil}')
