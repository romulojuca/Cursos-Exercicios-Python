# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas
# de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo
# de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

saque = int(input("Digite o valor do saque: "))
cont_100 = cont_50 = cont_10 = cont_5 = cont_1 = 0

if saque >= 100:
    cont_100 = saque // 100
    saque = saque % 100
if saque >= 50:
    cont_50 = saque // 50
    saque = saque % 50
if saque >= 10:
    cont_10 = saque // 10
    saque = saque % 10
if saque >= 5:
    cont_5 = saque // 5
    saque = saque % 5
if saque >= 1:
    cont_1 = saque // 1

print("Você irá receber:")
print(f"{cont_100} nota(s) de R$100, ", end='')
print(f"{cont_50} nota(s) de R$50, ", end='')
print(f"{cont_10} nota(s) de R$10, ", end='')
print(f"{cont_5} nota(s) de R$5, ", end='')
print(f"{cont_1} nota(s) de R$1")
