expr = str(input('digite a expressao: '))
lista = []

contPE = 0
contPD = 0

for c in expr:
    if c == '(':
        lista.append('(')
        contPE += 1
    elif c == ')':
        contPD +=1
        lista.append(')')
        if contPD > contPE:
            print('Incorreto!!')
            break

E = lista.count('(')
D = lista.count(')')
if E == D:
    print('Correto!')
