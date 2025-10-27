print('-=-' * 15)
print('CONVERSOR')
print('-=-' * 15)

valordolar = 0
while True:
    valordolar = float(input('Coloque o valor do dólar atualmente U$'))
    print(f'Valor dólar atualmente R${valordolar:.2f}')
    quantidadedolar = float(input('Quantos dólares você gostaria de comprar? U$'))
    conversao = quantidadedolar * valordolar
    print(f'Se você comprar U${quantidadedolar:.2f} você vai gastar R${conversao:.2f}\n')
