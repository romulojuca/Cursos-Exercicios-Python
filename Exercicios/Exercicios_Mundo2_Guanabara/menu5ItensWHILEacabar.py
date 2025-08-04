n1 = float(input('Digite o primeiro numero: '))
n2 = float (input('Digite o segundo numero: '))
n = 0
r = 0

while n != 5:
    print('Digite:\n[1] para somar.')
    print('[2] para multiplicar.')
    print('[3] ver o maior.')
    print('[4] digitar novos numeros.')
    print('[5] sair do porgrama.')
    n = int(input(' '))
    if n == 1:
        r = (n1+n2)
        print('A soma é {}'.format(r))
    
    if n == 2:
        r = (n1*n2)
        print('{} x {} = {}'.format(n1, n2, r))

    if n == 3 and n1 > n2:
        r = n1
        print('O maior é {}'.format(r))
        
    else:
        if n == 3 and n2 > n1:
            r = n2
            print('O Maior é {}'.format(r))

    if n == 4:
        n1 = float(input('Digite o primeiro numero novamente: '))
        n2 = float(input('Digite o segundo numero novamente: '))
print('FIM!')
