# Dicionarios

elemento = {
    'Z': 3,
    'nome': 'Lítio',
    'grupo': 'Metáis Alcalinos',
    'densidade': 0.534
}
print(f'Elemento: {elemento['nome']}')
print(len(elemento))

# adicionar uma chave
elemento['periodo'] = 1
print(elemento)

# Exclusão passando a chave, deleta a chave apénas, se usar del elemento, deleta o dicionario permanentemente
del elemento['periodo']
print(elemento)

# Apagar todo o dicionario
# elemento.clear()
print(elemento)

print(elemento.items())
for i, e in elemento.items():
    print(f"{i}: {e}")
print()
for i in elemento.keys():
    print(i)
print()
for i in elemento.values():
    print(i)
