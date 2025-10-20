print('Iniciando contador de número | Coloque -1 para sair.')
cont = 0
while True:
    numeros = int(input('Digite um número: '))
    if numeros == -1:
        break
    cont += 1
print(f'Foram digitados {cont} números.')