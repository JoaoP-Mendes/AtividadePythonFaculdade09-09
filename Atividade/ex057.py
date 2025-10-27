print('-=-' * 20)
print('LA RESTURANTE')
print('-=-' * 20)


print("""CARDÁPIDO E PREÇOS
1 - Gorgonzola...............R$83.90
2 - Mozzarella de Búfala.....R$81.90
3 - Presunto Parma...........R$95.95
4 - Queijo Brie..............R$94.90
5 - Queijos com Funghi.......R$83.90""")
print('-=-' * 20)


valorpratos = 0
while True:
    add = int(input('Qual prato gostaria de adicionar? '))
    if add == 1:
        print('Gorgonzola adicionado!!')
        valorpratos += 83.90
        decisao = str(input('Quer adicionar outro prato? S/N '))
        while not decisao in 'SsNn':
            decisao = str(input('Algo deu errado, quer adicionar outro prato? S/N '))
        if decisao in 'Nn':
           break

        elif decisao in 'Ss':
            decisao2 = str(input('Quer ver o cardápido novamente? S/N '))
            while not decisao2 in 'SsNn': 
                decisao2 = str(input('Algo deu errado. Quer ver o cardápido novamente? S/N '))
            if decisao2 in 'Ss':
                
                print('\n')
                print('-=-' * 15)
                print("""CARDÁPIDO E PREÇOS
1 - Gorgonzola...............R$83.90
2 - Mozzarella de Búfala.....R$81.90
3 - Presunto Parma...........R$95.95
4 - Queijo Brie..............R$94.90
5 - Queijos com Funghi.......R$83.90  """)
                print('-=-' * 15)

            elif decisao2 in 'Nn':
                continue

    elif add == 2:
        print('Mozzarella de Búfala adicionado!!')
        valorpratos += 81.90
        decisao = str(input('Quer adicionar outro prato? S/N '))
        while not decisao in 'SsNn':
            decisao = str(input('Algo deu errado, quer adicionar outro prato? S/N '))
        if decisao in 'Nn':
            break

        elif decisao in 'Ss':
            decisao2 = str(input('Quer ver o cardápido novamente? S/N '))
            while not decisao in 'SsNn': 
                decisao2 = str(input('Algo deu errado. Quer ver o cardápido novamente? S/N '))
            if decisao2 in 'Ss':
                
                print('\n')
                print('-=-' * 15)
                print("""CARDÁPIDO E PREÇOS
1 - Gorgonzola...............R$83.90
2 - Mozzarella de Búfala.....R$81.90
3 - Presunto Parma...........R$95.95
4 - Queijo Brie..............R$94.90
5 - Queijos com Funghi.......R$83.90  """)
                print('-=-' * 15)

            elif decisao2 in 'Nn':
                continue

    elif add == 3:
        print('Presunto de Parma adicionado!!')
        valorpratos += 95.95
        decisao = str(input('Quer adicionar outro prato? S/N '))
        while not decisao in 'SsNn':
            decisao = str(input('Algo deu errado, quer adicionar outro prato? S/N '))
        if decisao in 'Nn':
            break

        elif decisao in 'Ss':
            decisao2 = str(input('Quer ver o cardápido novamente? S/N '))
            while not decisao2 in 'SsNn': 
                decisao2 = str(input('Algo deu errado. Quer ver o cardápido novamente? S/N '))
            if decisao in 'Ss':
                
                print('\n')
                print('-=-' * 15)
                print("""CARDÁPIDO E PREÇOS
1 - Gorgonzola...............R$83.90
2 - Mozzarella de Búfala.....R$81.90
3 - Presunto Parma...........R$95.95
4 - Queijo Brie..............R$94.90
5 - Queijos com Funghi.......R$83.90  """)
                print('-=-' * 15)

            elif decisao2 in 'Nn':
                continue


    elif add == 4:
        print('Queijo de Brie adicionado!')
        valorpratos += 94.90
        decisao = str(input('Quer adicionar outro prato? S/N '))
        while not decisao in 'SsNn':
            decisao = str(input('Algo deu errado, quer adicionar outro prato? S/N '))
        
        
        if decisao in 'Nn':
            break

        elif decisao in 'Ss':
            decisao2 = str(input('Quer ver o cardápido novamente? S/N '))
            while not decisao2 in 'SsNn': 
                decisao2 = str(input('Algo deu errado. Quer ver o cardápido novamente? S/N '))
            if decisao2 in 'Ss':

                print('\n')
                print('-=-' * 15)
                print("""CARDÁPIDO E PREÇOS
1 - Gorgonzola...............R$83.90
2 - Mozzarella de Búfala.....R$81.90
3 - Presunto Parma...........R$95.95
4 - Queijo Brie..............R$94.90
5 - Queijos com Funghi.......R$83.90  """)
                print('-=-' * 15)

            elif decisao2 in 'Nn':
                continue
    
    elif add == 5:
        print('Queijos com Funghi adicionado')
        valorpratos += 83.90
        decisao = str(input('Quer adicionar outro prato? S/N '))
        while not decisao in 'SsNn':
            decisao = str(input('Algo deu errado, quer adicionar outro prato? S/N '))
        
        
        if decisao in 'Nn':
           break


        elif decisao in 'Ss':
            decisao2 = str(input('Quer ver o cardápido novamente? S/N '))
            while not decisao2 in 'SsNn': 
                decisao2 = str(input('Algo deu errado. Quer ver o cardápido novamente? S/N '))
            if decisao in 'Ss':

                print('\n')
                print('-=-' * 15)
                print("""CARDÁPIDO E PREÇOS
1 - Gorgonzola...............R$83.90
2 - Mozzarella de Búfala.....R$81.90
3 - Presunto Parma...........R$95.95
4 - Queijo Brie..............R$94.90
5 - Queijos com Funghi.......R$83.90  """)
                print('-=-' * 15)

            elif decisao2 in 'Nn':
                continue

gorjeta = str(input(f'\nA conta deu R${valorpratos:.2f}, gostaria de adicionar 10% para gorjeta do garfom? S/N '))
if gorjeta in 'Ss':
    valorGojeta = valorpratos * 10 / 100
    valorTotal = valorpratos + valorGojeta
    print(f'A conta total deu R${valorTotal:.2f}, valor pratos R${valorpratos:.2f} + valor R${valorGojeta:.2f}')
    print('Muito obrigado volte sempre!')

elif gorjeta in 'Nn':
    print(f'A conta deu R${valorpratos:.2f}, muito obrigado volte sempre!')