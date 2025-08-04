dic = {}
lista = []
media = 0

while True:
    dic['nome'] = str(input('Nome: '))
    dic['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
    dic['idade'] = int(input('Idade: '))
    lista.append(dic.copy())
    media = (media + dic['idade'])
    r = str(input('Deseja continuar? [s/n]: ')).lower().strip()[0]
    if r in 'n':
        break

print(f'- O grupo tem {len(lista)} pessoas.')
media = media/len(lista)
print(f'- A média de idade é de {media} anos.')
print(lista)
print(f'- As mulheres cadastradas foram: ',end='')
for p, v in enumerate(lista):
    if v['sexo'] in 'Ff':
        print(f'{v["nome"]} ', end='')
print()
print(f'- Lista das pessoas que estão acima da média: ')

for p, v in enumerate(lista):
    if v['idade'] > media:
        print(v)
