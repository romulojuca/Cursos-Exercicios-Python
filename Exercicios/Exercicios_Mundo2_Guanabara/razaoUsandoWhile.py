razao = float(input('Razão: '))
pt = float(input('Primeiro Termo: '))
c = 10


while c > 0:
    print('{:.0f}'.format(pt), end='')
    print(', ' if c > 1 else '!! ', end='')
    pt = pt + razao
    c = c - 1

print('FIM')
