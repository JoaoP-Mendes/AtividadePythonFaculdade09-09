print('LOJA INFO-TUDO')
while True:
    nomeProduto = str(input('Qual seria o item? ')).strip()
    produto = float(input('Coloque o valor do item e veja o desconto: R$ '))
    desconto = produto - (produto * 10 / 100)
    print(f'O {nomeProduto} teve um desconto de 10% foi de {produto:.2f} para {desconto:.2f}')
    addProduto = str(input('\nGostaria de verificar outro item? S/N ')).strip().upper()

    if addProduto == 'S':
        continue
    elif addProduto == 'N':
        break
print('Muito obrigado, volte sempre!!')