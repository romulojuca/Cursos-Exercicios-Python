def fatorial(n, show=False):
    """ n: Numero a ser calculdado
        show: (opcional) Mostrar ou Não a conta!
        return: O valor do Fatorial de um numero 'n'...
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c        
        if show == True:
            print(f'{c} ', end='')
            print(f'x ' if c > 1 else '= ', end='')
    return f


help(fatorial)
print(f'{fatorial(5, show=True)}')
