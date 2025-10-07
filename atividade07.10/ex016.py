a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite mais ou número: '))

if a > b and b > c:
    print(f'O maior número é {a} e o menor é {c}.')
elif a > c and c > b:
    print(f'O maior número é {a} e o menor é {b}.')
elif b > a and a > c:
    print(f'O maior número é {b} e o menor é {c}.')
elif b > c and c > a:
    print(f'O maior número é {b} e o menor é o {a}')
elif c > b and b > a:
    print(f'O maior número é {c} e o menor é {a}')
elif c > a and a > b:
    print(f'O maior número é {c} e o menor é {b}.')