n = int(input('Quantos termos da sequencia de Fibonacci? '))
p = 0
s = 1
c = 3
t = 0

print('A sequencia ficará {} -> {} -> '.format(p, s), end='')

while c <= n:
    t = p + s
    print('{} -> '.format(t), end='')
    p = s
    s = t
    c += 1

print('FIM!')
