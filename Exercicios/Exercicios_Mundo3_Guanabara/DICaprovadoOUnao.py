dic = {}
lista = []

dic['nome'] = str(input('Nome: '))
dic['media'] = float(input('Média: '))
lista.append(dic.copy())

print(lista[0])

print(f'Nome é igual a {lista[0]["nome"]}')
print(f'Média é igual a {lista[0]["media"]}')
if dic['media'] >= 7:
    print('Situação é igual a Aprovado!')
else:
    print('REPROVADO!')
