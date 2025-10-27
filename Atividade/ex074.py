numeros = []

for c in range(0, 5):
    numero = int(input('Digite um número: '))
    numeros.append(numero)

print('-=-' * 15)
for i, n in enumerate(numeros):
    print(f'O numero {n} está na posição {i} da lista')