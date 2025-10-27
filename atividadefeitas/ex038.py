print('-' * 35)
print('RESTAURANTE QUILO SABOR')
print('-' * 35)

while True:
    print('O valor do KG é R$59.00')
    KG = float(input('Quantos KG o cliente consumiu? '))
    print(f'O cliente consumiu {KG} quilos, o valor refeição foi de R${KG * 59.00:.2f}')
    decisao = str(input('Verificar próximo cliente? S/N ')).upper().strip()
    if decisao == 'S':
        print('\n')
        continue
    elif decisao == 'N':
        break
print('MUITO OBRIGADO, VOLTE SEMPRE!!!')