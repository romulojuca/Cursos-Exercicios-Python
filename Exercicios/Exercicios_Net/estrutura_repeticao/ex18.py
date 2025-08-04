#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

lista = []
r = 's'
total = 0

while r == 's':
    num = int(input("Digite um numero! "))
    lista.append(num)
    r = str(input("Deseja digitar outro numero? [s/n]")).lower().strip()
    while r not in 'sn':
        r = str(input("Deseja digitar outro numero? [s/n]")).lower().strip()

maior = lista[0]
menor = lista[0]

for c in lista:
    if c > maior:
        maior = c
    if c < menor:
        menor = c
    total += c

print(f"O maior é {maior}")
print(f"O menor é {menor}")
print(f"A soma entre eles é {total}")
