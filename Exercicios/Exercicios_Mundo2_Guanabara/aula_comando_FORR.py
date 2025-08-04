i = int (input('Inicio: '))
f = int (input('Fim: '))
p = int (input('Passo '))
for r in range (i, f+1, p):
    print(r)
print ('FIM! '*10)


n = int (input('Digite um numero: '))
for t in range (0, n+1):
    print(t)
print('FIM! '*10)


for c in range(0,2):#PRINTA 2x, desconsidera o ultimo numero!
    print ('Oi')
print ('FIM! '*10)

for c in range(7, -1, -2):#printa de 7 até 0 de 2 em 2!
    print (c)
print ('FIM! '*10)

for c in range(0, 6, 2):#PRINTA de 0 a 5 de 2 em 2!
    print (c)
print ('FIM! '*10)
