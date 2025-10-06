while True:
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        print(f'O número {n} é par')
    else:
        print(f'O número {n} é impar')
    print('Gostaria de verificar outro número? 1 - SIM / 2 - NÃO')
    decisao = int(input(''))
    if decisao == 2:
        break
    print('-' * 20)
print('PROGRAMA ENCERRADO!!')