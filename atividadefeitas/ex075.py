numeros = []

for c in range(0, 10):
    numero = int(input('Digite um número para lista: '))
    numeros.append(numero)

print('Ordem normal lista: ', end=' ')
for i in numeros:
    print(i, end=' ')

print('.')
print('Ordem inversa da lista: ',end=' ')
for c in reversed(numeros):
    print(c, end=' ')

