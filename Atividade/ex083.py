soma = []
soma_total = 0

for numero in range(0, 5):
    numero = int(input("Digite um número: "))
    soma_total += numero
    soma.append(numero)

print(f"\nA soma deu {sum(soma)}.")
for item in soma:
    print(item)