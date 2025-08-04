# Faça um Programa que peça dois números e imprima o maior deles.
n1 = float(input("Digite o primeiro numero! "))
n2 = float(input("Digite o segundo numero! "))
maior = n1
if n2 > n1:
    maior = n2
print(f"O maior numero é {maior}")
