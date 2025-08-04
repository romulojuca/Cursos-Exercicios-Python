#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números 
# pares e a quantidade de números impares.

lista = []
par = 0
impar = 0

for c in range(0, 10):
    num = int(input("Digite um numero: "))
    lista.append(num)

for c, v in enumerate(lista):
    if v % 2 == 0:
        par += 1
    if v % 2 != 0:
        impar += 1

print(f"Existem {par} numeros Pares e {impar} numers Ímpares!")
