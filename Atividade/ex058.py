print('COMEÇANDO PROGRAMA')
resposta = str(input('Vamos começar? S/N ')).upper().strip()
while resposta != 'N':
    print('PROGRAMA PARA VER INTERVALOS DE NÚMEROS')
    comeco = int(input('Quer começar com qual número? '))
    final = int(input('Até qual número? '))
    print(f'Os números que estão entre {comeco} e {final} são: \n')
    for intervalo in range(comeco + 1, final):
        print(intervalo)
    
    resposta = str(input('Quer continuar? S/N ')).upper().strip()
    if resposta == 'S':
        continue

print('PROGRAA ENCERRADO!')