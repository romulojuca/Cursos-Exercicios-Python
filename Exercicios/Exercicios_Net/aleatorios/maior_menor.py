"""Faça um Programa que leia três números inteiros, em seguida mostre o maior e o menor deles.
"""
n1 = int(input('Digite o primeiro numero! '))
n2 = int(input('Digite o segundo numero! '))
n3 = int(input('Digite o terceiro numero! '))

maior = menor = n1

if n2 > n1:
    maior = n2
if n3 > maior:
    maior = n3
if n2 < n1:
    menor = n2
if n3 < menor:
    menor = n3

print(f"{maior} é o maior!")
print(f"{menor} é o menor!")
