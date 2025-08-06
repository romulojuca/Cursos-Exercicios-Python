nome = input('Nome: ')
idade = int(input('Idade: '))
salario = float(input('Salário: '))
sexo = input('Sexo: ').lower().strip()
estado_civil = input('Estado Civil: ').lower().strip()

if len(nome) > 3:
    print('Nome Ok!')
else:
    print('Nome Inválido!')
if idade >= 0 and idade <= 150:
    print('Idade ok!')
else:
    print('Idade inválida!')
if salario > 0:
    print('Salário ok!')
else:
    print('Salário Inválido!')
if sexo in 'fm':
    print('Sexo ok!')
else:
    print('Sexo Inválido!')
if estado_civil in 'scvd' and len(estado_civil) == 1:
    print('Estado Civil ok!')
else:
    print('Estado Civil inválido!')
