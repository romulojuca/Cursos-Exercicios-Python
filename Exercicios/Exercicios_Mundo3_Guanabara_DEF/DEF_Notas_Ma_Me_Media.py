def notas(*n, sit=False):
    """
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou nao adicionar a sitiação
    :return: dicionario com carias informaçoes sobre a situação da turma.
    """
    dic2 = {}
    lista = []
    media = menor = maior = cont = 0
    for c in n:
        lista.append(c)
    for p, v in enumerate(lista):
        if p == 0:
            maior = v
            menor = v
        if v > maior:
            maior = v
        if v < menor:
            menor = v
        media += v
        cont += 1
    dic2['total'] = cont
    dic2['maior'] = maior
    dic2['menor'] = menor
    dic2['média'] = media/cont
    
    if sit == True:
        if dic2['média'] < 5:
            dic2['situação'] = 'RUIM'
        if dic2['média'] >= 5:
            dic2['situação'] = 'BOA'
        return dic2
    else:
        return dic2

resp = notas(3, 3.5, 6, 8, 7.5, 8, sit=True)
help(notas)
print(resp)
