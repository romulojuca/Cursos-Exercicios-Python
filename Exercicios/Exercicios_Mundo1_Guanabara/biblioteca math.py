#ceil (ARREDONDA PRA CIMA) 
#floor(ARREDONDA PRA BAIXO) 
#trunc (Elimina da virgula pra frente sem arredondar)

import math
import random

num = (int (input('Digite um numero: ')))
raiz = math.sqrt(num)
print ('A raiz de {} é {}'.format(num, math.ceil(raiz)))


#Numero aleatorio
num1 = random.randint(1,10)
print (num1)