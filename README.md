# 📊 Rebalanceamento de carteira
O rebalanceamento automático de uma carteira de ativos brasileiros e dos Estados Unidos pode ser facilitado por meio de um programa em Python.

## 🔄 Utilidade
Ao realizar aportes, é necessário efetuar diversos cálculos, como o patrimônio ideal, identificar o ativo com menor patrimônio, calcular a diferença e dividir pelo valor atual da cota. Este programa automatiza esse processo, simplificando a vida do usuário durante os aportes.

## 🛠️ Funcionalidades
* Quais ativos devem ser comprados e a quantidade de cada.
* Variação percentual dos ativos da carteira em relação ao objetivo definido.
* Quantos ativos o usuário possui em carteira
* Cotação dos ativos

## 🔄 Como funciona
A estratégia utilizada é a "Alocação de Ativos", ou seja, consiste em comprar o ativo cujo patrimônio está menor do que o percentual definido. 
Exemplo: Suponhamos uma carteira com 10 ativos e um patrimônio de 1000 reais, onde todos os ativos tem a mesma porcentagem (10% -> R$ 100).

Nessa carteira, há um ativo cujo patrimônio é 70 reais, ou seja, abaixo do objetivo definido. Dessa maneira, o programa irá investir nesse ativo até atingir os 100 reais, ou seja, irá investir 30 reais nesse ativo, mostrando o número de cotas que devem ser compradas de acordo com a cotação no momento.

Para usá-lo, basta substituir os ativos, proporções e definir as quantidades de cotas. Ao iniciar o programa, escolha uma opção e/ou insira o valor a ser aportado na carteira (não em cada ativo).

## 🖥️ Instalação 
É necessário instalar a biblioteca yfinance para obter automaticamente as cotações dos ativos. Use o comando:
```
pip install yfinance
```

## ⚠️ Atenção
* Em mercados brasileiros, valores fracionados de cotas serão arredondados, pois a B3 permite apenas valores inteiros.

* Caso chegue em um momento no qual o valor do aporte seja menor do que a cotação do ativo com menor patrimônio, o programa não buscará o ativo com menor cotação (pois esse pode ser o menos recomendado e com maior porcentagem), o cálculo irá priorizar o próximo ativo com menor patrimônio e com uma cotação que seja menor do que o restante do aporte.
  
* Os ativos brasileiros devem terminar em .SA na lista, pois assim são identificados na biblioteca importada. Além disso, deve-se organizar os ativos, proporções e quantidades em ordem, ou seja, o primeiro ticker da lista, deve corresponder a primeira proporção e deve corresponder a primeira quantidade da devida lista.

* Os ativos usados no programa são apenas para fins de cálculo, não são recomendação de compra e nem venda.

## 🚀 Futuras melhorias
* Permitir que o usuário edite ativos, quantidades e proporções em um arquivo txt, evitando a edição direta do código ✅
* Adicionar funções ao código para reduzir linhas e melhorar a legibilidade 
* Expandir opções no menu para tornar o programa mais multifuncional
