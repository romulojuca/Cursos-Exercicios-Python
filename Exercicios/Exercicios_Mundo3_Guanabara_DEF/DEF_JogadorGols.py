def ficha(nome='DESCONHECIDO', gols=0):
    print(f'O jogador {nome} fez {gols} gols no campeonato!')


n = str(input('Nome: '))
g = str(input('Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(gols=g, nome=n)
