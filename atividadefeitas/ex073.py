quantidade_votos = 0
votos_jose = 0
votos_joao = 0
votos_jairo = 0
votos_jeferson = 0
votos_brancos = 0
votos_nulos = 0


print('Iniciando votação')
print("""Informe o respectivo número para votação
[ 0 ] - Sair programa
[ 1 ] - José
[ 2 ] - João
[ 3 ] - Jairo
[ 4 ] - Jeferson
[ 5 ] - voto nulo
[ 6 ] - voto branco""")


while True:

    voto = int(input('informe o número do seu voto: '))
    while voto > 6 or voto < 0:
        voto = int(input('Voto não confirmado. Tente novamente: '))

    if voto == 1:
        print('Voto confirmado!')
        quantidade_votos += 1
        votos_joao += 1
        print('\n')
        continue


    elif voto == 2:
        print('Voto confirmado!')
        quantidade_votos += 1
        votos_jose += 1
        print('\n')
        continue


    elif voto == 3:
        print('Voto confirmado!')
        quantidade_votos += 1
        votos_jairo += 1
        print('\n')
        continue

    elif voto == 4:
        print('Voto confirmado!')
        quantidade_votos += 1
        votos_jeferson += 1
        print('\n')
        continue

    elif voto == 5:
        print('Voto nulo confirmado!')
        quantidade_votos +=1
        votos_nulos += 1
        print('\n')
        continue

    elif voto == 6:
        print('Voto confirmado!')
        quantidade_votos += 1
        votos_brancos += 1
        print('\n')
        continue
    
    elif voto == 0:
        break

print(f'Houveram {quantidade_votos} votos no total')
print('-=-' * 25)
print(f'O canditado José teve {votos_jose} votos')
print(f'O canditado João teve {votos_joao} votos')
print(f'O canditado Jairo teve {votos_jairo} votos')
print(f'O canditado Jeferson teve {votos_jeferson} votos')
print('-=-' * 25)
print(f'Houveram {votos_nulos} votos nulos.')
print(f'Houveram {votos_brancos} votos em branco.')

porcentagem_votos_brancos = votos_brancos * quantidade_votos / 100

print(f'Houveram {porcentagem_votos_brancos}% de votos em branco em relação a  {quantidade_votos} de votos')