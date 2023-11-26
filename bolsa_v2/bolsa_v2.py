import yfinance as yf
from funcoes_classes import *

ativos = []

with open('bolsa.txt', 'r') as carteira:
    for linha in carteira:
        ticker, quant, prop = linha.strip().split(";")
        ativos.append(Ativo(ticker, int(quant), float(prop)))

info = yf.download([ativo.ticker for ativo in ativos], period="1d")['Close']
print(info)

atualizaPreco(ativos, info)

patrimonio = sum([ativo.total for ativo in ativos])

atualizaTotalDeveria(ativos, patrimonio)

print("\n***Menu Interativo***")
opc = int(input(f"\n[1] Mostrar o desvio percentual dos ativos\n"
               f"[2] Rebalancear automaticamente a carteira\n"
               f"[3] Mostrar cotação dos ativos\n"
               f"[4] Mostrar quantidade de cada ativo\nSua opção: "))

if opc == 2:
    print()
