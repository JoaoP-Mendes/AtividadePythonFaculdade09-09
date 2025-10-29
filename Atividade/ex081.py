estoque = {"Arroz": 30, "Feijão": 30, "Açucar": 25, "Leite": 10,
           "Detergente":25, "Água Sanitária": 15, "Pasta de dente": 15,
           "Alface": 10, "Tomate": 15, "Repolho" : 20}

while True:
    verificar_no_estoque = str(input("Qual compra gostaria de verificar no estoque? ")).title()
    if verificar_no_estoque in estoque:
        print("O item está no estoque!")
        print(f"{verificar_no_estoque} : {estoque[verificar_no_estoque]} no estoque")
        continue
    elif verificar_no_estoque not in estoque:
        print(f"Infelizmente não o item {verificar_no_estoque} não está disponível no estoque")
        continue