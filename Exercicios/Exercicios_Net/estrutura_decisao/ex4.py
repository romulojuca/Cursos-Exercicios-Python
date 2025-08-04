# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = str(input("Digite uma letra! "))
if letra.isalpha():
    if letra in "aeiou":
        print("Você digitou uma vogal!")
    else:
        print("Você digitou uma consoante!")
else:
    print("Você nao digitou uma letra!")
