n1 = float (input('digite um numero: '))
n2 = float (input('Digite outro numero: '))
n3 = float (input ('Digite outro numero: '))
if n1 < n2 and n1 < n3:
    print('{} é o menor numero.'.format(n1))
if n2 < n1 and n2 < n3:
    print ('{} é o menor numero.'.format(n2))
if n3 < n1 and n3 < n2:
    print ('{} é o menor numero.'.format (n3))
#Poderia ter atribuido o valor a uma variavel e falado que ela era a menor (ELIMINAVA 1 IF IGUAL A BAIXO)
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n2 and n3>n1:
    maior = n3
print('O Maior numero é {}.'.format(maior))
