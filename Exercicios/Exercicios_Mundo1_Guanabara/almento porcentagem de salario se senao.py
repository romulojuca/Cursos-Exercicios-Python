s = float (input('Digite seu salario: '))
print ('Voce terá {:.2f}R$ de aumento.'.format(s*0.1) if s > 1250.00 else 'Voce terá {:.2f}R$ de aumento.'.format(s*0.15))
