# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total 
# do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, 
# faça um programa que nos dê:
# a) salário bruto.
# b) quanto pagou ao INSS.
# c) quanto pagou ao sindicato.
# d) o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$

valor_hora = float(input("Quanto você ganha por Hora? "))
horas_trab = int(input("Digite o numero de horas trabalhadas no mês: "))
salario_bruto = valor_hora * horas_trab
desc_inss = salario_bruto * 0.08
desc_irrf = salario_bruto * 0.11
desc_sindical = salario_bruto * 0.05
print("*"*37)
print("Holerite".center(40))
print("*"*37)
print(f"{'+ Salário Bruto :':<25} R${salario_bruto:<8}*")
print(f"{'- IR (11%) :':<25} R${desc_irrf:<8}*")
print(f"{'- INSS (8%) :':<25} R${desc_inss:<8}*")
print(f"{'- Sindicato ( 5%) :':<25} R${desc_sindical:<8}*")
print(f"{'= Salário Liquido :':<25} R${salario_bruto - desc_inss - desc_irrf - desc_sindical:<8}*")
print("*"*37)
