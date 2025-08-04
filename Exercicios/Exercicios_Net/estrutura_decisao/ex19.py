# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

num = int(input("Digite um numero abaixo de 1000: "))
num = str(num)
if len(num) == 1:
    num = '00' + num
if len(num) == 2:
    num = '0' + num
num.split()
for c, v in enumerate(num):
    if c == 0:
        print(f"{v} centena(s), ", end='')
    if c == 1:
        print(f"{v} dezena(s) e ", end='')
    if c == 2:
        print(f"{v} unidade(s).")
