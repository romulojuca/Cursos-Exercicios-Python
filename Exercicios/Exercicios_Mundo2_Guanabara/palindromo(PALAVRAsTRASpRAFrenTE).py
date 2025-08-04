frase = str (input('Digite uma frase: ')).strip().upper()

corte = frase.split()
junta = ''.join(corte)
t = junta [::-1] #Aqui t = junta do começo ao final de TRAZ para FRENTE!!!
'''t = ''
for c in range (len(junta)-1, -1, -1):
    t = t + junta[c]'''
print ('A frase {}, digitada ao contrario fica {}'.format(junta, t))
if t == junta:
    print('A frase é um Palíndromo!')
else:
    print ('A frase não é um Palíndromo!')
