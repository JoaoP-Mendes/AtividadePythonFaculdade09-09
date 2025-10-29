numeros = []
lista_pares = []
lista_impares = []
quantidade_pares = 0
quantidade_impares = 0

for numero in range(0, 10):
    numero = int(input('informe um número: '))
    if numero % 2 == 0:
        lista_pares.append(numero)
        quantidade_pares += 1
    elif numero % 2 != 0:
        lista_impares.append(numero)
        quantidade_impares += 1

print(f"Foram digitados {quantidade_pares} números pares eles foram {lista_pares}")
print(f"Foram digitados {quantidade_impares} números impares eles foram {lista_impares}")