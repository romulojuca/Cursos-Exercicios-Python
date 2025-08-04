produtos = ('Banana', 2000.00, 
            'Mamão', 34.00, 'Melancia', 120.50, 'Maracuja', 4.55, 
            'Pera', 7)

for c in range(0, len(produtos)):
    if c % 2 == 0:
        print(f'{produtos[c]:.<30}', end='')
    else:
        print(f'R${produtos[c]:>8.2f}')
