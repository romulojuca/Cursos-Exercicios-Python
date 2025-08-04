from time import sleep
lista = []

for c in range(0, 5):
    n = int(input(f'Digite o {c+1}º valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print(f'Adicionado no final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos}')
                break
            pos += 1


print(lista)
print('FIM!!')
