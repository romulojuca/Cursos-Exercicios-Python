lista = [[], []]

for c in range(1, 8):
    num = int(input(f'Digite o {c}º valor: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)

lista[0].sort()
lista[1].sort()

print(f'Pares: {lista[0]}')
print(f'Impares: {lista[1]}')
