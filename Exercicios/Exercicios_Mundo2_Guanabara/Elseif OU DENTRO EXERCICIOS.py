from datetime import date

valc = (float(input('Digite o valor da casa a ser comprada: ')))
salario = float (input('Digite o salário do comprador: '))
anos = int (input('Digite em quantos anos será dividido o financiamento: '))
meses = (anos*12)
if (valc/meses) > (salario*0.3):
    print ('Infelizmente voce na vai poder financiar essa casa somente neste periodo!!')
else:
    print ('Parabéns você pode comprar esta casa!')
 
n1 = int (input('Digite o primeiro numero inteiro: '))
n2 = int (input('Digite o segundo numero inteiro: '))
if n1 > n2:
    print ('O primeiro numero é maior!')
elif n2 > n1:
    print ('O segundo numero é maior!!')
else:
    print ('Não existe valor maior, os dois são iguais!!')

anon = int (input('Digite seu ano de nascimento: '))
data = date.today().year
if (data-anon) == 18:
    print ('Está na hora de se alistar!!')
elif (data-anon) > 18:
    print ('Ja passou {} ano(s) do tempo de se alistar!'.format((data-anon)-18))
else:
    print ('Falta {} anos para vc se alistar'.format(18-(data-anon)))
