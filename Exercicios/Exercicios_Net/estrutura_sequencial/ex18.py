# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo 
# aproximado de download do arquivo usando este link (em minutos).

cont_minutos = 0
tam_mb = float(input("Digite o tamanho do arquivo em MB: "))
velocidade_mbps = float(input("Digite a velocidade do link de internet em Mbps: "))
segundos = int(tam_mb / (velocidade_mbps / 8))
while True:
    if segundos >= 60:
        cont_minutos += 1
        segundos -= 60
    if segundos < 60:
        break
print(f"O tempo aproximado será de {cont_minutos} minutos e {segundos} segundos.")
