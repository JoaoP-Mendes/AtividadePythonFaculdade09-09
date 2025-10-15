while True: 
      Lata350ml = 0.350
      Garrafa600ml = 0.600
      Garrafa2L = 2.00

      print(f"""Refrigerantes
            [ 1 ] - Lata 350ml
            [ 2 ] - Garrafa 600ml
            [ 3 ] - Garrafa 2L""")


      EscolhaCola = int(input('Qual qual tamanho de refrigerante você gostaria? '))
      if EscolhaCola == 1:
      quantidade = int(input('Quantas latas você quer comprar? '))
      litros = quantidade * Lata350ml
      print(f'Se você comprar {quantidade} Latas de 350ml, você vai comprar {litros:.1f}L')
      elif EscolhaCola == 2:
      quantidade = int(input('Quantas garrafas você quer comprar? '))
      litros = quantidade * Garrafa600ml
      print(f'Se você comprar {quantidade} de garrafas de 600ml, você vai comprar {litros:.1f}L')
      elif EscolhaCola == 3:
      quantidade = int(input('Quantas garrafas você quer comprar? '))
      litros = quantidade * Garrafa2L
      print(f'Se você comprar {quantidade} de garras de 2 L, você vai comprar {litros:.1f}L')

   