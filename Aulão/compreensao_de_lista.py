numeros = [1, 4, 7, 9, 10, 12]

quadrados = [num ** 2 for num in numeros]
print(quadrados)

pares = [n for n in range(0, 11) if n % 2 == 0]
print(pares)

frase = 'A logica é apenas o principio da sabedoria, e não o seu fim.'
vogais = ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú']

lista_vogais = [v for v in frase if v in vogais]
print(f'A frase possui {len(lista_vogais)} vogais:')
print(lista_vogais)

# Distributiva entre valores de duas listas
distributiva = [k * m for k in [2, 3, 5] for m in [10, 20, 30]]
print(distributiva)
