print('LANCHONETE BURGÃO')

'100' = 11.20
'101' = 8.30
'102' = 11.50
'103' = 16.20
'201' = 6.00
'202' = 7.50
'203' = 4.70

valor = 0

while True:
    print('''CARDÁPIO - CÓDIGO E PREÇO
    [ 100 ] - CACHORRO QUENTE - R$11,20
    [ 101 ] - OVO SIMPLES     - R$8,30
    [ 102 ] - BAURU COM OVO   - R$11,50
    [ 103 ] - HAMBÚRGUER      - R$16,20
    [ 201 ] - REFRIGERANTE    - R$6,00
    [ 202 ] - SUCO            - R$7,50
    [ 203 ] - ÁGUA MINERAL    - R$4,70''')
    escolha1 = int(input('Digite o código do pedido: '))

    if escolha1 == 100:
        valor += escolha1
        print('''\nDeseja adionar alguma bebida
[ 201 ] - REFRIGERANTE    - R$6,00
[ 202 ] - SUCO            - R$7,50
[ 203 ] - ÁGUA MINERAL    - R$4,70
[ 204 ] - Nenhuma         - R$0,00''') 
        escolha2 = int(input('Digite o código do pedido: '))
        if escolha2 == '201':
            valor += '201'
            print('\n')
            break

print('')
