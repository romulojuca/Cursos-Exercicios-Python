print('\033[31m- '*30)

print(f"{'BANCO CENTRAL':>35}")
print('- '*30, end='')
print('\033[m')

valor = int(input('Valor do saque: '))
n50 = 0
n20 = 0
n10 = 0
n1 = 0
r = 0

while True:
    if valor >= 50:
        n50 = valor/50
        r = valor % 50
    else:
        r = valor
    if r >= 20:
        n20 = r/20
        r = r % 20
    if r >= 10:
        n10 = r/10
        r = r % 10
    if r >= 1:
        n1 = r

    break

if n50 > 0:
    print('Você receberá {:.0f} notas de R$50'.format(n50.__floor__()))
if n20 > 0:
    print('Você receberá {:.0f} notas de R$20'.format(n20.__floor__()))
if n10 > 0:
    print('Você receberá {:.0f} notas de R$10'.format(n10.__floor__()))
if n1 > 0:
    print('Você receberá {:.0f} notas de R$1'.format(n1))
