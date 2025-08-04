from random import shuffle, choice, sample

a1 = str(input ('Nome'))
a2 = str( input ('nome'))
a3 = str( input ('nome'))
a4 = str (input ('nome'))
mylist = (a1, a2, a3, a4)#Coloca as variaveis na lista
r = choice(mylist)#Escolhe 1 nome da lista
print(r)

res = sample(mylist, len(mylist))#embaralha a lista  mostra toda a lista embaralhada
print(res)

frase = str (input ('Digite uma frase: ')).upper()
print ('A letra A aparece {} vezes na frase'.format(frase.upper().count('A')))
print ('Aparece a primeira vez na posição {}.'.format(frase.strip().find('A')+1))
print ('A ultima vez que aparece é na posição {}'.format(frase.strip().rfind('A')+1))

nome = str (input ('Digite seu nome completo'))
nomea = nome.split()
print ('Seu primeiro nome é {}.'.format(nomea[0]))
print ('Seu sobrenome é {}.'.format(nomea[len(nomea)-1]))
