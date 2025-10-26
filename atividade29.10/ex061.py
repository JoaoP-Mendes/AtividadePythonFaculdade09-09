contImpar = 0
contPar = 0

while True:
    for c in range(0, 10):
        numero = int(input('Digite um número: '))
        if numero % 2 == 0:
            contPar += 1
        elif numero % 2 != 0:
            contImpar += 1

    print(f'Foram digitados {contPar} numeros pares')
    print(f'Foram digitados {contImpar} numeros impares\n')

    decisao = str(input('Quer fazer novamente? S/N ')).strip()
    while decisao not in 'SsNn':
         decisao = str(input('Não compreendido, que fazer novamente? S/N ')).strip()
    if decisao in 'Ss':
        continue
    elif decisao in 'Nn':
        break

print('MUITO OBRIGADO VOLTE SEMPRE!!!')
quit