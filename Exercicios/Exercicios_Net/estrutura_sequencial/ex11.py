# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

n1i = int(input("Digite um numero inteiro: "))
n2i = int(input("Digite outro numero inteiro: "))
n1r = float(input("Digite um numero real: "))

print(f"o produto do dobro do primeiro com metade do segundo fica: {(n1i * 2) + (n2i / 2):.0f} ")
print(f"a soma do triplo do primeiro com o terceiro fica: {(n1i * 3) + n1r:.2f}")
print(f"o terceiro elevado ao cubo fica: {n1r ** 3}")