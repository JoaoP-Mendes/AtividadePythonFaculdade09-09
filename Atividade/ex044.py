print('-=-' * 20)
print(f'{'VERIFICAÇÃO TABUADA'}')
print('-=-' * 20)

while True:
    tabuada = int(input('Gostaria de verificar a tabuada de qual número? '))
    print(f'\nINICIANDO TABUADA DE {tabuada}\n')
    
    for c in range(0, 11):
        print(f'{tabuada} x {c} = {tabuada * c}')
    
    decisao = str(input('Verificar outra tabuada? S/N ')).upper().strip
    if decisao == 'S':
        continue
    elif decisao == 'N':
        break
print('OBRIGADO, VOLTE SEMPRE!!')