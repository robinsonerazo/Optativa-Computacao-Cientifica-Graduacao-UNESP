class ProgressaoAritmetica(object):
    def __init__(self,a1,incr):
            self.a1 , self.incr = a1 , incr

    def __getitem__(self,key):

            if not isinstance( key , (int,long)  ): raise TypeError
            if key <= 0: raise IndexError
            return self.a1 + (key-1) * self.incr

    def soma(self,n):
        return ( self[1] + self[n] ) * n/2

    
