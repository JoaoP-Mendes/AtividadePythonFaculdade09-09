while True:
    nome = str(input('Qual seu nome? ')).strip()
    sexo = str(input('Qual seu sexo? M/F')).strip().upper()
    while sexo not in 'FM':
        sexo = str(input('Inválido, tente novamente. Qual seu sexo? M/F '))
    estadoCivil = str(input('Qual seu estado civil? ')).strip().upper()
    
    if sexo == 'F' and estadoCivil == 'CASADA' or estadoCivil == 'CASADO':
        tempoCasamento = int(input('Quantos anos você está casada? '))
        if tempoCasamento < 1:
            print(f'Nome: {nome}, sexo: {sexo} estado civil: {estadoCivil} a menos de {tempoCasamento} ano')
        
        elif tempoCasamento == 1:
            print(f'Nome: {nome}, sexo: {sexo} estado civil: {estadoCivil} a {tempoCasamento} ano')
        
        elif tempoCasamento > 1:
            print(f'Nome: {nome}, sexo: {sexo} estado civil: {estadoCivil} a {tempoCasamento} ano')

    
    else:
        print(f'Nome: {nome}, sexo: {sexo} estado civil: {estadoCivil}')
