"""Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
"""
class Canditados:
    def __init__(self, nome, votos):
        self.nome = nome
        self.votos = votos


eleitores = int(input("Digite o total de eleitores: "))
contador = 0
v1 = v2 = v3 = r = 0
print("1- Marcos do Gás, 2- Vanessa da Venda, 3- Joaquim do Pastel")
while contador != eleitores:
    r = int(input("Em quem voce vai votar? 1- Marcos do Gás, 2- Vanessa da Venda, 3- Joaquim do Pastel: "))
    if r != 1 and r != 2 and r != 3:
        while True:
            r = int(input("Apénas: 1- Marcos do Gás, 2- Vanessa da Venda, 3- Joaquim do Pastel "))
            if r == 1 or r == 2 or r == 3:
                break
    if r == 1:
        v1 += 1
    if r == 2:
        v2 += 1
    if r == 3:
        v3 += 1
    contador += 1

maior = v1
if v2 > v1:
    maior = v2
if v3 > maior:
    maior = v3

cc1 = Canditados("Marcos do Gás", v1)
cc2 = Canditados("Vanessa da Venda", v2)
cc3 = Canditados("Joaquim do Pastel", v3)

print(f"Candidato 1- Marcos do Gás teve {v1} votos!")
print(f"Candidato 2- Vanessa da Venda teve {v2} votos!")
print(f"Candidato 3- Joaquim do Pastel teve {v3} votos!")

print("O vencedor das eleições foi ", end="")
if maior == v1:
    print(f"{cc1.nome} com {v1} votos!")
if maior == v2:
    print(f"{cc2.nome} com {v2} votos!")
if maior == v3:
    print(f"{cc3.nome} com {v3} votos!")
