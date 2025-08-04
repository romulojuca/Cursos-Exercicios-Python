#Faça um programa que leia 5 números e informe o maior número.

lista = []

for c in range(0, 5):
    num = int(input("Digite um numero: "))
    lista.append(num)

lista.sort()
print(f"O maior numero é {lista[len(lista)-1]}")
