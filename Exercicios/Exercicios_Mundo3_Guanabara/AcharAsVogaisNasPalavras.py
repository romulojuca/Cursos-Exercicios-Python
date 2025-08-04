from time import sleep

conjunto = ('Feijao', 'Morcego', 'Carne', 'Jabuticaba', 'Vaca')
pf = ''
cont = 0

for p in conjunto:
    print(f'\nNa palavra {p.upper()} as vogais são:', end='')
    sleep(1)
    for posicao in p:
        if posicao in 'aeiou':
            print(posicao, end=' ')

print('\nFIM')
