box = []
R = 's'

while True:
    if R == 's':
        box.append(int(input('Digite um numero: ')))
        R = input('Deseja continuar? [s/n]')
    else:
        break
    while R not in 'sn':
        R = input('Digite s ou n. Deseja continuar? ')

a = []
b = []
for p in range(len(box)):
    if box[p] % 2 == 0:
        a.append(box[p])
    else:
        b.append(box[p])

print(f'Lista dos numeros digitados! {box}')
print(f'Lista dos Pares! {a}')
print(f'Lisa dos Impares! {b}')
