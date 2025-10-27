while True:
    numero = int(input('Coloque um número e veja sem antecessor e sucessor: '))
    print(f'O número antecesso de {numero} é {numero - 1} e seu sucessor é {numero + 1}')
    decisao = str(input('Quer verificar outro número? S/N ')).upper().strip()
    if decisao == 'S':
        print('\n')
        continue
    elif decisao == 'N':
        print('\n')
        break