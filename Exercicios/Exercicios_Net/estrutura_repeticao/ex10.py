#Faça um programa que receba dois números inteiros e gere os números inteiros que estão
# no intervalo compreendido por eles.

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

for c in range(num1, num2 + 1):
    print(c)
