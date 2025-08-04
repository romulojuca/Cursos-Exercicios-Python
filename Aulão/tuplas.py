halogenios = ('F', 'C1', 'Br', 'I', 'At')
gases_nobres = ('He', 'Ne', 'Ar', 'Xe', 'Kr', 'Rn')
elementos = halogenios + gases_nobres
print(elementos)
print('Cl' in halogenios)
t1 = (5, 6, 7, 8, 2, 2, 6, 6, 78, 34, 37, 387, 3, 25, 4)
print(min(t1))
print(max(t1))
print(t1.count(3))

# Operações nao disponiveis em tuplas: .sort .append . reverse .pop...

for i in elementos:
    print(i)

# transformando a tupla em lista
grupo17 = list(halogenios)
print(grupo17)
grupo10 = tuple(grupo17)
# nao pode usar o sorted na original mas pode jogar a copia ordenada em outra variavel
grupo20 = sorted(grupo10)
print(grupo20)
