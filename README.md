# Rebalanceamento de carteira
Programa em Python que faz o rebalanceamento automático de uma carteira de ativos brasileiros e dos Eua.

## Utilidade
Para fazer um aporte, deve-se fazer alguns cálculos, como patrimônio ideal, obter ativo com menor patrimônio, fazer a diferença entre os dois e com o valor obtido, dividir pela cotação. Com o programa, isso é feito de forma automática e facilita para o usuário no momento em quer for aportar. 

## Funcionalidades
* Mostra quais ativos devem ser comprados e a quantidade de cada.
* Mostra a variação percentual dos ativos da carteira em relação ao objetivo definido.

## Como funciona
A estratégia utilizada é a "Alocação de Ativos", ou seja, consiste em comprar o ativo cujo patrimônio está menor do que o percentual definido. 
Exemplo: Suponhamos uma carteira com 10 ativos e um patrimônio de 1000 reais, onde todos os ativos tem a mesma porcentagem (10% -> R$ 100).

Nessa carteira, há um ativo cujo patrimônio é 70 reais, ou seja, abaixo do objetivo definido. Dessa maneira, o programa irá investir nesse ativo até atingir os 100 reais, ou seja, irá investir 30 reais nesse ativo, mostrando o número de cotas que devem ser compradas de acordo com a cotação.

Para usá-lo, deve-se apenas trocar os ativos pelos do usuário, trocar as proporções de acordo com a estratégia e definir a quantidade. Quando o programa for iniciado, deve-se escolher uma das opções e/ou digitar o valor que será aportado na carteira (não em cada ativo).

## Instalação 
É necessário instalar uma biblioteca para puxar automaticamente a cotação dos ativos definidos e, além disso, deve-se ter o Python instalado. Pode-se instalar essa biblioteca usando o prompt de comando (CMD).
```
pip install yfinance
```

## Atenção
* Caso o cálculo do programa mande comprar um valor quebrado de cotas, será arredondado no caso do mercado brasileiro, visto que a B3 só permite comprar valores inteiros de ativos, diferente dos Eua, onde pode-se comprar 0.05 de uma ação e, nesse caso, será arredondado para 4 casas decimais.

* Caso chegue em um momento no qual o valor do aporte seja menor do que a cotação do ativo com menor patrimônio, o programa não buscará o ativo com menor cotação (pois esse pode ser o menos recomendado e com maior porcentagem), o cálculo irá priorizar o próximo ativo com menor patrimônio e com uma cotação que seja menor do que o restante do aporte.

* Os ativos brasileiros devem terminar em .SA na lista, pois assim são identificados na biblioteca importada. Além disso, deve-se organizar os ativos, proporções e quantidades em ordem, ou seja, o primeiro ticker da lista, deve corresponder a primeira proporção e deve corresponder a primeira quantidade da devida lista.

* Os ativos usados no programa são apenas para fins de cálculo, não são recomendação de compra e nem venda.

## Futuras melhorias
* Usuário poderá editar ativos, quantidades e proporções em um arquivo txt e não precisará editar o código diretamente
* Adicionar funções ao código, de modo que reduzirá linhas e tornará mais legível a leitura do algoritmo
* Adicionar mais opções ao Menu para tornar o programa multifuncional
