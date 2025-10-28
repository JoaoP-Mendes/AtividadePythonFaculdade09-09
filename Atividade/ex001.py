while True:
    nome = str(input('Digite o seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Qual seu sexo? '))
    telefone = str(input('Qual seu contato? '))
    endereço = str(input('Qual o endereço? '))


    print('\nOlá, {} você tem {} anos de idade ,sexo {},\nseu telefone é {} e sua residência {}'.format(nome, idade, sexo, telefone, endereço))
    confirmar = str(input('Os dados estão corretos? s/n '))

    if confirmar in 'Ss:': 
        print('Dados confirmado! ')
        continue
    elif confirmar in 'Nn':
        print('Faça novamente o cadastro')
        break
