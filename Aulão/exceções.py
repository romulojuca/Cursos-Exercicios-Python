# Exceções e Erros
# Bloco try... except

def div(k, j):
    return round(k / j, 2)


if __name__ == '__main__':
    while True:
        try:
            n1 = int(input('Digite o primeiro numero: '))
            n2 = int(input('Digite osegundo numero: '))
            break
        except ValueError:
            print('Ocorreu um erro ao pegar o valor, tente novamente!')

    try:
        r = div(n1, n2)
    except ZeroDivisionError:
        print(f'Não é possivel dividir por zero!')
    else:
        print(f'Resultado: {r}')
    finally:
        print('Fim do cálculo!')
