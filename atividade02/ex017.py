print('-' * 25)
print('REAJUSTE SALARIAL')
print('-' * 25)

while True:
    salario = float(input('Informe o salário: R$ '))
    
    if salario <= 280.00:
        reajuste = (salario * 20 / 100) + salario
        print(f'\nO salário teve aumento de {reajuste - salario:.2f}, 20%, foi de {salario:.2f} para {reajuste:.2f}')
        decisao = str(input('Verificar de outro funcionário? S/N ')).upper().strip()
        if decisao == 'S':
            continue
        elif decisao == 'N':
            break
    
    elif salario > 280.00 and salario <= 700.00:
        reajuste = (salario * 15 / 100) + salario
        print(f'\nO salário teve um aumento de {reajuste - salario:.2f}, 15%, foi de {salario:.2f} para {reajuste:.2f}')
        decisao = str(input('Verificar de outro funcionário? S/N ')).upper().strip()
        if decisao == 'S':
            continue
        elif decisao == 'N':
            break
    
    elif salario > 700.00 and salario <= 1500.00:
        reajuste = (salario * 10 / 100) + salario
        print(f'\nO salário teve um aumento de {reajuste - salario:.2f}, 10%, foi de {salario:.2f} para {reajuste:.2f}')
        dicisao = str(input('Verificar de outro funcionario? S/N ')).upper().strip()
        if dicisao == 'S':
            continue
        elif dicisao == 'N':
            break
    
        reajuste = (salario * 5 / 100) + salario
        print(f'\nO salario teve um aumento de {reajuste - salario:.2f}, 5%, foi de {salario:.2f} para {reajuste:.2f}')
        decisao = str(input('Verificar de outro funcionário? S/N '))
        if decisao == 'S':
            continue
        elif decisao == 'N':
            break
print('PROGRAMA ENCERRADO!')