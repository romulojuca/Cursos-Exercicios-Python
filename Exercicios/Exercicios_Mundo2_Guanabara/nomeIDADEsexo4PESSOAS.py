media = 0
m20 = 0
hv = 0
h = ''
for c in range(1, 5):
    nome = str(input('Pessoa {}, digite seu nome: '.format(c))).strip().lower()
    idade = int(input('Pessoa {}, digite sua idade: '.format(c)))
    sexo = str(input('Pessoa {}, digite seu sexo: '.format(c))).strip().lower()
    media = media + (idade/4)
    if sexo == 'm' and idade > 20:
        m20 = m20 + 1
    if sexo == 'h' and idade > hv:
        hv = idade
        h = nome
print('*='*20)
print('A média de idade das 4 pessoas é {}'.format(media))
print('O Homem mais velho é o {} com {} anos.'.format((h).upper(), hv))
print('{} Mulhere(s) tem mais de 20 anos!'.format(m20))
print('=*'*20)
