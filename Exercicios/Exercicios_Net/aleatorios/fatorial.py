numero = int(input('Fatorial de: '))
cont = total = 1

for e in range(numero, 0, -1):
    if e == numero:
        print(f'{e}!={e}x', end='')
    elif e == 1:
        print('1=', end='')
    else:
        print(f'{e}x', end='')
    cont = cont * e
print(cont)
