numeroConta = '123456-7'
saldo = 0
debito = 0
credito = 0
saldoAtual =0


while True:
    saldo = float(input('Qual o saldo da conta? R$'))
    debito = float(input('Quantos você está devendo: R$'))
    credito = float(input('Quantos você recebeu de crédito? R$'))
    saldoAtual = saldo - debito + credito
    
    print(f'O saldo atual é {saldoAtual:.2f}')
    decisao = str(input('Quer verificar novamente? S/N ')).upper().strip()
    if decisao == 'S':
        continue
    elif decisao == 'N':
        break
print('MUITO OBRIGADO! VOLTE SEMPRE')


"""totalAlunos = int(input('Digite o total de alunos: '))
for numero in range(totalAlunos):
    print("Aluno ", totalAlunos)"""