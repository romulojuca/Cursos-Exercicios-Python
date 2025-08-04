p = float (input('Preço do produto'))
f = str (input('Escolha: dinheiro - cheque - cartao - 2x no cartao - 3x ou mais:')).strip().lower()
if f == 'dinheiro':
    print ('Voce irá pagar R${:.2f}'.format(p-(p*0.1)))
elif f == 'cheque':
    print ('Voce irá pagar R${:.2f}'.format(p-(p*0.1)))
elif f == 'cartao':
    print ('Voce irá pagar R${:.2f}'.format(p-(p*0.05)))
elif f == '2x no cartao':
    print ('Você irá pagar R${:.2f}'.format(p))
elif f == '3x ou mais':
    print ('Você irá pagar R${:.2f}'.format(p+(p*0.2)))
