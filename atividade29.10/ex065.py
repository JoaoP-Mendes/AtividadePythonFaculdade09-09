divida = float(input('Qual o valor da sua divida R$'))
quantidade_parcelas = int(input(f'Em quantas vezes gostaria de parcelar R${divida}? '))


while quantidade_parcelas < 0:
    quantidade_parcelas = int(input('Algo deu errado, quantas vezes gostaria de parcelar? ')) 
print('\n')



if quantidade_parcelas > 0 and quantidade_parcelas <= 2: #Parcela 0
    juros = divida * 0 / 100
    valor_dividido = (juros + divida) / quantidade_parcelas
    print(f'A sua dívida ficou {quantidade_parcelas}x de R${valor_dividido:.2f} com juros de R${juros:.2f}')

elif quantidade_parcelas > 2 and quantidade_parcelas <= 5: #Parcela 3
    juros = divida * 10 / 100
    valor_dividido = (juros + divida) / quantidade_parcelas
    print(f'A sua dívida ficou {quantidade_parcelas}x de R${valor_dividido:.2f} com juros de R${juros:.2f}')

elif quantidade_parcelas > 5 and quantidade_parcelas <= 8: #Parcela 6
    juros = divida * 15 / 100
    valor_dividido = (juros + divida) / quantidade_parcelas
    print(f'A sua dívida ficou {quantidade_parcelas}x de R${valor_dividido:.2f} com juros de R${juros:.2f}')

elif quantidade_parcelas > 8 and quantidade_parcelas <= 11: #Parcela 9
    juros = divida * 20 / 100
    valor_dividido = (juros + divida) / quantidade_parcelas
    print(f'A sua dívida ficou {quantidade_parcelas}x de R${valor_dividido:.2f} com juros de R${juros:.2f}')

elif quantidade_parcelas >= 12: #Parcela 12
    juros = divida * 25 / 100
    valor_dividido = (juros + divida) / quantidade_parcelas
    print(f'A sua dívida ficou {quantidade_parcelas}x de R${valor_dividido:.2f} com juros de R${juros:.2f}')
    