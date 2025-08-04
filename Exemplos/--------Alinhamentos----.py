palavra = ('José', 65)
ficha = 0

# Alinha do começo e poe . até chegar em 30 espaços pra direita!
print(f'{palavra[0]:.<30}', end='')
# Alinha 8 espaços > e poe 2 casas flutuantes!
print(f'R${palavra[1]:>8.2f}R$')
print('\n')
print(f'{"CURSO EM VIDEO":^40}')  # CENTRALIZADO
print('=-'*40)


print(f'{"Nº.":<4}{"NOME":<10}{"Média":>8}')
print('=-' * 13)
'''for p, v in enumerate(ficha):
    print(f'{p:<4}{v[0]:<10}{v[2]:>8.1f}')'''

print('Joao'.center(30))
print(f'\t {10}')
print(f'\t {89089898}')
