times = ('time a', 'time b', 'time c', 'time d', 'time e', 'Chapecoense', 'time g', 'time h', 'time i', 'time j', 'time k', 'time l', 'time m', 'time n', 'time o', 'time p', 'time q', 'time r', 'time s', 'time t')

print(f'Os 5 primeiros times são: {times[0:5]}')
print(f'Os lanternas são: {times[len(times):len(times)-5:-1]}')
print(f'Os times da tabela em Ordem alfabética são: {sorted(times)}')
print(f'A Chapecoense está na posição {times.index("Chapecoense")+1} na tabela!')
