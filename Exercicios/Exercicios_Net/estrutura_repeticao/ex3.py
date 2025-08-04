# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

nome = str(input("Digite um nome com mais de 3 caractéres! "))
idade = int(input("Digite uma idade entre 0 e 150 anos! "))
salario = float(input("Digite um salário acima de 0: "))
sexo = str(input("Digite seu sexo 'f' ou 'm'")).upper().strip()
estado_civil = str(input("Estado civil use 's', 'c', 'v', 'd'")).strip().upper()

while True:
    if len(nome) <= 3:
        nome = str(input("Digite um nome com mais de 3 caractéres! "))
    elif idade < 0 or idade > 150:
        idade = int(input("Digite uma idade entre 0 e 150 anos! "))
    elif salario < 0:
        salario = float(input("Digite um salário acima de 0: "))
    elif sexo not in 'FM':
        sexo = str(input("Digite seu sexo 'f' ou 'm': ")).strip().upper()
    elif estado_civil not in 'SCVD':
        estado_civil = str(input("Estado civil use 's', 'c', 'v', 'd': ")).strip().upper()
    if len(nome) >= 4 and idade >= 0 and idade <= 150 and salario > 0 and sexo in "MF" and estado_civil in "SCVD":
        break

print(nome)
print(idade)
print(salario)
print(sexo)
print(estado_civil)
