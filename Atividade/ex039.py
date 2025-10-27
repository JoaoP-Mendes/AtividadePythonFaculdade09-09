while True: 
    dia = int(input('Digite o dia: '))
    while dia < 0 or dia > 30:
        dia = int(input('Dia invalido. Tente Novamente: '))
    
    mes = int(input('Coloque o número do mês: '))
    while mes < 0 or mes > 12:
        mes = int(input('Mês invalidao. Tente Novamente de 1 a 12: '))



    diasPassados = (mes - 1) * 30 + dia
    
    print(f"Se passararam desde o início do ano até {dia:02d}/{mes:02d} se passaram {diasPassados} dias.")

    decisao = str(input('Quer continuar? S/N: ')).upper().strip()
    if decisao == 'S':
        continue
    elif decisao == 'N':
        break
print('\nMUITO OBRIGADO, VOLTE SEMPRE')