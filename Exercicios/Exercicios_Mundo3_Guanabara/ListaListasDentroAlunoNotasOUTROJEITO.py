ficha = []
while True:
    nome = str(input('Nome:'))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1+nota2)/2
    ficha.append([nome, [nota1, nota2], media])
    r = str(input('Deseja continuar? [s/n]')).lower()[0]
    if r in 'n':
        break

print('=-' * 13)
print(f'{"Nº.":<4}{"NOME":<10}{"Média":>8}')
print('=-' * 13)
for p, v in enumerate(ficha):
    print(f'{p:<4}{v[0]:<10}{v[2]:>8.1f}')

print('=-' * 13)
while True:
    opc = int(input('Mostrar nota de qual aluno? (999 interrompe)!'))
    if opc == 999:
        break
    for p, v in enumerate(ficha):
        if opc == p:
            print(f'{v[0]} tem as notas {v[1]}!')
