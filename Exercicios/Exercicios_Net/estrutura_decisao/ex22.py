#Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
# Dica: utilize o operador módulo (resto da divisão).

num = int(input("Digite um numero: "))
if num % 2 == 0:
    print(f"O numero {num} é PAR!")
if num % 2 != 0:
    print(f"O numero é IMPAR!")
