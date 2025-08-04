nome = 'Curso de Python'
instrutor = 'Romulo'
print(nome + ' com ' + instrutor)
frase = 'vamos aprender python hj'
# split quebra a frase em blocos separados por espaço por padrao
palavras = frase.split()
print(palavras)
for i in palavras:
    print(i)

for i in nome:
    print(i)

print(frase[6:21])
print(frase[-3:])
email = input('Digite seu email! ')
arroba = email.find('@')
usuario = email[:arroba]
dominio = email[arroba+1:]
print(f'Usuario: {usuario}, Dominio: {dominio}')

produtos = 'carbonato de sódio e óxido de zinco'
print('sódio' in produtos)
print('magnésio' not in produtos)
# find se nao achar retorna -1 se achar retorna em que posição começa
item = 'hipoclorito'
pos = item.find('clor')
print(pos)

# .capitalize muda a primeira letra para maiuscula
objeto = 'joGuei o daDo'
print(objeto.capitalize())
# .title ele coloca cada letra de cada palavra maiuscula e o resto minuscula
print(objeto.title())

suplemento = 'cloreto de magnésio'
n_suple = suplemento.replace('magnésio', 'zinco')  # replace
print(n_suple)

frase = '     Romulo  A G Rueda  '
print(frase.strip())#lstrip, rstrip e strip todos espaços

fruta = 'Abacatee'
print(fruta)
print(fruta.rjust(20))#20 espaços no total e a palavra justificada a direita
print(fruta.center(12))# centraliza contando o valor total de caracteres
print(fruta.ljust(16, '-'))

p = 'Bóson Treinamentos'
print(p.startswith('b'))#retorna T ou F.. para ver se começa com a letra
print(p.endswith('s'))# para ver se termina com a letra

"""
Docstring é uma documentação no Python
"""
