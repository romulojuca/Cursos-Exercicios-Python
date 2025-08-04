num = int(input('Digite um numero para ver sua tabuada: '))

c = 0
n = 0
while num > 0:
    for n in range(1, 11):
        print(f'{num} X {n} = {num*n}')
        n += 1
    num = int(input(('Digite outro numero: ')))
    if num < 0:
        break

print('Fim !!')
