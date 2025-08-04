# Set
# Usar {} e somente colocar os valores vira um conjunto
planeta_anao = {'Plutão', 'Ceres', 'Eris', 'Haumea', 'Makemake'}
print(len(planeta_anao))
print('Lua' in planeta_anao)

for i in planeta_anao:
    print(i.upper(), end='-')
print()
# Lista comum
astros = ['Lua', 'Vênus', 'Sirus', 'Marte', 'Lua']
print(astros)

# set (conjunto)... quando usa o set transforma a lista em conjunto, e ele deleta todos nomes iguais duplicados
astros_set = set(astros)
print(astros_set)

# Comparações de conjunto
astros1 = {'Lua', 'Vênus', 'Sirus', 'Marte', 'Io'}
astros2 = {'Lua', 'Vênus', 'Sirus', 'Marte', 'Cometa de Halley'}
print(astros1 != astros2)
print(astros1 | astros2)  # juntar os 2 conjuntos
# Intersecção, tras os elementos que estão nos 2 conjuntos
print(astros1 & astros2)
print(astros1.intersection(astros2))  # mesma coisa de cima

# para verificar os elementos que nao aparecem nos 2 conjuntos usamos o ^ ou .symmetric_difference
print(astros1 ^ astros2)
print(astros1.symmetric_difference(astros2))

# add ou remover itens no conjunto
astros1.add('Urano')
astros1.remove('Io')
# Discard nao da erro se o elemento nao estiver no conjunto
astros1.discard('afafaf')
astros1.pop()  # remove 1 item do conjunto aleatoriamente
astros1.clear()  # limpa tudo
print(astros1)
