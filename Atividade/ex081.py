estoque = {"Arroz": 30, "Feijão": 30, "Açucar": 25, "Leite": 10,
           "Detergente":25, "Água Sanitária": 15, "Pasta de dente": 15,
           "Alface": 10, "Tomate": 15, "Repolho" : 20}

while True:
    verificar_no_estoque = str(input("Qual compra gostaria de verificar no estoque? ")).title()
    if verificar_no_estoque in estoque:
        print()