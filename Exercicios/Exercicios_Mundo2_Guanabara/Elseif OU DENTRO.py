nome = str (input ('Digite seu nome! '))
if nome == ('Romulo'):
    print ("Que nome bonito, {}!!".format(nome))
elif nome == "Thais" or nome == "Pedro" or nome == "Lucas":
    print ('Seu nome é bem comum no Brasil, {}!'.format(nome))
elif nome in "Ana Mariana Karina Maria":
    print ("QUe belo nome feminino {}".format (nome))
else:
    print ("Seu nome é dificil de encontrar, {}!".format(nome))
