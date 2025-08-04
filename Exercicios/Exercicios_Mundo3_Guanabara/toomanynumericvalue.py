lista = []
r = 's'

while r == 's':
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Numero adicionado...')
    else:
        print('Numero duplicado! Não vou adicionar...')
    
    r = str(input('Deseja continuar? [s/n]')).strip().lower()
    while r not in 'sn':
        r = str(input('Digite [s] ou [n], deseja digitar outro valor?'))

            
lista.sort()
print(f'Numeros adicionados em ordem numerica = {lista}')
