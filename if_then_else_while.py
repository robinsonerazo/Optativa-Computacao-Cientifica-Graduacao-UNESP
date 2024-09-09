# -*- coding: cp1252 -*-
print ''' Entre com um número  que tem que
          ser float ou inteiro, positivo ou
          negativo. De fato, o programa não
          permite qualquer outra coisa como
          imput... Experimente!'''

lista = []
count = 1
MAX_COUNT = int( raw_input('Entre com o número máximo de números: ') )

while count <= MAX_COUNT:

    num_float = False
    while  not num_float:
        
        numSt = raw_input(u'Entre com um número: ')
        
        try:
            numero = float(numSt)            
        except ValueError:
            print u'\nDeve ser um número, seu malandrinho! Tente outra vez...\n'
            continue  # Retorna ao while

        num_float = True

        if numero < 0. :
            print u'é negativo.\n'

        elif numero < 50. :
            print u'é menor do que 50.\n'

        elif numero < 100. :
            print u'é menor do que 100.\n'
            
        else:
            print u'é maior ou igual a 100.\n'

        lista.append(numero)
        print lista

        if  1 < count < MAX_COUNT:      print 'Outra vez...'
        count += 1
        
