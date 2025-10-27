numeros = []
pares = []
impares = []
quantidade_numeros = 0
quantidade_pares = 0
quantidade_impares = 0

for c in range(0, 20):
    numero = int(input('Digite um numero: '))
    quantidade_numeros += 1
    numeros.append(numero)

    if numero % 2 == 0:
        pares.append(numero)
        quantidade_pares += 1
    
    elif numero % 2 != 0:
        impares.append(numero)
        quantidade_impares += 1


print(f'\nForam digitado {quantidade_numeros} numeros.')
print(f'Os números digitado foram: {numeros}')

print(f'\nForam digitado {quantidade_pares} numeros pares.')
print(f'Os números digitado foram: {pares}')

print(f'\nForam digitado {quantidade_impares} numeros.')
print(f'Os números digitado foram: {impares}')