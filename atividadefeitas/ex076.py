notas = []
for i in range(0,4):
    nota = float(input(f'Digite sua {i + 1}° nota: '))
    notas.append(nota)

media = sum(notas) / 4
print(f'\nA média é {media}')