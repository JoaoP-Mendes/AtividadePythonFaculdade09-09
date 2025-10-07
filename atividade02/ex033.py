n1 = float(input('Digite o 1° número: '))
n2 = float(input('Digite o 2° número: '))
while True:
    print('''\nO que gostaria de fazer com esses número?
[ 1 ] - Verificar impar ou par
[ 2 ] - Verificar qual é positivo/negativo
[ 3 ] - Verificar inteiro ou decimal
[ 4 ] - Trocar números
[ 5 ] - Sair''')
    
    escolha = int(input('Digite a resposta: '))
    if escolha == 1: 
        if n1 % 2 == 0 and n2 % 2 == 0:
            print(f'{n1} e {n2} são números pares\n')
            
        elif n1 % 2 != 0 and n2 % 2 != 0:
            print(f'{n1} e {n2} são números impares\n')
            
        elif n1 % 2 == 0 and n2 % 2 != 0:
            print(f'{n1} é par e {n2} impar\n')
           
        elif n1 % 2 != 0 and n2 % 2 == 0:
            print(f'{n1} é impar e {n2} é par\n')

    continuar = str(input('\nQuer continuar? S/N ')).upper().strip()
    if continuar == 'S':
        continue
    elif continuar == 'N':
        break

    elif escolha == 2:
        if n1 > 0.0 and n2 > 0.0:
            print(f'{n1} e {n2} são números positivos.')

        elif n1 < 0.0 and n2 < 0.0:
            print(f'{n1} e {n2} são números negativos.')

        elif n1 > 0.0 and n2 < 0.0:
            print(f'{n1} é positivo e {n2} é negativo.')

        elif n1 < 0.0 and n2 > 0.0:
            print(f'{n1} é negativo e {n2} é positivo')