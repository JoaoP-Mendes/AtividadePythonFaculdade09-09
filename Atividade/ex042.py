totallitros = 0
while True: 

      Lata350ml = 0.350
      Garrafa600ml = 0.600
      Garrafa2L = 2.00

      print('-' * 50)
      print(f"""Refrigerantes
            [ 1 ] - Lata 350ml
            [ 2 ] - Garrafa 600ml
            [ 3 ] - Garrafa 2L
            [ 4 ] - Sair""")

      
      EscolhaCola = int(input('Qual qual tamanho de refrigerante você gostaria? '))
      while EscolhaCola != 1 and EscolhaCola != 2 and EscolhaCola != 3 and EscolhaCola != 4: 
            EscolhaCola = int(input('Escolha uma opção valida: '))

      if EscolhaCola == 1:
            quantidade = int(input('Quantas latas você quer comprar? '))
            litros = quantidade * Lata350ml
            totallitros += litros
            print(f'Se você comprar mais {quantidade} latas de 350 ml você irá comprar {litros:.1f}L\n')
            
            print('-' * 50)
            decisao = str(input('Quer adiocinar outro refrigerante? S/N ')).upper().strip()
            if decisao == 'S':
                  continue
            elif decisao == 'N':
                  break


      elif EscolhaCola == 2:
            quantidade = int(input('Quantas garrafas você quer comprar? '))
            litros = quantidade * Garrafa600ml
            totallitros += litros
            print(f'Se você comprar mais {quantidade} garrafas de 600ml você irá comprar {litros:.1f}L\n')

            print('-' * 50)
            decisao = str(input('Quer adicionar outro refrigerante? S/N ')).upper().strip()
            if decisao == 'S':
                  totallitros += litros
                  continue
            elif decisao == 'N':
                  break


      elif EscolhaCola == 3:
            quantidade = int(input('Quantas garrafas você quer comprar? '))
            litros = quantidade * Garrafa2L
            totallitros += litros
            print(f'Se você comprar mais {quantidade} de garrafas de 2 L você irá comprar {litros:.1f}L\n')

            print('-' * 50)
            decisao = str(input('Quer adicionar outro refrigerante? S/N ')).upper().strip()
            if decisao == 'S':
                  continue
            elif decisao == 'N':
                  print('-' * 50)
                  break

      elif EscolhaCola == 4:
            break
print(f'\nNo total você comprou {totallitros:.1f}L de refrigerante')

#Possiveis atualizações para tentar no futuro:
#- Colocar a opção para o cliente ver quantos litros ele já tem