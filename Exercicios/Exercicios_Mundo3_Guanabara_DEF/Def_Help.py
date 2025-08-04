def ajuda(msg):
    print(f'\033[31;31;7m')
    return help(f'{msg}')
    print(f'\033[m')


def sistema(aqui):
    tam = len(aqui)+4
    print(f'\033[31;32;7m~'*tam)
    print(f'  {aqui}')
    print(f'~'*tam, '\033[m')

def comando(com):
    tam = len(com)+4
    print(f'\033[31;33;7m~'*tam)
    print(f'  {com}')
    print(f'~'*tam, '\033[m')



while True:
    sistema('SISTEMA DE AJUDA PyHELP')
    r = (input('Função ou Biblioteca > '))
    if r == 'fim':
        break
    comando(f'Acessando o manual do comando {r}')
    ajuda(r)
