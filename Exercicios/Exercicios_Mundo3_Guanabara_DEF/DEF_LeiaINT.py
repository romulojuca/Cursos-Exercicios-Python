def leiaInt(num):
    while True:
        n = str(input(num))
        if n.isnumeric():
            n = int(n)
            break
        else:
            print('Apenas numeros inteiros!')
    return n



n = leiaInt('Digite um numero: ')
print(f'{n}')
