"""Faça um Programa que leia três números e mostre o maior deles.
"""

n1 = float(input("Digite um numero: "))
n2 = float(input("Digite outro numero: "))
n3 = float(input("Digite mais um numero: "))
maior = n1
if n2 > n1:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3
print(f"O maior numero é {maior}")
