# -*- coding: cp1252 -*-

def wordsub(arq,sub):
# arq = open('AC-DC_letras.txt')

    '''\n
    Função para determinar o número de palavras em um arquivo
qualquer arq que contem um determinada substring sub. A fun-
ção retorna um dicionário contendo o número de palavras, nú-
mero total de palavras do arquivo, a frequência e a lista de
palavras.
    '''
     
    count = 0
    count_words = 0
    lista = []

    for linha in arq:
        wordst = linha.strip('\n')
        words = wordst.split()
        for word in words:
            if sub in word:
                count += 1
                lista.append(word)
            count_words += 1
        
    freq = (100.*count)/count_words

    ret = sub,count,count_words,freq,lista
    arq.close()

    return ret

if __name__ == '__main__':
    print wordsub.__doc__
    arqu = open('AC-DC_letras.txt')
    sub = 'back'
    sub,count,count_words,freq,lista = wordsub(arqu,sub)
    print sub,count,count_words,freq,lista
            
