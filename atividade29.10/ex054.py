print('iniciando programa | Coloque 0 para sair')
cont = 0
cont50 = 0
while True:
    numeros = int(input('Coloque um número inteiro: '))
    cont += 1
    if numeros == 50:
        cont50 += 1
    if numeros == 0:
        break
print(f'\nForam digitado {cont} números')
print(f'Dentro de {cont} números, {cont50} deles são o número 50.')
print('PROGRAMA ENCERRADO!')