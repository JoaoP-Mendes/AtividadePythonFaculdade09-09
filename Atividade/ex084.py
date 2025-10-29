import random
vetor = []

for i in range(0, 10):
    numeros_gerados_pela_maquina = random.randint(1, 100)
    vetor.append(numeros_gerados_pela_maquina)

verificar_lista = 0
while verificar_lista != -1:
    verificar_lista = int(input('Verifique se o número está no vetor ou -1 para sair: '))
    if verificar_lista in vetor:
        print(f"O número está no vetor!")
    else:
        print("O número informado não está no vetor.")
print("Programa encerrado!")
print(f"Os números na lista são: {vetor}")