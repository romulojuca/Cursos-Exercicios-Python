def area(a, b):
    m2 = a * b
    print(f'A área do terreno é {m2.__ceil__()}m²')


a = float(input('Digite a largura do terreno: '))
b = float(input('Digite o comprimento do terreno: '))

area(a, b)
