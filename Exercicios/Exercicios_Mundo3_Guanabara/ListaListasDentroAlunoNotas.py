lista = []
listatest = []
n1 = 0
n2 = 0
notas = 0
while True:
    listatest.append(str(input('Digite o nome do aluno: ').strip().upper()))
    listatest.append(float(input('Digite a primeira nota: ').strip()))
    listatest.append(float(input('Digite a segunda nota: ').strip()))
    lista.append(listatest[:])
    listatest.clear()
    r = input('Deseja continuar? [s/n]')
    if r == 'n':
        break

for p, v in enumerate(lista):
    n1 = v[1]
    n2 = v[2]
    print(f'{p+1}º - {v[0]: ^20} ', end='')
    print(f'média {(n1+n2)/2}!')

while True:
    notas = int(input('Deseja mostrar as notas de qual aluno? '))
    if notas == 999:
        break
    for p, v in enumerate(lista):
        if notas == p+1:
            print(f'As nota de {v[0]} são:', end='')
            print(f'{v[1]}, {v[2]}')
