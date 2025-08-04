#A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.

maior = 500

primeiro = 0
segundo = 1
terceiro = 0
contador = 0

print(f"Sequência -> {primeiro} -> {segundo} -> ",end='')


while terceiro <= 500:
    terceiro = primeiro + segundo
    print(f"{terceiro} -> ", end='')
    primeiro = segundo
    segundo = terceiro

print(f"FIM!")
