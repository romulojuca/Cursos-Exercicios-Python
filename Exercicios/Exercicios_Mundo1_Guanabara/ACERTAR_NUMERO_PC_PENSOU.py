from random import randint
from time import sleep

n = randint(0, 5)
p = int (input('Digite um numero de 0 a 5 e tente acertar o que o PC pensou!'))
print ('-=-'*20)
print ('PROCESSANDO...')
sleep(3)
if n == p:
    print ('Voce venceu!! PARABÉNS!!')
else:
    print ('Voce perdeu!! TENTE NOVAMENTE!!')
print ('-=-'*20)
