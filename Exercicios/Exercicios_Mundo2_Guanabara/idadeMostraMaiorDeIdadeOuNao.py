from datetime import date

data = date.today().year
d = 0

for c in range(1, 8):
    ano = int (input ('Digite seu ano de nascimento: '))
    ano1 = ano + 18
    if ano1 <= data:
        d = (d + 1)
print('Dessas 7 pessoas {} Já atingiram 18 anos e {} não atingiram!'.format(d, 7-d))
