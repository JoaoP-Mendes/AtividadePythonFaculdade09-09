distancia = float(input('Qual a distância em KM? '))
litros = float(input('A cada quantos KM seu carro consome o litro? '))


Litros_usados = distancia / litros 
custo = Litros_usados * 5.79 
#5.79 é o preço da gasolina, fiz com base em pesquisa no google no preço da cidade

print('O custo aproximado da viagem será R${:.2f}'.format(custo))
