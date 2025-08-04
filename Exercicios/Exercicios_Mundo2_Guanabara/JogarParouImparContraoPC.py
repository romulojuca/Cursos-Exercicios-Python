from random import randint

print('=--'*30)
print('VAMOS JOGAR PAR OU IMPAR!!!!')
print('=--'*30)
num = int(input('Escolha um numero: '))
ppi = str(input('Você quer Par ou Impar? [P/I]')).strip().upper()[0]
pcpi = ''
pc = ''
numpc = randint(1, 10)
t = num + numpc
c = 0


while True:
    if ppi == 'P':
        pcpi = 'I'
    if ppi == 'I':
        pcpi = 'P'
    if t % 2 == 0 and ppi == 'P' or t % 2 != 0 and ppi == 'I':
        c += 1
        print(f'O PC escolheu {numpc} e você {num}, Você venceu!!')
        num = int(input('Vamos denovo, digite um numero! '))
        ppi = str(input('Par ou Impar? [P/I]')).strip().upper()[0]
        numpc = randint(1, 10)
        t = num + numpc
    else:
        print(f'Você escolheu {num} e o PC {numpc}, Você perdeu!!')
        print(f'Você teve {c} vitoria(s)')
        print('FIM!!!')
        break
