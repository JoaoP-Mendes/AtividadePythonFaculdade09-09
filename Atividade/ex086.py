while True:
    salario = float(input("Informe o seu salário R$"))
    financa = float(input("Informe o valor do financiamento R$"))
    if financa <= salario * 5:
        print("Financiamento Concedido")
    elif financa > salario * 5:
        print('Financiamento negado')
    print("Obrigado por consultar!")