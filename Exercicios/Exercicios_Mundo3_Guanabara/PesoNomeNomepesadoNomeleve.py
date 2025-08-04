pessoas = list()
lista = list()

r = 's'
maior = menor = 0
while r == 's':
    pessoas.append(str(input('Nome: ')))
    pessoas.append(int(input('Peso: ')))
    if len(lista) == 0:
        maior = menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas[1]
    
    lista.append(pessoas[:])
    pessoas.clear()
    
    r = input('Deseja continuar? [s/n]')
print(lista)
print(f'Ao todo foram cadastradas {len(lista)} pessoas!')
print(f'O maior peso foi de {maior}Kg. Pessoas mais pesadas: ',  end='')
for p in lista:
    if p[1] == maior:
        print(f'{p[0]} ', end='')
print()
print(f'O menor peso foi de {menor}Kg. pessoas leves: ', end='')
for p in lista:
    if p[1] == menor:
        print(f'{p[0]}')
