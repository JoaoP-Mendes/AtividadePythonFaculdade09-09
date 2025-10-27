n = int(input('Digite um número: '))
if n < 0:
    print(f'O número {n} é negativo')
elif n > 0:
    print(f'O número {n} é positivo')
elif n == 0:
    print(f'O número {n} não é positivo nem negativo')