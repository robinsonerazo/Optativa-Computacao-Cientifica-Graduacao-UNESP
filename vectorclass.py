# -*- coding: cp1252 -*-

import math

class Vector(object):

    def __init__(self, x = 0., y = 0., z = 0.):
        self.x = x
        self.y = y
        self.z = z
        self.mod = ( self | self ) ** 0.5

    def __add__(self,other):
        return Vector(x = self.x + other.x,
                      y = self.y + other.y,
                      z = self.z + other.z )

    def __sub__(self,other):
        return Vector(x = self.x - other.x,
                      y = self.y - other.y,
                      z = self.z - other.z )

    def __mul__(self,alfa):
        return Vector(alfa * self.x,
                      alfa * self.y,
                      alfa * self.z )

    def __rmul__(self,alfa):
        return Vector(alfa * self.x,
                      alfa * self.y,
                      alfa * self.z )

    def __or__(self,other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __xor__(self,other):
        return Vector(self.y * other.z - self.z * other.y,
                      self.z * other.x - self.x * other.z,
                      self.x * other.y - self.y * other.x)

    def __lt__(self,other):
        return math.degrees (math.acos( (self | other) / (self.mod * other.mod)))
    
    def __neg__(self):
        return self * (-1)

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

        if self.z < 0.:
            vet += ' %.3fk' %self.z
        else:
            vet += ' +%.3fk' %self.z
            
        return vet

# Instanciando os versores para quando se importa a classe
ex = Vector(1.)
ey = Vector(0.,1.)
ez = Vector(0., 0., 1.)

if __name__ == '__main__':

    alfa = 10
    v1 = Vector(3., -4., 2.)
    v2 = Vector(5., 3., -6.)
    v3 = v1 + v2
    v4 = v1 - v2

    print 'Vetor 1: ' , v1
    print 'Vetor 2: ' , v2
    print 'Soma vetorial: ', v3
    print 'Subtração vetorial: ', v4
    print 'Produto por escalar: ',v1 * alfa
    print 'Produto interno: ',v1 | v2 ,',', v2 | v1
    print 'Produto Externo de i ^ j: ', ex ^ ey
    print 'Produto Externo de j ^ i: ', ey ^ ex
    print 'Ângulo entre vetores 1 e 2: ', v1 < v2,'°'
    print 'Ângulo entre vetores i e j: ', ex < ey,'°'
                      
        
