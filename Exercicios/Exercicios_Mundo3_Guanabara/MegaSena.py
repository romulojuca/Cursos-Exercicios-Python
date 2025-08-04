from time import sleep
from random import randint
num = 0
cont = 0
lista = []
fake = []
jogos = int(input('Quantos jogos serão gerados? '))

while True:
    for c in range(1, 7):
        num = randint(1, 60)
        while num in fake:
            num = randint(1, 60)
        fake.append(num)
        
    lista.append(fake[:])
    fake.clear()
    cont += 1
    if cont == jogos:
        break

for c, p in enumerate(lista):
    p.sort()
    print(f'O jogo {c+1} tem os resultados: {p}')
    sleep(1)
