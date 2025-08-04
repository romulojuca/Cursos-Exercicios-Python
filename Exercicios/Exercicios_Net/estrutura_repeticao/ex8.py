#Faça um programa que leia 5 números e informe a soma e a média dos números.

lista = []
soma = 0
media = 0

for c in range(0, 5):
    num = int(input("Digite um numero! "))
    lista.append(num)

for c, v in enumerate(lista):
    soma += v

media = soma / 5
print(f"A soma é {soma} e a média é {media}")
