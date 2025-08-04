d = int (input('Digite quantos Km voce quer viajar '))
if d <= 200:
    print ('Com uma distancia de {}Km voce vai gastar R${:.2f}.'.format(d, d*0.5))
else:
    print ('Com uma distancia de {}Km voce vai gastar R${:.2f}.'.format(d, d*0.45))