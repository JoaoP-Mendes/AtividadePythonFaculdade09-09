peso = float(input('Informe a quantidade de Kilos: '))
if peso <= 50.0:
    print('Peso dentro do Regulamento. Nenhum problema identificado.')
elif peso > 50.0:
    kg_ultrapassados = peso - 50.0
    multa = kg_ultrapassados * 4.0
    print(f'{kg_ultrapassados}kg ultrapassados, será aplicado uma multa de R${multa:.2f}')