# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice"
# e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

def pergunta(frase: str):
    r = ''
    while r != 's' and r != 'n':
        r = str(input(f"{frase}"))
    return r



def classificado(lista):
    num = 0
    for c, v in enumerate(lista):
        if v == 's':
            num += 1

    if num == 0 or num == 1:
        return "Inocente"
    if num == 2:
        return "Suspeita"
    if num == 3 or num == 4:
        return "Cúmplice"
    if num == 5:
        return "Assassino"

lista = []
lista.append(pergunta("Telefonou para a vítima?"))
lista.append(pergunta("Esteve no local do crime?"))
lista.append(pergunta("Mora perto da vítima?"))
lista.append(pergunta("Devia para a vítima?"))
lista.append(pergunta("Já trabalhou com a vítima?"))
print(classificado(lista))
