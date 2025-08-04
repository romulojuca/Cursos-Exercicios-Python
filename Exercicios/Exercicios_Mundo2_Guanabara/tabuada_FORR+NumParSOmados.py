n = int (input('Digite um numero para ver sua tabuada: '))
x = 0
for c in range (0, 10):
    x += 1
    print('{} X {} = {}'.format(x, n, (x*n)))


soma = 0
cont = 0
for w in range (1, 7):
    num = int (input('Digite o {}º numero: '.format(w)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('{} desses numeros são PARES, a soma deles é {}!'.format(cont, soma))
