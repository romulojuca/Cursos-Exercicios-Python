n1 = [5, 7, 8, 9, 11, 15]
n2 = [1, 2, 3, 7, 10, 19]
numeros = n1 + n2

numeros[0] = 9
print(len(numeros))
print(sorted(numeros, reverse=True))  # Deixar os valores em ordem
print(sum(numeros))
print(min(numeros))
print(max(numeros))
numeros.append(20)
numeros.pop()  # remove o ultimo
numeros.pop(3)  # remove o elemento na posicao 3
print(numeros)
numeros.insert(3, 70)  # insert na posicao 3 o valor 70
print(numeros)
print(17 in numeros)  # se tem o numero 17 na lista T ou F

planetas = ['Mercúrio', 'Vênus', 'Marte', 'Saturno', 'Urano', 'Netuno']
for i in planetas:
    print(i)
bebidas = []
for i in range(1, 6):
    bebida = str(input('Digite o nome da bebida! '))
    bebidas.append(bebida)

bebidas.sort()
print(bebidas)
