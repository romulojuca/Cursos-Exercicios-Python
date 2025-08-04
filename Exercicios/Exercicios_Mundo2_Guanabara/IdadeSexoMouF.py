print('=*='*20)
frase1 = 'CADASTRO DE PESSOAS'
print (f'O {frase1} tem...')
print('=*='*20)

idade = int(input('Idade: '))
sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
            sexo = str(input('Sexo [M/F]:')).strip().upper()[0]
cm = 0
m = 0
maior = 0
i = ''

while True:
    if idade > 18:
        maior += 1
    if sexo == 'M':
        cm += 1
    if sexo == 'F' and idade < 20:
        m += 1
    i = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while i not in 'SN':
        i = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

    if i == 'N':
        break
    else:
        idade = int(input('Idade: '))
        sexo = str(input('Sexo [M/F]:')).strip().upper()[0]
        while sexo not in 'MF':
            sexo = str(input('Sexo [M/F]:')).strip().upper()[0]

print(f'{maior} Pessoas tem mais de 18 anos!')
print(f'{cm} Homens foram cadastrados!')
print(f'{m} Mulheres tem menos de 20 anos!')
