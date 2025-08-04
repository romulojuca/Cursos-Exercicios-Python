from random import randint
from time import sleep

lista = randint(1, 5)
c = 1

print ('=*'*20)
print ('TENTE ADIVINHAR O NUMERO DE 1 a 10 QUE PENSEI...')
print ('*='*20)
sleep(2)

n = int(input('1ª tentativa! '))
print('Checando...')
sleep(2)

while n != lista:
    c = c + 1
    n = int(input('Você errou tente denovo... '))
    print('Checando...')
    sleep(2)
    
print('PARABÉNS!!! Era o numero {}!! Você acertou na {}ª tentativa!!'.format(lista, c))
