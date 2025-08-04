nome = str (input ('Digite seu nome completo: ')).strip()
print ('Seu nome maiusculo eh {}.'.format(nome.upper()))
print ('Seu nome minusculo eh {}.'.format(nome.lower()))
print ('Seu nome completo tem {} letras.'.format (len(nome)-nome.count(' '))) #len conta os caracteres

nome1 = nome.split()
print ('Seu primeiro nome tem {} letras'.format (len(nome1 [0])))

n = str (input ('Digite um numero de 0 a 9999: '))
n1 = (n.split())
print ('Milhar eh: {}'.format(n1[0][0]))
print ('Centena eh: {}'.format(n1[0][1]))
print ('Dezena eh: {}'.format(n1[0][2]))
print ('Unidade eh: {}'.format(n1[0][3]))