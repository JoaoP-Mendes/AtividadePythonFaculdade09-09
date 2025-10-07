print('-=-=-=-=-=-=-=-=-=-= Verificação número se maior ou menor que 10 -=-=-=-=-=-=-=-=-=-=')
num = float(input('Digite um número: '))
print('-=-=-=-=-=-=-=-=-=-= -=-=-=-=-=-=-=-=-=-=- =-=-=-=-=-=-=-=-=-= -=-=-=-=-=-=-=-=-=-=-=')



if num > 10:
    print('O número {} é maior que 10'.format(num))
elif num < 10:
    print('O número {} é menor que 10'.format(num))
elif num == 10:
    print('O número digitado tem o mesmo valor que 10')
