# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#par ou ímpar;
#positivo ou negativo;
#inteiro ou decimal.
from math import trunc
from decimal import Decimal

resp = float(0)
num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
operador = str(input("Qual operação você deseja usar? + - * ou /: "))

if operador in '+':
    resp = num1 + num2
if operador in '-':
    resp = num1 - num2
if operador in '*':
    resp = num1 * num2
if operador in '/':
    resp = num1 / num2
#trunc elimina tudo depois da virgula(vira inteiro)
resp_copy = trunc(resp) + 2
resp += 2

if resp % 2 == 0:
    print(f"{resp - 2} é PAR, ", end='')
if resp % 2 != 0:
    print(f"{resp - 2} é IMPAR, ", end='')
if resp >= 0:
    print("POSITIVO, ", end='')
if resp < 0:
    print("NEGATIVO, ", end='')
if resp % resp_copy == 0:
    print("e INTEIRO!")
if resp % resp_copy != 0:
    print("e DECIMAL!")
