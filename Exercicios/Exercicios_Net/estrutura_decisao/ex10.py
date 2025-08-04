"""Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou
V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
"""
turno = str(input("Digite o turno que você estuda! M- Matutino, V- Vespertino ou N- Noturno ")).upper().strip()
if turno == "M":
    print("Você estuda no turno Matutino")
elif turno == "V":
    print("Você estuda no turno Vespertino")
elif turno == "N":
    print("Você estuda no turno Noturno")
else:
    print("Valor Invalido")
