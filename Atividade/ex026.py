while True:
    produto = str(input('Qual produto gostaria de verificar? '))
    preço = float(input(f'Coloque o preço da aquisição do {produto}: R$'))

    if preço < 50.00:
        valorvenda = (preço * 45 / 100) + preço
        print(f'O valor do {produto} ficou de R${preço:.2f} para R${valorvenda:.2f}')
        decisao = str(input('Quer verificar outro produto? S/N ')).upper().strip()
        print('\n')
        if decisao == 'S':
            continue
        elif decisao == 'N':
            break

    elif preço >= 50.00:
        valorvenda = (preço * 30 / 100) + preço
        print(f'O valor do {produto} ficou de R${preço:.2f} para R${valorvenda:.2f}')
        decisao = str(input('Quer verificar outro produto? S/N ')).upper().strip()
        print('\n')
        if decisao == 'S':
            continue
        elif decisao == 'N':
            break

print('MUITO OBRIGADO! Volte Sempre')

