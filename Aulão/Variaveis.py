print('Hello, World!')

media = 0
nome = 'Romulo'
nome, idade = 'Romulo', 34
n1 = n2 = n3 = n4 = 0.0
estado = True

# Funções Type()
print(type(media))
print(type(n2))
print(type(nome))
print(type(estado))
print(type(1+2j))

# Função isinstance()
# Retorna T ou F

a = 10
b = 'Sol'
print(isinstance(a, int))
print(isinstance(b, str))
print(isinstance(b, float))
print(isinstance(a, (int, float))) # Se é de um ou outro tipo
