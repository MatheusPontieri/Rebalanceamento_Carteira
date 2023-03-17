import yfinance as yf
from time import sleep
import heapq
# Sempre manter yfinance atualizado

# Define os ativos e as proporções
ativos = ["HGLG11.SA", "HGRE11.SA", "HGFF11.SA", "HGPO11.SA", "WEGE3.SA", "PETR4.SA", "ITUB4.SA", "VALE3.SA", "AAPL", "MSFT"]
proporcoes = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]

# Quantidade de ações de cada tipo
quantidades = [2, 2, 1, 3, 10, 6, 3, 8, 0.25, 0.15]
quantidades1 = quantidades.copy()

# Pede o patrimônio atual e o valor do aporte
print("\n")
valor_aporte = float(input("Digite o valor do aporte: "))
valor_aporte2 = valor_aporte

# Obtém as cotações atuais dos ativos
stock = yf.Ticker("USDBRL=X")
dolar = stock.history(period='1d')['Close'][0]

current_prices = []
for ticker in ativos:
    stock = yf.Ticker(ticker)
    current_price = stock.history(period='1d')['Close'][0]
    if ".SA" not in ticker:
        current_price *= dolar
    current_prices.append(current_price)
print(current_prices)
sleep(8)

# Calcula o patrimônio atual da carteira
patrimonio_carteira = [q * p for q, p in zip(quantidades, current_prices)]

# Calcula o valor total da carteira após o aporte
valor_total_carteira = sum(patrimonio_carteira) + valor_aporte

# Verifica se é necessário rebalancear a carteira
if valor_total_carteira < min(current_prices):
    print("Valor do aporte é menor que a menor cotação dos ativos.")
else:
    # Calcula o novo valor que cada ativo deve ter na carteira
    novo_patrimonio = [proporcao * valor_total_carteira for proporcao in proporcoes]

    # Calcula quanto falta investir em cada ativo
    faltas = [novo_patrimonio[i] - current_prices[i] * quantidades[i] for i in range(len(ativos))]

    i = 2
    # Enquanto ainda houver valor disponível para investir e a carteira estiver desbalanceada
    while valor_aporte > min(current_prices) and any([falta > 0 for falta in faltas]):
        # Identifica qual é o ativo com menor patrimônio atual
        menor_patrimonio = min([current_prices[i] * quantidades[i] for i in range(len(ativos))])
        menor_patrimonio1 = ([current_prices[i] * quantidades[i] for i in range(len(ativos))])
        
        # Investe o valor disponível na ação com menor patrimônio atual
        index_menor_patrimonio = [current_prices[i] * quantidades[i] for i in range(len(ativos))].index(menor_patrimonio)
        quantidade_a_comprar = (faltas[index_menor_patrimonio] / current_prices[index_menor_patrimonio])

        if quantidade_a_comprar <= 0.5 and ".SA" in ativos[index_menor_patrimonio]:
            quantidade_a_comprar = 1
        elif quantidade_a_comprar > 0.5 and ".SA" in ativos[index_menor_patrimonio]:
            quantidade_a_comprar = round(faltas[index_menor_patrimonio] / current_prices[index_menor_patrimonio])
        else:
            # 4 pois pode comprar fração de ação nos Eua com até 4 casas decimais
            quantidade_a_comprar = round(faltas[index_menor_patrimonio] / current_prices[index_menor_patrimonio],4)

        cotacao_menor_patrimonio = current_prices[index_menor_patrimonio]

        # Caso o programa mande comprar x cotas de um ativo para rebalancear, mas o valor restante do aporte só permite a compra de x - 1
        if valor_aporte < quantidade_a_comprar * cotacao_menor_patrimonio:
            print(f"O aporte restante não permite comprar {quantidade_a_comprar} cotas de {ativos[index_menor_patrimonio]}, haverá uma diminuição de cotas até poder comprar!")
            while valor_aporte < quantidade_a_comprar * cotacao_menor_patrimonio or quantidade_a_comprar == 0:
                # Se mandar comprar 1 cota e depois verificar que não tenho dinheiro nem para uma, vai diminuir para 0
                quantidade_a_comprar -= 1
                if quantidade_a_comprar <= 0: #Só de entrar nesse if, já não tenho mais dinheiro para comprar
                    proximo_menor_patrimonio = heapq.nsmallest(i, menor_patrimonio1)[-1]
                    index_menor_patrimonio = menor_patrimonio1.index(proximo_menor_patrimonio)
                    quantidade_a_comprar = round(faltas[index_menor_patrimonio] / current_prices[index_menor_patrimonio]) 
                    cotacao_menor_patrimonio = current_prices[index_menor_patrimonio]
                    if cotacao_menor_patrimonio < valor_aporte and quantidade_a_comprar <= 0:
                        quantidade_a_comprar = 1
                    i += 1
            # Devo verificar novamente toda vez que comprar uma ação próxima recomendada, pois pode acontecer da prioridade da mesma diminuir e outra tomar seu index
            # vou pular pra próximo índice apenas se não conseguir comprar nem uma cota
                     
        quantidades[index_menor_patrimonio] += quantidade_a_comprar
        valor_aporte -= quantidade_a_comprar * cotacao_menor_patrimonio

        # Atualiza o patrimônio atual da carteira e as faltas de investimento
        patrimonio_carteira = [q * p for q, p in zip(quantidades, current_prices)]
        faltas = [novo_patrimonio[i] - current_prices[i] * quantidades[i] for i in range(len(ativos))]
        print("Comprar ",quantidade_a_comprar," cotas do ativo",ativos[index_menor_patrimonio])
        i = 2

    # Mostra na tela as novas quantidades de ações de cada tipo
    print("\nQuantidades a comprar:\n")
    for i in range(len(ativos)):
        print(r"Comprar",quantidades[i] - quantidades1[i],"",ativos[i])
