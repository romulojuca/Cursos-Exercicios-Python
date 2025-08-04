"""Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato.
"""

produto1 = float(input("Digite o valor do primeiro produto! "))
produto2 = float(input("Digite o valor do segundo produto! "))
produto3 = float(input("Digite o valor do terceiro produto! "))
menor_preco = produto1
if produto2 < menor_preco:
    menor_preco = produto2
if produto3 < produto2 and produto3 < produto1:
    menor_preco = produto3
print(f"Você deve comprar o produto que custa R${menor_preco}.")
