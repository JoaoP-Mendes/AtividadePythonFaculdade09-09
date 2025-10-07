while True:
    ano = int(input('Qual ano você vai verificar? '))
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(f'O ano {ano} é bissexto')
        decisao = str(input('Quer verificar outro ano? S/N: ')).upper().strip()
        if decisao == 'S':
            continue
        elif decisao == 'N':
            break
    else: 
        print(f'O ano {ano} não é bissexto')
        decisao = str(input('Quer verificar outro ano? S/N: ')).upper().strip()
        if decisao == 'S':
            continue
        elif decisao == 'N':
            break
print('MUITO OBRIGADO, VOLTE SEMPRE')