media = []

for aluno in range(0, 10):
    MEDIA = []
    for n in range(0, 4):
        nota = float(input(f'Digite sua {n + 1}º nota: '))
        MEDIA.append(nota)
    valormedia = sum(MEDIA) / 4
    media.append(valormedia)
    print('-=-' * 15)

print(media)
media_maior = 0

for a, m in enumerate(media):
    print(f'A {a + 1}º média é: {m}')
    if m >= 7.0:
        media_maior += 1
print(f'Houveram {media_maior} médias maiores ou iguais a 7.0')
