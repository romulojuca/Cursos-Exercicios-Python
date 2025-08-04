'''from math import factorial

n = int(input('Digite um numero para ver seu fatorial! '))
f = factorial(n)
print ('O fatorial de {} é {}'.format(n, f))'''
## Metodo com biblioteca de cima!

n = int(input('Digite o numero para ver seu fatorial! '))
c = n
t = 1

print('Calculando fatorial de {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    t = t * c
    c = c - 1
print(t)
