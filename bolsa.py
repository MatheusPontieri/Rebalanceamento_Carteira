from time import sleep
import yfinance as yf

sleep(1)

while True:
    
    print("Menu de Opções\n")
    print("[1] - Fazer rebalanceamento da carteira")
    print("[2] - Saber variação percentual dos ativos")
    op = int(input("Digite a opção escolhida: "))
    
    while op == 1:
    
        patr_atual = float(input("\nDigite o patrimônio em Renda Variável: "))
        aporte = float(input("Digite o valor do aporte: "))
        ativos = int(input("Digite a quantidade de ativos: "))
        pctg = (100/ativos)/100
        patr_final = patr_atual + aporte
        idealagr = patr_final*pctg
        # Posso criar def que verifica o menor preço e faz rebalanceamento
        while op == 1:
            ticker = str(input("Digite o ticket do ativo com menor patrimônio no seguinte estilo (WEGE3F.SA):  "))

            ativo = yf.Ticker(ticker)
            cot = ativo.history(period="1d")["Close"][0]
            atual = float(input("Digite a quantidade de cotas desse ativo: "))
            natual = atual*cot
            investir = (idealagr - natual)/cot
            print(investir)
            investir1 = round(investir,2)

            sleep(1)
            print("\nVocê deve comprar",investir1,"cotas desse ativo!\n")
            sleep(2)
            op = int(input("O que deseja fazer?\n[1] Mais um rebalanceamento\n[2] Voltar ao menu inicial:\nOpção escolhida: "))
            print("\n")
        op = 3
        
    while op == 2:
        patr_atual = float(input("Digite o patrimônio em Renda Variável: "))
        ativos = int(input("Digite a quantidade de ativos: "))
        pctg = (100/ativos)/100
        idealants = patr_atual*pctg
    
        hglg11 = float(input("Valor investido em HGLG11: "))
    
        hgre11 = float(input("Valor investido em HGRE11: "))
    
        hgff11 = float(input("Valor investido em HGFF11: "))
    
        hgpo11 = float(input("Valor investido em HGPO11: "))
    
        wege3 = float(input("Valor investido em WEGE3: "))
    
        petr4 = float(input("Valor investido em PETR4: "))
    
        itub4 = float(input("Valor investido em ITUB4: "))
    
        vale3 = float(input("Valor investido em VALE3: "))
    
        desvio_hglg11 = ((hglg11 - idealants)/patr_atual)*100
        desvio_hgre11 = ((hgre11 - idealants)/patr_atual)*100
        desvio_hgff11 = ((hgff11 - idealants)/patr_atual)*100
        desvio_hgpo11 = ((hgpo11 - idealants)/patr_atual)*100
        desvio_wege3 = ((wege3 - idealants)/patr_atual)*100
        desvio_petr4 = ((petr4 - idealants)/patr_atual)*100
        desvio_itub4 = ((itub4 - idealants)/patr_atual)*100
        desvio_vale3 = ((vale3 - idealants)/patr_atual)*100
        
        print("Desvio percentual dos ativos:")
        print("HGLG11: ",round(desvio_hglg11,1),"%")
        print("HGRE11: ",round(desvio_hgre11,1),"%")
        print("HGFF11: ",round(desvio_hgff11,1),"%")
        print("HGPO11: ",round(desvio_hgpo11,1),"%")
        print("WEGE3:",round(desvio_wege3,1),"%")
        print("PETR4:",round(desvio_petr4,1),"%")
        print("ITUB4:",round(desvio_itub4,1),"%")
        print("VALE3:",round(desvio_vale3,1),"%")
        
        op = int(input("Deseja voltar ao menu inicial(1 - Sim 2 - Não): "))
        if op == 2:
            break