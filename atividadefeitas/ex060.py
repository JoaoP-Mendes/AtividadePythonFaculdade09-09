tabuada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

while True:
    tab = int(input('Gostaria de verificar qual tabuada entre 1 e 10? '))
    if tab in tabuada:

        print('-' * 25)
        for c in range(1, 10):
            print(f'{tab} x {c} = {tab * c}')
        print('-' * 25)
    
    elif tab not in tabuada:
        print(f'O valor {tab} não está lista que conseguimos gerar.\n')

    decisao = str(input('Quer continuar? S/N '))
    if decisao in 'Ss':
        continue
    elif decisao in 'Nn':
        break
    while decisao not in 'SsNn':
        decisao = str(input('ALGO DEU ERRADO. Quer continuar? S/N '))