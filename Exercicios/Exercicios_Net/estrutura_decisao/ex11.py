"""As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe
contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, 
baseado no salário atual:
-> salários até R$ 280,00 (incluindo) : aumento de 20%
-> salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
-> salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
-> salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
-> o salário antes do reajuste;
-> o percentual de aumento aplicado;
-> o valor do aumento;
-> o novo salário, após o aumento.
"""
salario_final = porcentagem = 0
salario = float(input("Digite seu salário atual: "))

if salario < 280:
    salario_final = (salario * 0.2) + salario
    porcentagem = 20
if salario >= 280 and salario < 700:
    salario_final = (salario * 0.15) + salario
    porcentagem = 15
if salario >= 700 and salario < 1500:
    salario_final = (salario * 0.1) + salario
    porcentagem = 10
if salario >= 1500:
    salario_final = (salario * 0.05) + salario
    porcentagem = 5
print(f"Você ganhava R${salario:.2f} e houve um aumento de {porcentagem:.0f}%")
print(f"Agora você irá ganhar R${salario_final:.2f}, teve um almento de R${salario_final - salario:.2f}")
