# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados 
# da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados 
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que 
# custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# a) comprar apenas latas de 18 litros;
# b) comprar apenas galões de 3,6 litros;
# c) misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e 
# sempre arredonde os valores para cima, isto é, considere latas cheias.

area = float(input("Qual o tamanho da área a ser pintada em m²? "))
cont_qnt_latas = cont_qnt_galoes = 0
litros_necessarios = (area / 6)
qnt_latas = litros_necessarios / 18
qnt_galoes = litros_necessarios / 3.6
litros_necessarios = (litros_necessarios * 0.1) + litros_necessarios
print(f"Se for comprar só latas precisará de {qnt_latas.__ceil__()} latas e irá custar R${80 * qnt_latas.__ceil__():.2f}")
print(f"Se for comprar só galões precisará de {qnt_galoes.__ceil__()} galões e irá custar R${25 * qnt_galoes.__ceil__():.2f}")
while True:
    if litros_necessarios >= 18:
        cont_qnt_latas += 1
        litros_necessarios -= 18
    if litros_necessarios < 18:
        if litros_necessarios >= 3.6:
            cont_qnt_galoes += 1
            litros_necessarios -= 3.6
        else:
            break
if litros_necessarios > 0:
    cont_qnt_galoes += 1
print(f"Para um menor desperdício compre {cont_qnt_latas} lata e {cont_qnt_galoes} galões, com o custo de R${(cont_qnt_galoes * 25) + (cont_qnt_latas * 80):.2f}")
