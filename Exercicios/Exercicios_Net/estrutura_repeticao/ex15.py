#A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
# Faça um programa capaz de gerar a série até o décimo termo.

lista = []
lista2 = []
inicial = 1


for c in range(0, 8):
    if c == 0:
        lista.append(1)
    lista.append(lista[c] + lista[c-1])

print(f"Sequencia -> {inicial} -> ", end='')

for c in lista:
    print(f"{c} -> ",end='')

print("FIM!")
