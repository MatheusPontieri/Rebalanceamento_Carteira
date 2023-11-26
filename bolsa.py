import yfinance as yf
import heapq
# Sempre manter yfinance atualizado -> pip install yfinance --upgrade

# Define os ativos, proporções e quantidades a partir de um arquivo txt. Não deixar linhas sobrando no arquivo
ativos, proporcoes, quantidades, moedas, valor_moedas = [], [], [], ['USDBRL=X', 'EURBRL=X'], []
with open('bolsa.txt', 'r') as arquivo:
    for linha in arquivo:
        tick, quant, prop = linha.strip().split(';')
        ativos.append(tick), quantidades.append(float(quant)), proporcoes.append(float(prop))
quantidades1 = quantidades.copy()

print('\nCalculando cotações')

# Obtém as cotações atuais dos ativos
dados_moedas = yf.download(moedas, period = '1d', progress = False) # Posso pegar a cotação de várias moedas
for moeda in moedas:
    valor = dados_moedas['Close'][moeda].iloc[-1]
    valor_moedas.append(valor)
    
# Posso trocar tickers = 'USDBRL=X' por uma lista e colocar [ticket] dps de Close
info = yf.download(ativos, period = '1d', progress = False)

current_prices = []
for ticker in ativos:
    current_price = info['Close'][ticker].iloc[-1]
    current_price *= valor_moedas[0] if ".SA" not in ticker else 1
    current_prices.append(current_price)

# Calcula o patrimônio atual da carteira e o objetivo de cada ativo
patrimonio_carteira = [q * p for q, p in zip(quantidades, current_prices)]
prop_atual = [proporcao * sum(patrimonio_carteira) for proporcao in proporcoes]

op = int(input(f"\n***Menu Interativo***\n\n[1] Mostrar o desvio percentual dos ativos\n"
               f"[2] Rebalancear automaticamente a carteira\n"
               f"[3] Mostrar cotação dos ativos\n"
               f"[4] Mostrar quantidade de cada ativo\nSua opção: "))
print()

if op == 2:
    # Pede o patrimônio atual e o valor do aporte
    valor_aporte = float(input("Digite o valor do aporte: "))
    valor_aporte2 = valor_aporte

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
        # Enquanto ainda houver valor disponível para investir e a carteira estiver desbalanceada
        i = 2
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

            # Verificar se ativos dos Eua não entram aqui 🤔
            # Caso o programa mande comprar x cotas de um ativo para rebalancear, mas o valor restante do aporte só permite a compra de x - 1
            if valor_aporte < quantidade_a_comprar * cotacao_menor_patrimonio:
                print(f"O aporte restante não permite comprar {quantidade_a_comprar} cotas de {ativos[index_menor_patrimonio]}, haverá uma diminuição de cotas até poder comprar!")
                while valor_aporte < quantidade_a_comprar * cotacao_menor_patrimonio or quantidade_a_comprar == 0:
                    # Se mandar comprar 1 cota e depois verificar que não tenho dinheiro nem para uma, vai diminuir para 0
                    quantidade_a_comprar -= 1
                    if quantidade_a_comprar <= 0: #Só de entrar nesse if, já não tenho mais dinheiro para comprar
                        proximo_menor_patrimonio = heapq.nsmallest(i, menor_patrimonio1)[-1]
                        index_menor_patrimonio = menor_patrimonio1.index(proximo_menor_patrimonio)
                        quantidade_a_comprar = round(faltas[index_menor_patrimonio] / current_prices[index_menor_patrimonio]) # Visc vai dar 0 aqui
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
            comprar = quantidades[i] - quantidades1[i]
            if comprar != 0:
                print(f"Comprar {comprar} {ativos[i]}")

elif op == 1:
    lista_desvio = []
    for i in range(len(ativos)):
        desvio = (patrimonio_carteira[i] - prop_atual[i])/sum(patrimonio_carteira)*100
        lista_desvio.append(desvio)

    i = 0
    while i < len(lista_desvio):
        proximo_menor_pctg = heapq.nsmallest(i+1, lista_desvio)[-1]
        index_prox_menor_pctg = lista_desvio.index(proximo_menor_pctg)
        print(f"{ativos[index_prox_menor_pctg]}: {round(proximo_menor_pctg,1)}%")
        i += 1

elif op == 3:
    print(*(f'{ativos[i]}: R$ {current_prices[i]:.2f}' for i in range(len(current_prices))), sep='\n')

elif op == 4:
    for i in range(len(ativos)):
        print(f"{ativos[i][:6]}: {quantidades1[i]}")

else:
    print("Opção Inválida!")
