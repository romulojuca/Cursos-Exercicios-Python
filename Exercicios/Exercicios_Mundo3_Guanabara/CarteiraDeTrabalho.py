from datetime import date

ano = date.today().year

lista = {}
lista['nome'] = str(input('Nome: '))
lista['idade'] = ano - int(input('Ano de Nascimento: '))
lista['ctps'] = int(input('Carteira de Trabalho: (0 não tem)'))

if lista['ctps'] != 0:
    lista['ano_contratacao'] = int(input('Ano de contratação: '))
    lista['salario'] = float(input('Salário: '))
    lista['aposentadoria'] = (35 + (lista['ano_contratacao'] - (ano - lista['idade'])))
for k, v in lista.items():
    print(f'{k} tem o valor {v}')
