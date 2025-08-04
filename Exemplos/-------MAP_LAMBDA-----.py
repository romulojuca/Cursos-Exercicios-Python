numbers = [1, 2, 3, 4, 5]
squared_nums = map(lambda x: x ** 2, numbers)
print(list(squared_nums))


numberss = [1, 2, 3, 4, 5]
def square(number):
    return number ** 2


squared_numss = map(square, numberss)
print(list(squared_numss))

valores = [100.53, 67.89, 999.01]

impostos = map(lambda cadaValor: cadaValor * 0.3, valores)
print(f'{list(impostos)}')
