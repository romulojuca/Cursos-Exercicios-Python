n = int(input('Digite numeros para somar ou [999] para parar!  '))
t = 0
c = 0

while n != 999:
    c += 1
    t = t + n
    n = int(input(' '))
    
print('Voce digitou {} numeros!'.format(c))
print('A soma foi de {}!'.format(t))
