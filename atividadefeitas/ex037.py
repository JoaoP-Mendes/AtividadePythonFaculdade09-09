valorpão = 1.00
valorbroa = 3.50
qntpão = 0
qntbroa = 0


quantidadepão = int(input('Quantos pães foram vendidos? '))
qntpão += quantidadepão
valor1 = quantidadepão * valorpão

quantidadebroa = int(input('Quantas broas foram vendidas? '))
qntbroa += quantidadebroa
valor2 = quantidadebroa * valorbroa

total = valor1 + valor2 

print(f'\nForam vendidos {qntpão} pães, {qntbroa} broas.')
print(f'O valor total é R${total:.2f}, deve ser guardado R${total * 10 / 100}.')