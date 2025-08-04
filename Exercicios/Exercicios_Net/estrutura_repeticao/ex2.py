#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

nome = str(input("usuario: "))
senha = str(input("senha: "))

while True:
    if nome == senha:
        print("O nome e a senha nao podem ser iguais!")
        nome = str(input("usuario: "))
        senha = str(input("senha: "))

    elif nome != senha:
        print("Usuario cadastrado com sucesso!")
        break
