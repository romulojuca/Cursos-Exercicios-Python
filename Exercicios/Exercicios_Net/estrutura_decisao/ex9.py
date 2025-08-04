"""Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""

lista = []
for c in range(0, 3):
    lista.append(float(input("Digite um numero: ")))
lista.sort(reverse=True)
print(f"Os numeros em ordem decrescente ficam {lista}")
