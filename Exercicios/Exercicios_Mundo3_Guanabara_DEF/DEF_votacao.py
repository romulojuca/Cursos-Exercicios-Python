def voto(n):
    from datetime import date
    ano = date.today().year
    idade = ano - n
    return idade


nascimento = int(input('Ano de nascimento: '))
voto(nascimento)
if voto(nascimento) >= 18 and voto(nascimento) <= 65:
    print(f'Com {voto(nascimento)} anos: Voto obrigatorio!')
if voto(nascimento) > 65:
    print(f'Com {voto(nascimento)} anos: Voto opcional!')
if voto(nascimento) < 18:
    print(f'Com {voto(nascimento)} anos: Não VOTA')
