import jogo as j
import fileHundler as fh


def mostrar_menu():
    print("="*30)
    print(' ' * 7 + "JOGO DA FROCA")
    print("="*30)
    print("\n1 - JOGAR")
    print("2 - SCORE")
    print("3 - SAIR")
    print("="*30)


arquivo = "score.txt"
if fh.existeArquivo(arquivo):
    print('Arquivo Localizado')
else:
    print('ARQUIVO NAO EXISTE.')
    fh.criarArquivo(arquivo)

while True:
    mostrar_menu()
    opcao = int(input('Escolha a opção: '))
    match opcao:
        case 1:
            print('Iniciando...')
            j.jogar()
        case 2:
            print('SCORE')
            dados = fh.listarArquivo('score.txt')
            if not dados:
                print('Score vazio')
            else:
                i = 1
                for jogador in dados:
                    print(f'{i} -> {jogador}')
                    i += 1
        case 3:
            print('Saindo do jogo. até!')
            break
