# Recursividade

# Fórmula geral para o fatorial:


def fatorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fatorial(num - 1)


if __name__ == '__main__':
    x = int(input('Digite um numero inteiro positivo! '))
    try:
        res = fatorial(x)
    except RecursionError:
        print(f'O numero fornecido é muito grande ou negativo!')
    else:
        print(f'O fatorial de {x} é {res}')
