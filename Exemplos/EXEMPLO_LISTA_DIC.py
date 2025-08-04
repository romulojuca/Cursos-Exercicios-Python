dados = {}
cadasto = []
gols = []
cont_gols = status = 0
resp = 'S'
while True:
    while resp not in 'SN':
        resp = str(input(f'Deseja continuar? S/N: ')).strip().upper()
    if resp == 'N':
        break
    dados['nome'] = str(input('Nome: '))
    dados['partidas'] = int(input('Qnts Patidas: '))
    for e in range(dados['partidas']):
        gols.append(int(input(f'Quantos gols na partida {e+1}: ')))
    dados['gols'] = gols[:]
    gols.clear()
    for c in dados['gols']:
        cont_gols += c
    dados['total_gols'] = cont_gols
    cont_gols = 0
    cadasto.append(dados.copy())
    resp = ' '
print('-='*30)
print("cod ", end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('-='*30)
for i, e in enumerate(cadasto):
    print(f'{i:<3} ', end='')
    for d in e.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    status = int(input(f'Dados de qual jogador? '))
    if status == 999:
        break
    print(print(f'LEVANTAMENTO DO JOGADOR {cadasto[status]["nome"]}:'))
    for i, e in enumerate(cadasto):
        if i == status:
            for n in range(0, e['partidas']):
                print(f'Na partida {n+1}ª partida fez ', end=' ')
                for c, v in e.items():
                    if c == 'gols':
                        print(v[n])
