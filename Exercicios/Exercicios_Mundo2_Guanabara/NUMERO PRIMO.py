num = int (input('Digite um numero inteiro: '))

t = 0
for c in range (1, num + 1):
    if num % c == 0:
        t = t + 1
        print('\033[33m', end='')
    else:
        print('\033[31m', end='')
        
    print ('{} '.format(c), end='')
print('\n\033[mO numero {} foi divisivel {} vezes! '.format(num, t))
if t == 2:
    print('{} é numero primo!!'.format(num))
else:
    print('{} não é numero primo!!'.format(num))
