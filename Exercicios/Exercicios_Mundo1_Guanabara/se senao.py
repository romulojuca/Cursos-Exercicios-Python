n1 = float (input ('Digite sua primeira nota: '))
n2 = float (input('Digite sua segunda nota: '))
m = (n1+n2)/2
print ('Sua media é {:.1f}'.format(m))
if m >= 6:
    print ('Parabéns você passou de ano!!')
else:
    print ('Voce não passou de ano! ESTUDE MAIS!!')
print ('PARABÉNS' if m>= 6 else 'ESTUDE MAIS') #SIMPLIFICADO