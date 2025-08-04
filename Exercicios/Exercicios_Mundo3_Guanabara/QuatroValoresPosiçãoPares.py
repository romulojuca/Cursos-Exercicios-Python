n = (int(input('Digite um numero: ')), int(input('Digite outro numero: ')), int(input('Outro numero: ')), int(input('Outro: ')))
print(n)

n9 = n.count(9)
if n9 >= 1:
    print(f'O numero nove apareceu {n9} vezes!')
else:
    print('O numero nove não apareceu nenhuma vez!')
