# -*- coding: cp1252 -*-
class PG (object):
    
    """
       As inst�ncias da classe PG representam sequ�ncias de progress�o
       geom�trica cujo termo inicial � a1 e raz�o q. Qualquer termo i
       pode ser obtido com self[i] e a soma dos termos at� i como
       self.soma(i) .
    """
    
    def __init__(self,a1,q):
            self.a1 , self.q = a1 , q

    def __getitem__(self,key):

            if not isinstance( key , (int,long)  ): raise TypeError
            if key <= 0: raise IndexError
            return self.a1 * self.q**(key-1) 

    def soma(self,n):
        try:
            return ( self[n]*self.q - self.a1 ) / (self.q - 1.)
        except ZeroDivisionError: print 'Divis�o por zero, meo!'

if __name__ == '__main__':

    print PG.__doc__
    print
    a = PG(1,2)

    print a.a1
    print a.soma(1000)
