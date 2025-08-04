from time import sleep

for c in range(10, -1, -1):
    print(c)
    sleep(1)
print ('BOOOMMMM !!')

for d in range(2, 51, 2):
    print (d)

a1 = 0
cont = 0
for e in range(1, 501, 2): #Separou todos os impares...
    if e % 3 == 0:         #Pegou apenas os divisiveis por 3...
        a1 = a1 + e
        cont = cont + 1
print ('Dos {} numeros divisiveis por 3, a soma é {}!'.format(cont, a1))
