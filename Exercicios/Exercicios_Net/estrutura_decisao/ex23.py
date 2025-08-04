# Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.
from math import trunc

num = float(input("Digite um numero: "))
#trunc elimina todos os numeros decimais!
num_copy = trunc(num)
if num % num_copy == 0:
    print(f"{num} é um numero inteiro!")
if num % num_copy != 0:
    print(f"{num} é um numero decimal!")
