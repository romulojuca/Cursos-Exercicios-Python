# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                       Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
# receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade
# (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

kg_morango = float(input("Quantos Kg de Morango deseja comprar? "))
kg_maca = float(input("Quantos Kg de Maça deseja comprar? "))
total_kg = kg_maca + kg_morango

if kg_morango <= 5:
    valor_morango = kg_morango * 2.5
elif kg_morango > 5:
    valor_morango = kg_morango * 2.2
if kg_maca <= 5:
    valor_maca = kg_maca * 1.8
elif kg_maca > 5:
    valor_maca = kg_maca * 1.5

valor_total = valor_maca + valor_morango

if total_kg > 8 or valor_total > 25:
    valor_total = valor_total - (valor_total * 0.1)

print(f"Você irá pagar {valor_total:.2f}")
