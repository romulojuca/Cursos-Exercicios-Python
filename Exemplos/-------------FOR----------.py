import math

# PARA cada VALOR em VALORES:
valores = [0, 9, 4]
for valor in valores:
    print(f'{valor}...')

# PARA cada POSICAO, INDICE em VALORES
for posicao, valor in enumerate(valores):
    print(f'Na posição {posicao} encontrei o valor {valor}')
print('Cheguei ao final da lista')

numeros = []
for cont in range(0, 2):
    numeros.append(int(input('Digite um valor: ')))
print(numeros)

a = [2, 3, 4, 7]
b = a[:]  # CRIA uma COPIA da lista a na variavel b
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

cadastro = {'nome': ['Pedro', 'Maria', 'Joana'], 'sexo': [
    'M', 'F', 'F'], 'ano': [2000, 1991, 2020], 'idade': [20, 30, 40]}

# Roda um dicionario nos itens selecionados
for nome, sexo, idade in zip(cadastro['nome'], cadastro['sexo'], cadastro['idade']):
    if sexo == 'F' and idade <= 30:
        print(nome)

# copia de um dicionario indo para lista
testDicionario = {'nome': 'José'}
testLista = []
testLista.append(testDicionario.copy())
print(testLista)
