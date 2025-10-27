while True:
    sexo = str(input('Digite o sexo M/F: ')).upper().strip()
    while sexo not in 'MF':
        sexo = str(input('Algo deu errado. Tente novamente: ')).upper().strip()
    altura = float(input('Coloque sua altura: '))
    if sexo == 'M':
        peso = (72.7 * altura) - 58
        print(f"\nO peso ideal para o sexo masculino de {altura}m é {peso:.2f}KG")
    elif sexo == 'F':
        peso = (62.1 * altura) - 44.7
        print(f'\nO peso ideal para o sexo feminino de {altura}m é {peso:.2f}KG')
    
    decisao = str(input('Gostaria de fazer novamente? S/N ')).upper().strip()
    if decisao == 'S':
        continue
    elif decisao == 'N':
        break
print('MUITO OBRIGADO, VOLTE SEMPRE!')
