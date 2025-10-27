camisetaP = 10.00
camisetaM = 12.00
camisetaG = 15.00

qntcamisetaP = 0
qntcamisetaM = 0
qntcamisetaG = 0

valortotalcamisetaP = 0
valortotalcamisetaM = 0
valortotalcamisetaG = 0

while True:
    print('''TABELA PREÇOS
[ 1 ] - Camiseta P : R$10.00
[ 2 ] - Camiseta M : R$12.00
[ 3 ] - Camiseta G : R$15.00''')
    camiseta = str(input('Informe o tamanho da camiseta para iniciar: ')).upper().strip()
   
    if camiseta == 'P': #Camisetas P
        quantidade = int(input('Informe a quantidade de camisetas P para adicionar no carrinho: '))
        qntcamisetaP += quantidade
        valortotalcamisetaP = quantidade * camisetaP
        decisao = str(input('Quer adionar outro tamanho? S/N ')).upper().strip()
        if decisao == 'S':
            print('\n')
            continue
        elif decisao == 'N':
            print('\n')
            break
    
    elif camiseta == 'M': #Camisetas M
        quantidade = int(input('Informe a quantidade de camisetas M para adicionar no carrinho: '))
        qntcamisetaM += quantidade
        valortotalcamisetaM = quantidade * camisetaM
        decisao = str(input('Quer adionar outro tamanho? S/N ')).upper().strip()
        if decisao == 'S':
            print('\n')
            continue
        elif decisao == 'N':
            print('\n')
            break
    
    elif camiseta == 'G': #Camisetas G
        quantidade = int(input('Informe a quantidade de camisetas G para adicionar no carrinho: '))
        qntcamisetaG += quantidade
        valortotalcamisetaG = quantidade * camisetaG
        decisao = str(input('Quer adicionar outro tamanhos? S/N ')).upper().strip()
        if decisao == 'S':
            print('\n')
            continue
        elif decisao == 'N':
            print('\n')
            break
    
print(f'Foram adicionadas no carrinho:')
print(f'{qntcamisetaP} camisetas do tamanho P - R${valortotalcamisetaP:.2f}')
print(f'{qntcamisetaM} camisetas do tamanho M - R${valortotalcamisetaM:.2f}')
print(f'{qntcamisetaG} camisetas do tamanho G - R${valortotalcamisetaG:.2f}')
print(f'O valor total da compra é R${valortotalcamisetaP + valortotalcamisetaM + valortotalcamisetaG:.2f}')
