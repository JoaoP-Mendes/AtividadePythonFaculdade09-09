alunos = 50
sexoFAlt = 0
sexoMBom = 0


for aluno in range (1, alunos + 1):
    sexo = str(input(f'Coloque o sexo M/F do {aluno}° aluno(a): ')).upper().strip()
    while sexo not in 'MF':
        sexo = str(input(f'ALGO DEU ERRADO. Coloque o Sexo do {aluno}° aluno. M ou F: ')).upper().strip()
    
    altura = float(input('Coloque a altura do aluno(a): '))
    
    statusFisico = int(input('Coloque o status físico do aluno: 1 - bom, 2 - regular, 3 - ruim: '))
    while altura != 1 or altura != 2 or altura != 3:
        statusFisico = int(input('Algo deu errado, COLOQUE: 1 - bom, 2 - regular, 3 - ruim: '))

    if sexo == 'F' and altura > 1.70:
        sexoFAlt += 1

    elif sexo == 'M' and statusFisico == 1:
        sexoMBom += 1

    

"""numero = int(input('Digite um número para a soma: '))
soma = 0
while numero != 0:
    soma = soma + numero
    numero = int(input('Digite um número para a soma: '))


print(soma)"""
