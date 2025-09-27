aluno = str(input('Qual o nome do aluno(a)? ')).strip()
disciplina = str(input('Qual disciplina gostaria de verificar? ')).strip()
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
n3 = float(input('Digite sua terceira nota: '))

med = (n1 + n2 + n3) / 3
print('\nAluno(a) {}, disciplina {}, média {:.1f}'.format(aluno, disciplina, med))
