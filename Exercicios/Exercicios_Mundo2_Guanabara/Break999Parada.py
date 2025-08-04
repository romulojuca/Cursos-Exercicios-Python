num = int(input('Digite um numero: '))
c = 0
t = 0

while num != 999:
    
    c += 1
    t = t + num
    num = int(input(('Outro numero: ')))
    if num == 999:
        break

print(f'Você digitou {c} numeros e soma deles foi {t}!! ')
