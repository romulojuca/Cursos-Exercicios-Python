"""Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do
Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto
menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20%
Imprima na tela as informações, dispostas conforme o exemplo abaixo.
No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
"""
irrf = 0
sindicato = 0.03
inss = 0.1
fgts = 0.11
horas = int(input("Digite o numero de horas trabalhadas esse mês: "))
valor_hora = float(input("Digite o valor da hora: "))
salario_bruto = horas * valor_hora
if salario_bruto > 900 and salario_bruto <= 1500:
    irrf = 0.05
if salario_bruto > 1500 and salario_bruto <= 2500:
    irrf = 0.1
if salario_bruto > 2500:
    irrf = 0.2

total_desconto = (salario_bruto * irrf) + (salario_bruto * inss) + (salario_bruto * sindicato)

print("Holerite".center(40))
print(f"{f'Salário Bruto: ({valor_hora} * {horas})':<33} : R$ {salario_bruto}")
print(f"{f'(-) IR ({irrf * 100:.0f}%)':<33} : R$ {salario_bruto * irrf}")
print(f"{f'(-) INSS ({inss * 100:.0f}%)':<33} : R$ {salario_bruto * inss}")
print(f"{'FGTS (11%)':<33} : R$ {salario_bruto * fgts}")
print(f"{'Total de descontos':<33} : R$ {total_desconto}")
print(f"{'Salário Líquido':<33} : R$ {salario_bruto - total_desconto}")
