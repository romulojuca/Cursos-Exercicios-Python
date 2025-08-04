def leiaInt(num):
    while True:
        try:
            n = int(input(num))
        except (ValueError, TypeError):
            print('Apenas numeros inteiros')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuario preferiu nao digitar esse numero! \033[m')
            return 0
        except ZeroDivisionError:
            print('Não é possivel dividir um numero por 0!')
        else:
            return n


n = leiaInt('Digite um numero: ')
print(f'{n}')
