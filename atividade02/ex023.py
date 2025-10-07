print('GRANJA TECFRANGO')

while True:
    print('Iniciando processo de gastos por galinhas da GANJA TECFRANGO')
    leftRings = 7.00
    rightRing = 4.00
    qntGalinhas = int(input('Quantas galinhas gostaria de verificar? '))
    valor = (leftRings + rightRing) * qntGalinhas

    print(f'A cada 1 galinha se tem o gasto de R${leftRings + rightRing:.2f}')
    print(f'{qntGalinhas} galinhas tem o gasto de R${valor:.2f}')
    decisao = str(input('Fazer novamente? S/N ')).upper().strip()
    print('\n')

    if decisao == 'S':
        continue
    elif decisao == 'N':
        break
print('AGRADECIMENTO TECFRANGOs')