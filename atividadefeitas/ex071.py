while True:
    numero = int(input('Coloque um número positivo: '))
    print(numero)
    numero_string = str(numero)
    print(f'Número invertido: {numero_string[::-1]}')

    decisao = str(input('\nFazer novamente? S/N ')).strip()
    while decisao not in 'SsNn':
        decisao = str(input('Algo deu errado, quer fazer novamente? '))
    if decisao in 'Ss':
        continue
    elif decisao in 'Nn':
        break
print('PROGRAMA ENCERRADO')
quit