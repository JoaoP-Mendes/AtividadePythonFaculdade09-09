while True:
    valor = float(input('Qual o valor da compra? R$'))
    print("""Opções de pagamento
PIX
Dinheiro
Crédito""")
    formaPagamento = str(input('Qual a forma de pagamento: ')).upper().strip()
    
    if formaPagamento == 'PIX':
        desconto = valor - (valor * 10 / 100)
        print(f'O valor foi de R${valor:.2f}, para R${desconto:.2f}')

    elif formaPagamento == 'DINHEIRO':
        desconto = valor - (valor * 10 / 100)
        print(f'O valor foi de R${valor:.2f}, para R${desconto:.2f}')

    elif formaPagamento == 'CRÉDITO' or formaPagamento == 'CREDITO':
        parcelas = int(input('Será quantas parcelas? (1 para à vista) '))

        if parcelas == 1:
            desconto = valor - (valor * 5 / 100)
            print(f'O valor foi de R${valor:.2f}, para R${desconto:.2f}')

        elif parcelas == 2: 
            valorparcela = valor / parcelas
            print(f'O valor ficou duas parcelas de R${valorparcela:.2f}')
        elif parcelas >= 3:
            valorparcela = valor / parcelas
            print(f'O valor ficou duas parcelas de R${valorparcela:.2f}')