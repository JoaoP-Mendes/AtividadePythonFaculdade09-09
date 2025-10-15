soma: 0
while True:
    somavalor = int(input('Coloque o número e veja soma / coloque -999 para sair: '))
    somavalor += soma
    if somavalor == -999:
        break
    print(somavalor)
