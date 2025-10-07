# Entrada de dados
altura = float(input("Digite a altura em metros: "))
sexo = input("Digite o sexo (M para masculino, F para feminino): ").upper()

# Cálculo do peso ideal
if sexo == 'M':
    peso_ideal = (72.7 * altura) - 58
    print(f"Peso ideal para homem com {altura}m: {peso_ideal:.2f} kg")
elif sexo == 'F':
    peso_ideal = (62.1 * altura) - 44.7
    print(f"Peso ideal para mulher com {altura}m: {peso_ideal:.2f} kg")
else:
    print("Sexo inválido! Digite M para masculino ou F para feminino.")