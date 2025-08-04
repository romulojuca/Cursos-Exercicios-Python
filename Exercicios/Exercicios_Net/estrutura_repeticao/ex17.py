#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

num = int(input("Digite um numero para ver seu fatorial! "))
total = 1

print(f"{num}!=",end='')
for c in range(num, 0, -1):
    print(f"{c}x", end='')
    total *= c

print(f"={total}")
