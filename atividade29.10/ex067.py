print('INICIANDO JOGO')

while True: #Fazendo cadastro de usuario e senha
    print("""FAÇA O LOGIN PARA ENTRAR
    [ 1 ] - Fazer login
    [ 2 ] - Novo usuario""")
    opcao_login_novo = int(input(''))

    while opcao_login_novo != 1 and opcao_login_novo != 2:
        opcao_login_novo = int(input('ALGO DEU ERRADO. [ 1 ] para login ou [ 2 ] - para novo usuario: '))

    if opcao_login_novo == 1: 
        usuario = str(input('Coloque o seu nome de úsuario: '))
        senha = str(input('Coloque sua senha: '))

        while usuario not in Usuario or  senha not in SenhaUsuario:
            print('Usuario e/ou senha incorretos. TENTE NOVAMENTE\n')
            usuario = str(input('Usuario: '))
            senha = str(input('Digite a senha: ')) 

        if usuario in Usuario and senha in SenhaUsuario:
            print('Login feito! Iniciando jogo.\n')
            break

    elif opcao_login_novo == 2:
        Usuario = (str(input('Coloque um nome para o úsuario: ')))
        SenhaUsuario = (str(input('Defina uma senha: ')))
        print('Cadastro feito! Continue para o login\n')