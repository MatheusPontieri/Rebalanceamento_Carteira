class Ativo:
    def __init__(self, ticker, quant, prop):
        self.ticker = ticker
        self.quant =  quant
        self.prop = prop
        self.preco = 0
        self.total = 0
        self.totalDeveria = 0

    def __repr__(self):
        return f"{self.ticker};{self.quant};{self.prop};{self.preco}"

    def atualizaTotal(self):
        self.total = self.quant * self.preco

    def atualizaTotalDeveria(self, patrimonio):
        self.totalDeveria = self.prop * patrimonio 

def atualizaPreco(ativos, info):
    for ativo in ativos:
        preco = info[ativo.ticker].iloc[-1]
        ativo.preco = round(preco, 2)
        ativo.atualizaTotal()

def atualizaTotalDeveria(ativos, patrimonio):
    for ativo in ativos:
        ativo.atualizaTotalDeveria(patrimonio)
