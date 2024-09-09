# -*- coding: cp1252 -*-

"Exemplo de Herança"

import math
import vectorclass as vc

class Vector2D(vc.Vector):

    def __init__(self, x = 0., y = 0.):
        vc.Vector.__init__(self, x, y)

    def __repr__(self):

        vet = ''

        if self.x < 0.:
            vet += '%.3fi' %self.x
        else:
            vet += ' +%.3fi' %self.x

        if self.y < 0.:
            vet += ' %.3fj' %self.y
        else:
            vet += ' +%.3fj' %self.y
            
        return vet

if __name__ == '__main__':

    v1 = Vector2D( 3. , -4.)
    v2 = Vector2D( -5., 2.)

    print v1+v2
    print
    print v1^v2,'   ', v1|v2
    print
    print v1.mod
