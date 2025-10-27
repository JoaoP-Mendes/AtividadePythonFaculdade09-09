while True: 
    salario = float(input('Informe o salario: R$ '))
    vendas = float(input('Informe o valor de produtos vendidos: R$ '))
    comissao = vendas * 4 / 100
    print(f'O salário fixo é {salario:.2f}')
    print(f'O valor da comissão foi de {comissao:.2f}')
    print(f'O valor do salário R${salario:.2f} + comissão R${comissao:.2f} é R${salario + comissao:.2f}')

    decisao = str(input('\nContinuar para outro funcionário? S/N ')).upper().strip()
    if decisao == 'S':
        continue
    elif decisao == 'N':
        break
print('PROGRAMA ENCERRADO!')