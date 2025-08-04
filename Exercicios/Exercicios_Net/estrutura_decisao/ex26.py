#Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro. Escreva um algoritmo que leia o número de litros vendidos,
# o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a
# ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

def calculo(litros, tipo):
    if tipo == 'A':
        if litros <= 20:
            return (litros * alcool) - (litros * alcool * 0.03)
        elif litros > 20:
            return (litros * alcool) - (litros * alcool * 0.05)
    if tipo == 'G':
        if litros <= 20:
            return (litros * gasolina) - (litros * gasolina * 0.04)
        elif litros > 20:
            return (litros * gasolina) - (litros * gasolina * 0.06)


litros_vendidos = float(input("Digite a quantidade de litros: "))
tipo_combustivel = str(input("Tipo do combustível A-álcool, G-gasolina: ")).strip().upper()
alcool = 1.90
gasolina = 2.50

print(f"Você irá pagar R${calculo(litros_vendidos, tipo_combustivel):.2f} com o desconto!")
