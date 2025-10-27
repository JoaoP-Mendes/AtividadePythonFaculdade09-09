aluno = str(input('Digite seu nome: '))
turno = str(input(f'{aluno}, informe o turno que estuda: M - matutino V - vespertino N - noturno')).strip()

while turno not in 'MmVvNn':
    turno = str(input('Periodo invalido. Informe o período da sua aula: ')).strip()
if turno in 'Mm':
    print(f'Bom dia! Bem-vindo(a) a aula')
elif turno in 'Vv':
    print(f'Boa tarde! Bem-vindo(a) a aula')
elif turno in 'Nn':
    print(f'Boa noite! Bem-vindo(a) a aula')