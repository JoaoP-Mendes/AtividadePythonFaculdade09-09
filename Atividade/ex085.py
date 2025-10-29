hora_trabalhada = 6.40
while nome_professora1 != 'Sair':
    nome_professora1 = str(input('Informe o nome da primeira professora: ')).title()
    nome_professora2 = str(input('Informe o nome da segunda procesora: ')).title()

    quantidade_horas_pf1 = int(input(f'Quantas horas/aulas a professora {nome_professora1}: '))
    salario_professora1 = quantidade_horas_pf1 * hora_trabalhada


    quantidade_horas_pf2 = int(input(f'Quantas horas/aulas a professora {nome_professora2}: '))
    salario_professora2 = quantidade_horas_pf1 * hora_trabalhada

    if salario_professora1 > salario_professora2:
        print(f"A professora {nome_professora1} ganha R${salario_professora1:.2f}, enquanto a professora {nome_professora2} ganha R${salario_professora2:.2f}")
    elif salario_professora1 == salario_professora2:
        print(f"Professora {nome_professora1} e {nome_professora2} ganharam o mesmo valor de salário R${salario_professora1:.2f}")
    if salario_professora1 < salario_professora2:
        print(f"A professora {nome_professora2} ganha R${salario_professora2:.2f}, enquanto a professora {nome_professora1} ganha R${salario_professora1:.2f}")
print("Programa encerrado!")