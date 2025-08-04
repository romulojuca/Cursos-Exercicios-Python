#Altere o programa anterior para mostrar no final a soma dos números.
#PROGRAMA ANTERIOR: Faça um programa que receba dois números inteiros e gere os números inteiros que estão
# no intervalo compreendido por eles.

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
soma = 0

for c in range(num1, num2 + 1):
    soma += c
    print(c)

print(f"A soma dos numeros é {soma}")
