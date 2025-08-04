def escreva(txt):
    #OUTRA OPÇÃO
    #tam = len(txt) + 4
    #print(f'{("-" * tam)}')
    print(f"{('-'*(len(txt)+4))}")
    print(f'  {txt}')
    print(f"{('-'*(len(txt)+4))}")

escreva('Olá, Mundo!')
escreva('===========TESTE===========')
escreva('a')
