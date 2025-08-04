"""Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores
podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero,
isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
"""
ladoA = int(input("Digite o primeiro lado: "))
ladoB = int(input("Digite o segundo lado: "))
ladoC = int(input("Digite o terceiro lado: "))
ladoAB = ladoA + ladoB
ladoBC = ladoB + ladoC
ladoAC = ladoA + ladoC
if ladoAB > ladoC and ladoBC > ladoA and ladoAC > ladoB:
    print("Isso pode virar um ", end='')
    if ladoA == ladoB == ladoC:
        print("Triângulo Equilátero.")
    elif ladoAB == ladoAC or ladoAB == ladoBC or ladoBC == ladoAC:
        print("Triângulo Isósceles.")
    else:
        print("Triângulo Escaleno.")
else:
    print("Isso não pode virar um triangulo!")
