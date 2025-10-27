print('Iniciando contador de números impares | Coloque -999 para sair.')
cont = 0
while True:
    numeros = int(input('Digite um número: '))
    if numeros == -999:
        break
    if numeros % 2 == 1:
        cont += 1
print(f'Foram digitados {cont} números impares.')