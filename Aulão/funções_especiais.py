# Funções lambda (anõnimas)
from functools import reduce


def quadrado(x): return x**2


def par(x): return x % 2 == 0


def f_c(f): return (f - 32) * 5/9


for i in range(1, 11):
    print(quadrado(i))

print(par(8))
print(par(9))

print(f_c(212))

# map(função, iterável) USADO PARA COISAS ITERAVEIS lista, tupla, string
num = [1, 2, 3, 4, 5, 6, 7, 8]
dobro = list(map(lambda x: x*2, num))
print(dobro)

palavras = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação']
maiúsculas = list(map(str.upper, palavras))
print(maiúsculas)

# Função filter()
# Sintaxe:
# filter(função, sequência)


def numeros_pares(n):
    return n % 2 == 0


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Ele vai filtrar o que é True e jogar o valor dentro da lista (No caso de a função retornar T ou F ele retorna o valor da variavel e nao T or F)
num_par = list(filter(numeros_pares, numeros))
print(num_par)

num_impar = list(filter(lambda x: x % 2 != 0, numeros))
print(num_impar)

for i, e in enumerate(numeros):
    if e % 2 == 0:
        print(e)

# Função reduce() RETORNA 1 VALOR
# Sintaxe:
# reduce(função, sequência, valor_inicial)


def mult(x, y):
    return x * y


numeros1 = [1, 2, 3, 4, 5]
total = reduce(mult, numeros1)
print(total)

# Soma cumulativa dos quadrados de valores, usando lambda

numero = [1, 2, 3, 4]
