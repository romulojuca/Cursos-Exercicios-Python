import fileHundler as fh
from random import choice
import desenhos as d


def jogar():
    lista_palavras = []
    arquivo = fh.abrirArquivoLeitura('palavras.txt')
    # abrindo o txt para voltar as palavras em uma lista
    for linha in arquivo:
        palavra = linha.strip()
        lista_palavras.append(palavra)
    # selecionando uma palavra aleatoria no txt
    palavra_sorteada = choice(lista_palavras)

    for i in range(15):
        print()

    digitadas = []
    acertos = []
    erros = 0

    nome = input('Nome: ')

    while True:
        adivinha = d.imprimir_palavra_secreta(palavra_sorteada, acertos)

        # VITORIA
        if adivinha == palavra_sorteada:
            print('Voce acertou!')
            break

        # Tentativas
        tentativa = input('\nDigite uma letra: ').lower().strip()
        if tentativa in digitadas:
            print('Voce ja usou esta letra!')
            continue
        else:
            digitadas.append(tentativa)
            if tentativa in palavra_sorteada:
                acertos += tentativa
            else:
                erros += 1
                print(f'Você errou!')

        score = d.desenhar_forca(erros)

        # DERROTA
        if erros == 6:
            print('Enforcado!')
            print(f'A palavra era {palavra_sorteada}')
            break

    fh.inserir_score('score.txt', nome, score)
