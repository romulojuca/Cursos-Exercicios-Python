#print(f'{"Cod":<6}{"Nome":<15}{"Gols":<7}{"Total":<5}')
lista = []
exp = str(input('Digite uma expressão: '))

for c in exp:
    if c == '(':
        lista.append('(')
    elif c == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão está VALIDA!')
else:
    print('INVALIDA')
