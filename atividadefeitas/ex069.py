numeros = []
for c in range(0, 5):
    numero = int(input('Digite um número: '))
    numeros.append(numero)

print('\n')
print(f'A soma dos números é {sum(numeros)}')
print(f'A média dos números é {sum(numeros) // 5}')