G = 2.50
A = 1.90

descG = G * 3 / 100

while True:
    print('Gostaria de abastecer com gasolina ou com Álcool? ')
    decisao = str(input('Digite G - para gasolina e A - Para alcool: ')).upper().strip()
    if decisao == 'G':
        litros = float(input('\nQuantos litros gostaria de colocar? '))

        if litros <= 20.00:
            ndesco = 3
            desco = G * 3 / 100
            valor = litros * G - (desco * litros)
            break

        elif litros > 20.00:
            ndesco = 5
            desco = G * 5 / 100
            valor = litros * G - (desco * litros)
            break

    elif decisao == 'A':
        litros = float(input('\nQuantos litros gostaria de colocar? '))

        if litros <= 20.00:
            ndesco = 4
            desco = A * 4 / 100
            valor = litros * A - (desco * litros)
            break

        elif litros > 20.00:
            ndesco = 6
            desco = A * 6 / 100
            valor = litros * G - (desco * litros)
            break

print(f'O valor para {litros:.1f}L com desconto de {ndesco}% por L é R${valor:.2f}')
        