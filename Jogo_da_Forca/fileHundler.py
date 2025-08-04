def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')  # leitura
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')  # w cria um arquivo se nao existir
        a.close()
    except:
        print('Erro na criação')
    else:
        print(f'Arquivo {nomeArquivo} criado com sucesso!\n')


def abrirArquivoLeitura(nomeArquivo):
    try:
        a = open(nomeArquivo, 'r')
    except:
        print('Nao foi possivel abrir para leitura')
    else:
        print(f'Arquivo {nomeArquivo} aberto com sucesso!\n')
    return a


def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print('ERRO ao ler o arquivo.')
    else:
        dados = a.readlines()
    finally:
        a.close()
        return dados


def inserir_score(nomeArquivo, nomeJogador, score):
    try:
        a = open(nomeArquivo, 'at')
    except:
        print('ERRO ao ler o arquivo.')
    else:
        a.write('{} com {} Pontos.\n'.format(nomeJogador, score))
    finally:
        a.close()
