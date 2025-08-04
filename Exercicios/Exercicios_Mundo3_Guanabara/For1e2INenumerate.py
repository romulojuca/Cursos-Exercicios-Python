lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!\n')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('Comi pra caramba!\n')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba!\n')

print(sorted(lanche))
#Coloca as palavras em ordem alfabetica NAO ALTERA POSIçÃO DAS VARIAVEIS

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.count(5)) #Quantas vezes aparece o numero 5
print(c.index(8)) # Achar a PRIMEIRA VEZ que aparece o nº 8
print(c.index(5, 2))# Achar a PRIMEIRA VEZ que aparece o nº 5, DA POSIÇÃO 2 pra frente!!
                #(Começa contar desde a primeira variavel a posição!!!)

pessoa = ('Gustavo', 39, 'M', 99.88)
print(pessoa)
#del(pessoa) #Deleta a variavel 'pessoa'
#print(pessoa) #Da erro pois a variavel foi deletada e nao está definida!
