lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = soma = 0

for l in range(0, 3):
    for c in range(0, 3):
        lista[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if lista[l][c] % 2 == 0:
            par += lista[l][c]

for p, v in enumerate(lista):
    print(v)
print(f'A soma dos valores pares é {par}')

for l in range(0, 3):
    for c in range(0, 3):
        if c == 2:
            soma += lista[l][c]
print(f'A soma dos valores da terceira coluna é {soma}')

for p, v in enumerate(lista[1]):
    if p == 0:
        maior = v
    elif v > maior:
        maior = v
print(f'O maior valor da segunda linha é {maior}')
