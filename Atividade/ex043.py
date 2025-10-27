totalguardado = 0

while True:
    centavos1 = 0.1
    centavos5 = 0.5
    centavos10 = 0.10
    centavos25 = 0.25
    centavos50 = 0.50
    real1 = 1.0

    print("""Adicionar na reserva de moedas: 
          R$0.01
          R$0.10
          R$0.25
          R$0.50
          R$1.00""")
    adionandoValor = float(input('Qual moeda deseja adicionar? R$'))

    if adionandoValor == 0.01:
        quantidadeMoedas = int(input('Quantas Moedas de R$0.01 centavos você quer adicionar? '))
        valorMoedas = 0.01 * quantidadeMoedas
        totalguardado += valorMoedas

        decisao = str(input('Quer adicionar outras moedas? S/N ')).upper().strip()
        if decisao == 'S':
            print('\n')
            continue
        elif decisao == 'N':
            print('\n')
            break
    elif adionandoValor == 0.10:
        quantidadeMoedas = int(input('Quantas moedas de R$0.10 centavos você quer adicionar? '))
        valorMoedas = 0.10 * quantidadeMoedas
        totalguardado += valorMoedas

        decisao = str(input('Quer adicionar outras moedas? S/N ')).upper().strip()
        if decisao == 'S':
            print('\n')
            continue
        elif decisao == 'N':
            print('\n')
            break

    elif adionandoValor == 0.25:
        quantidadeMoedas == int(input('Quantas moedas de R$0.25 centavos você quer adicionar? '))
        valorMoedas = 0.25 * quantidadeMoedas
        totalguardado += valorMoedas

        decisao = str(input('Quer adicionar outras moedas? S/N '))
        if decisao == 'S':
            print('\n')
            continue
        elif decisao == 'N':
            print('\n')
            break
    
    elif adionandoValor == 0.50:
        quantidadeMoedas = int(input('Quantas moedas de R$0.50 centavos você quer adicionar? '))
        valorMoedas = 0.50 * quantidadeMoedas
        totalguardado += valorMoedas

        decisao = str(input('Quer adicionar outras moedas? S/N '))
        if decisao == 'S':
            print('\n')
            continue
        elif decisao == 'N':
            print('\n')
            break

    elif adionandoValor == 1.00:
        quantidadeMoedas = int(input('Quantas moedas de R$1.00 você quer adionar? '))
        valorMoedas = 1.00 * quantidadeMoedas
        totalguardado += valorMoedas

        decisao = str(input('Quer adicionar outras moedas? S/N '))
        if decisao == 'S':
            continue
        elif decisao == 'N':
            break


if totalguardado < 1.00:
    print(f'Dani tem R${totalguardado:.2f} centavos guardados no total')
elif totalguardado >= 1.00:
    print(f'Dani tem R${totalguardado} guardados no total')
