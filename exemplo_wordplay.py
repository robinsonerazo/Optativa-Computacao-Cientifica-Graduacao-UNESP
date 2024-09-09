import wordplay

arq = open('AC-DC_letras.txt')
dic = {}

while 1:

    sub = raw_input('Entre com uma substring: ')

    tupla = wordplay.wordsub(arq,sub)

    dic[sub] = tupla
    print dic[sub]
    print 
   
