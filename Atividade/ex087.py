while True:
    entrada_kg = float(input("Informe o peso do transporte em kg: "))
    if entrada_kg <= 0.500:
        print("O valor do transporte deu R$1,00")
    elif entrada_kg > 0.500 and entrada_kg < 2.00:
        print("O valor do transporte deu R$2,20")
    elif entrada_kg > 2.00 and entrada_kg < 10.0:
        print("O valor do transporte deu R$3,70")