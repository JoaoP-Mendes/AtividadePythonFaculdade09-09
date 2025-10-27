while True:
    numero = int(input('Digite e veja o fatorial: '))
    fatorial = 1
    contador = numero

    while contador > 0:
        fatorial *= contador
        contador -= 1
    print(f'O fatorial de {numero} é {fatorial}')

    decisao = str(input('Quer fazer novamente? S/N ')).strip()
    while decisao not in 'SsNn':
        decisao = str(input('Não entendi, quer fazer novamente? S/N ')).strip()
    if decisao in 'Ss':
        continue
    elif decisao in 'Nn':
        break
print('PROGRAMA ENCERRADO')
quit