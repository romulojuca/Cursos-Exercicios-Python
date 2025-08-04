def div(k, j):
    if j != 0:
        return k / j
    else:
        return 'Impossivel dividir por 0'


def quadrado(valor):
    quadrados = []
    for x in valor:
        quadrados.append(x ** 2)
    return quadrados


def contar(num=11, caracter='+'):
    for i in range(1, num):
        print(caracter, end=' ')


def soma(a, b, c=0):
    if c == 0:
        return a * b
    else:
        return a + b + c


# usado para separar a area aonde criar as funções, classes etc da area que executa
# ela indica o ponto principal de entrada no programa e separar organizando melhoe o codigo
if __name__ == '__main__':
    a = int(input('Digite um numero: '))
    b = int(input('Digite um numero: '))

    r = div(a, b)
    print(r)

    valores = [2, 5, 7, 9, 12]
    resultados = quadrado(valores)
    print(resultados)

    contar(8, '@')
    print(soma(5, 6))
