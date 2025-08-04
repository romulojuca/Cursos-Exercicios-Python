# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

def earlyReturn(data: str) -> str:
    lista = []
    lista1 = []
    for c, v in enumerate(data):
        if c in {0, 1, 3, 4 ,6 ,7 , 8, 9}:
            v = int(v)
        lista1.append(v)
        lista = lista1.copy()
    if lista[0] > 3:
        return "DATA INVALIDA!"
    if lista[2] != '/' or lista[5] != '/':
        return "DATA INVALIDA!"
    if lista[0] == 3 and lista[1] > 0:
        return "DATA INVALIDA!"
    if lista[3] > 1:
        return "DATA INVALIDA!"
    if lista[3] == 1 and lista[4] > 2:
        return "DATA INVALIDA!"
    return f"{data} é válida!"


data = {}
data = str(input("Insira uma data no formato dd/mm/aaaa "))

print(earlyReturn(data))
