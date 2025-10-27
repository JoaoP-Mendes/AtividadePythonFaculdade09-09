nome = str(input('Digite seu nome: ')).strip()
numeroTitulo = int(input('Digite seu titulo eleitoral: (12 digitos): '))
numeroCandidato = int(input('Digite o numero do candidato: '))

print('\nNome: {}'.format(nome))
print('Nº título: {}'.format(numeroTitulo))
print('Nº candidato: {}'.format(numeroCandidato))

confirmar = str(input('Deseja confirmar? sim ou não:  '))

if confirmar.lower() == "sim":
    print('\nConfirmado')
else:
  print('\nTente novamente')
