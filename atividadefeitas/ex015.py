while True:
    sexo = str(input('Informe o sexo M/F: ')).upper().strip()
    if sexo == 'M':
        print('Sexo Masculino.')
        descisao = str(input('Gostaria de verificar outro? S/N ')).upper().strip()
        if descisao == 'S':
            continue
        elif descisao == 'N':
            break

    elif sexo == 'F':
        print('Sexo Feminino.')
        descisao = str(input('Gostaria de verificar outro? S/N ')).upper().strip()
        if descisao == 'S':
            continue
        elif descisao == 'N':
            break

    elif sexo != 'M' and sexo != 'F':
        print('\nTENTE NOVAMENTE. ALGO DEU ERRADO.')
        
       

    