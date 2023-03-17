import yfinance as yf
from time import sleep
# Sempre manter yfinance atualizado

# Define os ativos e as proporções
ativos = ["HGLG11.SA", "HGRE11.SA", "HGFF11.SA", "HGPO11.SA", "WEGE3.SA", "PETR4.SA", "ITUB4.SA", "VALE3.SA"]
proporcoes = [0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125]

# Quantidade de ações de cada tipo
quantidades = [2, 2, 1, 3, 10, 6, 3, 8]
quantidades1 = [2, 2, 1, 3, 10, 6, 3, 8]

# Pede o patrimônio atual e o valor do aporte
valor_aporte = float(input("Digite o valor do aporte: "))

# Obtém as cotações atuais dos ativos
current_prices = []
for ticker in ativos:
    stock = yf.Ticker(ticker)
    current_price = stock.history(period='1d')['Close'][0]
    current_prices.append(current_price)
    
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
    print(faltas)
    sleep(2)

    # Enquanto ainda houver valor disponível para investir e a carteira estiver desbalanceada
    while valor_aporte > min(current_prices) and any([falta > 0 for falta in faltas]):
        # Identifica qual é o ativo com menor patrimônio atual
        menor_patrimonio = min([current_prices[i] * quantidades[i] for i in range(len(ativos))])

        # Investe o valor disponível na ação com menor patrimônio atual
        index_menor_patrimonio = [current_prices[i] * quantidades[i] for i in range(len(ativos))].index(menor_patrimonio)
        acao = ativos[index_menor_patrimonio]
        quantidade_a_comprar = (faltas[index_menor_patrimonio] / current_prices[index_menor_patrimonio])
        quantidades[index_menor_patrimonio] += quantidade_a_comprar
        valor_aporte -= quantidade_a_comprar * current_prices[index_menor_patrimonio]

        # Atualiza o patrimônio atual da carteira e as faltas de investimento
        patrimonio_carteira = [q * p for q, p in zip(quantidades, current_prices)]
        faltas = [novo_patrimonio[i] - current_prices[i] * quantidades[i] for i in range(len(ativos))]
        print("Você deve comprar ",quantidade_a_comprar," cotas do ativo",ativos[index_menor_patrimonio])

    # Mostra na tela as novas quantidades de ações de cada tipo
    print("Quantidades a comprar:")
    for i in range(len(ativos)):
        comprar = round(quantidades[i] - quantidades1[i],2)
        print(ativos[i],"-> ",comprar)
