sexo = str(input('Informe seu sexo [M/F]: ')).upper().strip()[0]

while sexo not in 'MmFf':
    sexo = str(input('Sexo invalido, digite novamente! ')).upper().strip()[0]
    if sexo == 'M':
        print ('Sexo masculino registrado com sucesso!')
    elif sexo == 'F':
        print ('Sexo feminino registrado com sucesso!')
