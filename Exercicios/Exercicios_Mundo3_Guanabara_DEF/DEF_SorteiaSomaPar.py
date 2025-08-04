from random import randint

numeros = []

def sorteia(*s):
    for i in s:
        numeros.append(i)
    print(numeros)


def somaPar(*sp):
    soma = 0
    for c, v in enumerate(sp[0]):
        if v % 2 == 0:
            soma += v
    print(f'A soma dos pares é {soma}')


sorteia(randint(1, 10),
        randint(1, 10),
        randint(1, 10),
        randint(1, 10),
        randint(1, 10))
somaPar(numeros)
