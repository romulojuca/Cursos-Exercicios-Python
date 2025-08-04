# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento 
# diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo 
# regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo 
# excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule 
# o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor 
# da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.


multa = cont_excesso = excesso = 0
while True:
    peso = float(input("Digite o peso do peixe: "))
    if peso > 50:
        excesso = peso - 50
        multa = multa + (excesso * 4)
        cont_excesso += excesso
        print(f"Esse peixe excedeu {excesso}Kg! ")
    r = input("Deseja cadastrar outro peixe? [s/n]").lower().strip()
    while r not in "sn":
        r = input("Cadastrar novo peixe? Apénas [s/n]")
    if r == "n":
        break

print(f"Teve {cont_excesso}Kg de Excesso e você irá pagar R${multa} de multa!")
