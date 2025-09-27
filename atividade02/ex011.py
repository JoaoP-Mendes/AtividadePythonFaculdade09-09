nome = str(input('Digite o nome: ')).strip()
idade = int(input('Qual é a idade? '))

if idade == 0 and idade <= 2:
    print('{}, tem {} anos de idade e é um bebezinho'.format(nome, idade))
elif idade == 3 and idade <= 11:
    print('{}, tem {} anos de idade é apenas uma criança'.format(nome, idade))
elif idade == 12 and idade <= 21:
    print('{}, tem {} anos de idade é um(a) jovem'.format(nome, idade))