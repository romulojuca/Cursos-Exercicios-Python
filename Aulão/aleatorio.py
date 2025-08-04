import random

for i in range(1, 6):
    print(random.randint(1, 50))

for i in range(5):
    # arredonda para 2 casas decimais i gual o :.2f
    # random.random vai de 0 a 1
    print(f'{round(random.random() * 10, 2)}')

valor = random.uniform(1, 100)
print(f'{valor:.4f}')

lista = [2, 3, 4, 5, 6, 8, 3, 3, 7, 8, 3,
         3, 0, 57, 457, 457, 456, 346, 3245, 345]
# choice escolhe 1, sample vc escolhe quantos serao selecionados
print(random.choice(lista))
print(random.sample(lista, 3))
print(lista)
random.shuffle(lista)
print(lista)
lista.sort()
print(lista)
