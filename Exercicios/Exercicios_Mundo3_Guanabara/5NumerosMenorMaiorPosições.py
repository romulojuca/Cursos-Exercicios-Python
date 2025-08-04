num = []
maior = 0
menor = 0

for cont in range(0, 5):
    num.append(int(input(f'Digite o valor para a posição {cont}:')))
    if cont == 0:
        maior = menor = num[cont]
    else:
        if num[cont] > maior:
            maior = num[cont]
        if num[cont] < menor:
            menor = num[cont]
    



print(f'Voce digitou os valores -> {num}')
print(f'Menor nº: {menor} nas posições ',end='')
for p, n in enumerate(num):
    if n == menor:
        print(f'{p}...',end='')
print()

print(f'Maiorº: {maior} nas posições ', end='')
for p, n in enumerate(num):
    if n == maior:
        print(f'{p}...', end='')
print()
