# -*- coding: cp1252 -*-
import numpy as np
import scipy as sp
import pylab as pl

#Cria função polinomial

p = sp.poly1d([3,4,5])
print p
print p.coeffs
print p.deriv(2)
pi = p.integ(4)
print 'Integraçao a 4\n' ,pi
print 'Ordem', p.order
p.variable

# Criando Nan

p = sp.NAN
print p

#Criando vetores de intervalos diferentes

a = sp.r_[0.05:10:5j , 11:50:1 , 50:500:100] #j ?
print a

#Para ângulos
angulo = sp.r_[-sp.pi:sp.pi:361j] #rad
print angulo
angulo = sp.degrees( sp.r_[-sp.pi:sp.pi:361j] )#em graus
print angulo

k = 2
angulo = sp.degrees( sp.r_[-sp.pi:sp.pi:(k*360+1)*1j] )#em graus
print angulo

