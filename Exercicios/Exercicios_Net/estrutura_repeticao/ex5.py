#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

anos = 0
pais_a = int(input("Digite a populacao do pais A: [1000 até 1000000] "))
cres_a = float(input("Digite a taxa de crescimento do pais A: [1 a 5%] "))
pais_b = int(input("Digite a populacao do pais B: [1000 até 1000000] "))
cres_b = float(input("Digite a taxa de crescimento do pais B:[1 a 5%] "))

while True:
    if pais_a < 1000 or pais_a > 1000000:
        pais_a = int(input("Digite a populacao do pais A: [1000 até 1000000] "))
    if cres_a < 1 or cres_a > 5:
        cres_a = float(input("Digite a taxa de crescimento do pais A: [1 a 5%] "))
    if pais_b < 1000 or pais_a > 1000000:
        pais_b = int(input("Digite a populacao do pais B: [1000 até 1000000] "))
    if cres_b < 1 or cres_b > 5:
        cres_b = float(input("Digite a taxa de crescimento do pais B:[1 a 5%] "))
    if pais_a >= 1000 and pais_b >= 1000 and pais_a <= 1000000 and pais_b <= 1000000 and cres_a >= 1 and cres_b >= 1 and cres_a <= 5 and cres_b <= 5:
        break

if pais_a >= pais_b:
        print("A população do pais A já é maior que o país B!")
else:
    while True:
        if pais_a < pais_b:
            pais_a = (pais_a * (cres_a/100)) + pais_a
            pais_b = (pais_b * (cres_b/100)) + pais_b
            anos = anos + 1
            print(anos)
        else:
            print(f"Irá demorar {anos} anos para população do país A passar ou se igualar a do país B.")
            break
