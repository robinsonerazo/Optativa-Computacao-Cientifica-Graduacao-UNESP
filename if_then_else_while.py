# -*- coding: cp1252 -*-
print ''' Entre com um n�mero  que tem que
          ser float ou inteiro, positivo ou
          negativo. De fato, o programa n�o
          permite qualquer outra coisa como
          imput... Experimente!'''

lista = []
count = 1
MAX_COUNT = int( raw_input('Entre com o n�mero m�ximo de n�meros: ') )

while count <= MAX_COUNT:

    num_float = False
    while  not num_float:
        
        numSt = raw_input(u'Entre com um n�mero: ')
        
        try:
            numero = float(numSt)            
        except ValueError:
            print u'\nDeve ser um n�mero, seu malandrinho! Tente outra vez...\n'
            continue  # Retorna ao while

        num_float = True

        if numero < 0. :
            print u'� negativo.\n'

        elif numero < 50. :
            print u'� menor do que 50.\n'

        elif numero < 100. :
            print u'� menor do que 100.\n'
            
        else:
            print u'� maior ou igual a 100.\n'

        lista.append(numero)
        print lista

        if  1 < count < MAX_COUNT:      print 'Outra vez...'
        count += 1
        
