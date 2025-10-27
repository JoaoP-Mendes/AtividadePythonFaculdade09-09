nome = str(input('Digite o nome: ')).strip()
sexo = str(input('Coloque o sexo M/F: ')).strip().upper()
idade = int(input('Qual é a idade? '))

if idade == 0 or idade <= 2:
    if sexo == 'M':
        print('{}, tem {} anos de idade e é um bebezinho'.format(nome, idade))
    elif sexo == 'F':
        print('{}, tem {} anos de idade e é uma bebezinho'.format(nome, idade))

elif idade == 3 or idade <= 11:

    print('{}, tem {} anos de idade é apenas uma criança'.format(nome, idade))
elif idade == 12 or idade <= 21:
    print('{}, tem {} anos de idade é um(a) jovem'.format(nome, idade))
elif idade == 22 or idade <= 64:
    print('{}, tem {} anos de idade já é adulto'.format(nome, idade))
elif idade == 65 or idade <= 100:
    print('{}, tem {} anos de idade é um idoso'.format(nome, idade))
elif idade > 100:
    print('{}, tem {} anos de idade é um idosinho'.format(nome, idade))