#------------------------------  LISTAS -------------------------------

lanche = ['lanche', 'suco', 'pizza', 'sorvete', 'cookie']

lanche.insert(0, 'cachorro quente')#adiciona 'cachorro quente' na posição 0
lanche.append('banana')#adiciona 'banana' no final
lanche.remove('pizza')#REMOVE 'pizza' da lista e todos os itens da frente voltam uma casa!
lanche.pop(3)#REMOVE o item na posição 3 e todos os itens da frente voltam uma casa!
del lanche[3]#REMOVE o item na posição 3 e todos os itens da frente voltam uma casa!
print(lanche)

valores = [8,1,5,2,7,0,3,9]
valores.sort()#coloca os valores em ordem numerica
valores.sort(reverse=True)#coloca os valores em ordem numerica de traz para frente
print(valores)

num = []
num.append(5)
num.append(9)
num.append(4)
