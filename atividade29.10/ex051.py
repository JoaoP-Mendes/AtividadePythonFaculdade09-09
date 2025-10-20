while True:
    n1 = int(input('Coloque o número e veja soma / coloque -999 para sair: '))
    if n1 == -999:
        break
    n2 = int(input(f'{n1} + ' ))
    n3 = n1 + n2
    print(f'{n1} + {n2} = {n3}')
print('PROGRAMA ENCERRADO!')