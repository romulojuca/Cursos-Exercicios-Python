# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                       Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de
# carne da promoção, porém não há limites para a quantidade de carne por cliente. Se
# compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre
# o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada
# pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade
# de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.


def calcular(pdt, kg):
    if pdt == 'FILEDUPLO' and kg <= 5:
        return float (kg * 4.9)
    if pdt == 'FILEDUPLO' and kg > 5:
        return float (kg * 5.8)
    if pdt == 'ALCATRA' and kg <= 5:
        return float (kg * 5.9)
    if pdt == 'ALCATRA' and kg > 5:
        return float (kg * 6.8)
    if pdt == 'PICANHA' and kg <= 5:
        return float (kg * 6.9)
    if pdt == 'PICANHA' and kg > 5:
        return float (kg * 7.8)


print('-- hypermercado tabajara --'.upper().center(40))
produto = str(input("Escolha um produto (File Duplo - Alcatra - Picanha) ")).strip().upper().replace(' ', '')
kg = float(input("Quantos Kg deseja comprar? "))

valor = calcular(produto, kg)
while True:
    r = input(f"Ficou R${valor:.2f}, gostaria de pagar no cartão tabajara e ganhar 5% de desconto? Digite [s/n]").lower().strip()
    if r == "s" or r =="n":
        break

print("Nota Fiscal".center(40).upper())
print(f"{'Produto':<30} {produto}")
print(f"{'Quantidade':<30} {kg}")
print(f"{'Valor':<30} {valor}")
print(f"{'Forma de Pagamento':<31}", end="")
print(f"{'Cartão Tabajara'}") if r =='s' else print(f"{'Dinheiro'}")
print(f"{'Total':<31}", end="")
print(f"{valor}") if r == 'n' else print(f"{valor - (valor * 0.05)}")
