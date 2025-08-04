lista = {}
lista_gols = []
partidas = 0
total = 0

lista['nome'] = str(input('Nome do Jogador: '))

partidas = int(input(f'Quantas partidas {lista["nome"]} jogou? '))

for p in range(0, partidas):
    lista_gols.append(int(input(f'Quantos gols na partida {p+1}? ')))

lista['gols'] = lista_gols.copy()
for p, v in enumerate(lista_gols):
    total += v
print('=-' * 30)
lista['total'] = total
for k, v in lista.items():
    print(f'O campo {k} tem o valor {v}.')
print('=-' * 30)
print(f'O jogador {lista["nome"]} jogou {partidas} partidas.')
for p, v in enumerate(lista_gols):
    print(f'Na partida {p+1}, fez {v} gols.')
print(f'Foi um total de {lista["total"]}')
