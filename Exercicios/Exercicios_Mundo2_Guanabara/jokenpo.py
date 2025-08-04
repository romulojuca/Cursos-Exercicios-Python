from random import choice, shuffle, randint, random

pedra = str ('pedra')
papel = str ('papel')
tesoura = str ('tesoura')
lista = (pedra, papel, tesoura)
r = choice(lista)
print ('-=-'*20)
print ('Vamos jogar Jokenpô !')
print ('-=-'*20)
p = (input('Escolha Pedra, Papel ou Tesoura  ')).strip().lower()

if r == 'pedra' and p == 'tesoura':
    print('{}!!!! Você Perdeu!'.format(r).upper())
elif r == 'papel' and p == 'pedra':
    print('{}!!!! Você Perdeu! '.format(r).upper())
elif r == 'tesoura' and p == 'papel':
    print('{}!!!! Você Perdeu! '.format(r).upper())
elif r == 'pedra' and p == 'papel':
    print('{}!!!! Você Ganhou! '.format(r).upper())
elif r == 'papel' and p == 'tesoura':
    print('{}!!!! Você Ganhou! '.format(r).upper())
elif r == 'tesoura' and p == 'pedra':
    print('{}!!!! Você Ganhou! '.format(r).upper())
elif r == 'pedra' and p == 'pedra':
    print ('{}!!!! Empate Haha! '.format(r).upper())
elif r == 'papel' and p == 'papel':
    print ('{}!!!! Empate Haha! '.format(r).upper())
elif r == 'tesoura' and p == 'tesoura':
    print ('{}!!!! Empate Haha! '.format(r).upper())
