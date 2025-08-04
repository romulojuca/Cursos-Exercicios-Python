# Escopo global e Local

varGlobal = 'Curso de Python'

def escreve_texto():
    global varGlobal
    print(varGlobal)
    varGlobal = 'Curso EscreveTexto'
    varLocal = 'LOCAL'
    print(varLocal)


escreve_texto()
print(varGlobal)