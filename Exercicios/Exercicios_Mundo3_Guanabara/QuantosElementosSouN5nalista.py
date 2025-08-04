lista = []
n = 0
r = 's'
c = 0

while True:
    if r == 's':
        lista.append(int(input('Digite um numero: ')))
        c += 1
        r = input('Deseja continuar? [s/n]').strip().lower()
        while r not in 'sn':
            r = input('Digite apenas s ou n. Deseja continuar? ')
    else:
        break
lista.sort(reverse=True)
print(f'Voce digitou {c} numero(s).')
print(f'Os valores em ordem decrescente são: {lista}')
if lista.count(5) == True:
    print(f'O numero 5 FOI encntrado!')
else:
    print(f'O numero 5 NÃO foi encontrado!')
