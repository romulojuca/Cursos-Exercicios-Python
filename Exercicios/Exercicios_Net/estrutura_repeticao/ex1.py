#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = int(input("Digite uma nota entre 0 e 10: "))

while True:
    if nota < 0 or nota > 10:
        nota = int(input("Digite uma nota entre 0 e 10: "))
    elif nota >= 0 and nota <= 10:
        print(nota)
        break