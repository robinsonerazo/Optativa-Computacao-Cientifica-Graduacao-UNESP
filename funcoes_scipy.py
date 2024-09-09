# -*- coding: cp1252 -*-
import numpy as np
import scipy as sp
#import pylab as pl

#Cria fun��o polinomial

p = sp.poly1d([3,4,5])
print p
print p.coeffs
print p.deriv(2)
pi = p.integ(4)
print 'Integra�ao a 4\n' ,pi
print 'Ordem', p.order
p.variable

# Criando Nan

p = sp.NAN
print p

#Criando vetores de intervalos diferentes

a = sp.r_[0.05:10:5j , 11:50:1 , 50:500:100] #j ?
print a

#Para �ngulos
angulo = sp.r_[-sp.pi:sp.pi:361j] #rad
print angulo
angulo = sp.degrees( sp.r_[-sp.pi:sp.pi:361j] )#em graus
print angulo

k = 2
angulo = sp.degrees( sp.r_[-sp.pi:sp.pi:(k*360+1)*1j] )#em graus
print angulo

#Fatorial
f = sp.factorial(100)
print f
f = sp.factorial(100, exact = 1)
print f

#Calcula combina��es entre elementos
print sp.comb(10,4,exact = 1) #10 elementos combinados 4 a 4

#Gerador de n�meros aleat�rios
print sp.rand(2,4,3) #array de n�meros aleat�rios
print sp.randn(2,4,3) #array de n�meros aleat�rios distribu�dos normalmente

#Integra��o num�rica >> sp.integrate()

#Equa��o diferencial ordin�ria ( odeint ) dy/dt = f(y,t)

#Otimiza��o (optimize) \\ melhor � o pacote openopt.org //
'Fun��o de Rosenbrock usado para testes de otimiza��o'

#Ajuste por m�nimos quadrados (leastsq) - importante!!!

#Minimizadores de fun��es escalares

'Computa��o Cient�fica �: otimiza��o, integra��o, interpola��o, quadrantura'

# Determina��o de ra�zes 

    #fsolve � basicamente Newton-Raphson
    #m�todo do ponto fixo
    #Grandes problemas - n�o utilize fsolve, Newton-Raphson. Use Krylov, ..

	#Fun��o np.mgrid >> produz grade em espa�o 3D'
    #pl.colorbar >> produz barra de n�veis'

    #Para problemas grandes, para ser mais r�pido >> Precondicionamento �
    # uma arte, uma ci�ncia e uma ind�stria.

# INTERPOLA��O - Importante!!

    # Interpola��o 1D (interp1d)
    # Interpola��o para dados multivari�veis (griddata)
        #'opengrid � menos caro computacionalmente'
        #'plot >> mostra curvas'
        #'imshow >> mostra matrizes'

    # Interpola��o por Spline (legais para se usar!)
        #'Ajuste por curvas polinomiais'

    #Representa��o por splines para 2D
        #'Ajuste de pontos em duas dimens�es'

    # Interpol��o por base radial

# TRANSFORMADAS DE FOURIER

    # TF 1D escalar
    # Tipo I
    # Tipo II
    # Convolu��o FFT

# PROCESSAMENTO DE SINAIS

    # B-Splines
    # Filtros (lineares e n�o-lineares)
    # Convolu��o e Correla��o
    # Filtros por equa��es de diferen�as
    # Outros filtros (Wiener, Hilbert, Order, Median)

# �LGEBRA LINEAR

    #'Otimiza-se com a compila��o das bibliotecas ATLAS LAPACK e BLAS'

    # Classe de Matrizes( comando mat, permite entrada como matlab )
    # Rotinas b�sicas
        #'Inversa: Matriz A >> A.I'
        #'Resolvendo sistemas lineares >> sp.linalg.solve(A,b)'
        #'Determinante >> sp.linalg.det(A)'
        #'C�lculo de normas >> sp.linalg.norm()'
        #'Resolvendo problemas de m�nimos quadrados (linear) e pseudo-inversas'
        #'Inversa Generalizada >>'
        #'Autovalor e autovetor >> lambda , v = sp.linalg.eig(A)'
        #'Decomposi��o de valor singular (autovetor e valor para matrizes � nxn)'
        #'Decomposi��o LU >> sp.linalg.lu_solve(A)'
        #'Decomposi��o de Cholesky >> sp.linalg.cho_solve(A) '
        #'Decomposi��o QR'
        #'Decomposi��o de Schur'

    # Fun��es Matriciais
