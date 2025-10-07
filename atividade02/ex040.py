salario = float(input('Informe seu salario: R$'))

conta1 = 200.00
conta2 = 120.00

valorconta1 = (conta1 * 2 /100) + conta1
valorconta2 = (conta2 * 2 /100) + conta2



print(f'\nJoão recebeu R${salario}, o valor da 1º conta é R${conta1}, da 2º conta é {conta2}')
print(f'Fazendo o calculo ele pagará da 1º conta R${valorconta1:.2f} e da 2º conta R${valorconta2:.2f}')
print(f'\nA soma das duas contas é de R${valorconta1 + valorconta2:.2f} e irá sobrar do seu salário R${salario - (valorconta1 + valorconta2):.2f}')