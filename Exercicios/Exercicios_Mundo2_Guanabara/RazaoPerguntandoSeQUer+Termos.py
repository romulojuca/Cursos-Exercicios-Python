pt = float(input('Primeiro Termo: '))
razao = float(input('Razão: '))

x = 1
c = 10

while c > 0:
    print('{:.2f}'.format(pt), end='')
    print(', ' if c > 1 else '!!', end='')
    pt = pt + razao
    c = c - 1
    if c == 0:
        print('\nVocê gostaria de ver mais quantos termos? ', end='')
        x = int(input(' '))
        if x == 0:
            print('FIM!!!')
        else:
            c = x
print('')
