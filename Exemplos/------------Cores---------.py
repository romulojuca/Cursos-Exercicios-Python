#cores do texto: 30 Branco - 31 Verme - 32 verde - 33 Amarelo - 
# 34 azul - 35 Roxo - 36 azul claro - 37 cinza

#Codigo de fundo: 40 Branco... IGUAL OS DE CIMA

#estilo: 0 nada - 1 Negrito (bold) - 4 Underline - 
# 7 negative (inverte as cores do texto e de fundo)

n = 'Aula de Python'
print(f'\033[31;35;4m{n}\033[m')
