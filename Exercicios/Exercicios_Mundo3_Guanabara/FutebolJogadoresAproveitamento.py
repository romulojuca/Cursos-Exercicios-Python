dic = {}
jogadores = []
gols = []
r = 's'
while True:
    total = 0
    dic.clear()
    gols.clear()
    dic['nome'] = str(input('Nome do jogador: '))
    jogos = int(input('Quantas partidas ele jogou? '))
            
    for c in range(0, jogos):
        gols.append(int(input(f'Quantos gols na {c+1}ª partida? ')))
    dic['gols'] = gols[:]
    
    for c, v in enumerate(gols):
        total += v
    dic['total'] = total/jogos
    
    jogadores.append(dic.copy())

    r = str(input('Deseja continuar? [s/n] ')).strip().lower()[0]
    while r not in 'sn':
        r = str(input('ERRO!! Responda [s/n]')).strip().lower()[0]
        if r in 'n':
            break
    if r == 'n':
        break

print('Cod. ', end='')
for k in dic.keys():
    print(f'{k:<15}', end='')
print()
for k, v in enumerate(jogadores):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f' {str(d):<15}', end='')
    print()


while True:
    dados = int(input('Mostrar dados de qual jogador? (999 PARA): '))
    if dados == 999:
        break
    if dados >= len(jogadores):
        print(f'Cod. errado! Não existe cod. {dados}!')
    else:
        print(f'JOGOS E GOLS DO JOGADOR {jogadores[dados]["nome"]}')
        for p, v in enumerate(jogadores[dados]["gols"]):
            print(f'No jogo {p+1} ele marcou {v} gols.')
