while True:
    A = int(input('Digite um valor / 0 para sair: '))
    if A == 0:
        break
    B = int(input('Digite outro valor: '))
    
    if A == B: 
        C = A + B
        print(f'O valor {A} + valor {B} é = {C}')
    elif A != B:
        C = A * B
        print(f'O valor {A} x valor {B} é = {C}')
print('PROGRAMA ENCERRADO')