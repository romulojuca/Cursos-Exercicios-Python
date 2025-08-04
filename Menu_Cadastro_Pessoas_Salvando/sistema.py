from lib.interface import leiaInt, menu
from lib.arquivo import *

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

cabeçalho('SISTEMA ARQUIVO v1.0')
while True:
    resposta = menu(['Ver Pessoas cadastradas',
                    'Cadastrar nova Pessoa', 'Sair do sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar nova pessoa!
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
