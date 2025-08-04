#Faça um Programa que leia um número e exiba o dia correspondente da semana.
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

dia = int(input("Digite um numero correspondente com os dias da semana: "))
dic = {0: 'Domingo', 1: 'Segunda', 2: 'Terça', 3: 'Quarta', 4: 'Quinta', 5: 'Sexta', 6: 'Sábado'}
for c, v in dic.items():
    if dia - 1 == c:
        print(v)
if dia not in {1, 2, 3, 4, 5, 6, 7}:
    print("Valor Inválido!")
