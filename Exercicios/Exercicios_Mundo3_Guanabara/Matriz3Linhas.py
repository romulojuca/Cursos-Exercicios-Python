lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
numero = par = terceirac = maior = 0

for i in range(0, 3):
    for c in range(0, 3):
        lista[i][c] = int(input(f'Digite um valor para [{i}, {c}]'))

for e in range(0, 3):
    for i in range(0, 3):
        if lista[e][i] % 2 == 0:
            par += lista[e][i]
        if i == 2:
            terceirac += lista[e][i]
        if e == 1:
            if lista[e][i] > maior:
                maior = lista[e][i]

        print(f'[{lista[e][i]:^3}]', end='')
    print()
print(f'{'-=' * 30}')
print(f'A soma dos pares é de {par}')
print(f'A soma da terceira coluna é {terceirac}')
print(f'Maior valor da segudna linha é {maior}')
