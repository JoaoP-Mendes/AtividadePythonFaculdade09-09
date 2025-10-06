print('REAJUSTE SALARIAL')
while True:
    salario = float(input('Informe o salário :R$'))
    
    if salario <= 280.00:
        reajuste = (salario * 20 / 100) + salario
        print(f'O salário teve aumento de {reajuste - salario:.2f}, 20%, foi de {salario:.2f} para {reajuste:.2f}')
        decisao = str(input('Verificar de outro funcionário? S/N ')).upper().strip()
        if decisao == 'S':
            continue
        elif decisao == 'N':
            break
    
    if salario > 280.00 and salario <= 700.00:
        reajuste = salario * 15 / 100
        print(f'')