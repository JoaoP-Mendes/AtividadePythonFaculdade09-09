pontos_juizes = []
nome = str(input('Qual o nome do atleta? '))

for c in range(0, 7):
    notas_juizes = float(input('Nota juiz: '))
    pontos_juizes.append(notas_juizes)
print(pontos_juizes)

media = sum(pontos_juizes) // 7
maior_nota = max(pontos_juizes)
menor_nota = min(pontos_juizes)

print(f"""Atleta {nome}
Maior nota {maior_nota}
Menor nota {menor_nota}
Média notas {media}""")