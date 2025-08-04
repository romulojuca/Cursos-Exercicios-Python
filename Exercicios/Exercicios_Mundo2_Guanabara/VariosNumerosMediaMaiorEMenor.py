n = int(input('Digite um numero: '))
c = 0
resposta = 's'
m = 0
men = 999999999999999999999999999999999999999999999999999
t = 0


while resposta not in 'nNao':
    c += 1
    if n > m:
        m = n
    if n < men:
        men = n
    t = t + n
    resposta = str(input('Deseja continuar? [Sim/Nao]')).strip().lower() [0]
    if resposta == 's':
        n = int(input('Digite outro numero: '))

print('A média entre os numeros é {:.2f}'.format(t/c))
print('O maior numero digitado foi {}'.format(m))
print('O menor numero digitado foi {}'.format(men))
