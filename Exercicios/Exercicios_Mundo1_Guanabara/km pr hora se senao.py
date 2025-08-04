km = int (input('Entre com a velocidade do carro em KM/h'))
print ('Parabéns voce está na velocidade permitida' if km <= 80 else 'Voce ultrapassou a velocidade e vai pagar uma multa de {}R$'.format((km-80)*7))
