aluno = str(input('Digite seu nome completo: ')).strip()
disciplina = str(input('Coloque o nome da disciplina: ')).strip()

nota1 = float(input('\nColoque a nota da sua primeira prova: '))
nota2 = float(input('Coloque a nota da sua segunda prova: '))
nota3 = float(input('Coloque a nota da sua terceira prova: '))

med = (nota1 + nota2 + nota3) / 3
print('\nA média do aluno {} é {:.1f}.'.format(aluno,med))

if med >= 6 :
    print('O aluno foi aprovado! Parabens')
else : 
    print('Infelizmente não foi dessa vez, o aluno não passou.')
