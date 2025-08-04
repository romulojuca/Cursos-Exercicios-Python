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


def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(f'\033[0;34m{txt.center(42)}\033[m')
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[32m{c}\033[m - \033[33m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua Opção: \033[m')
    return opc
