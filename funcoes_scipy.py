# -*- coding: cp1252 -*-
import numpy as np
import scipy as sp
#import pylab as pl

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

#Fatorial
f = sp.factorial(100)
print f
f = sp.factorial(100, exact = 1)
print f

#Calcula combinações entre elementos
print sp.comb(10,4,exact = 1) #10 elementos combinados 4 a 4

#Gerador de números aleatórios
print sp.rand(2,4,3) #array de números aleatórios
print sp.randn(2,4,3) #array de números aleatórios distribuídos normalmente

#Integração numérica >> sp.integrate()

#Equação diferencial ordinária ( odeint ) dy/dt = f(y,t)

#Otimização (optimize) \\ melhor é o pacote openopt.org //
'Função de Rosenbrock usado para testes de otimização'

#Ajuste por mínimos quadrados (leastsq) - importante!!!

#Minimizadores de funções escalares

'Computação Científica é: otimização, integração, interpolação, quadrantura'

# Determinação de raízes 

    #fsolve é basicamente Newton-Raphson
    #método do ponto fixo
    #Grandes problemas - não utilize fsolve, Newton-Raphson. Use Krylov, ..

	#Função np.mgrid >> produz grade em espaço 3D'
    #pl.colorbar >> produz barra de níveis'

    #Para problemas grandes, para ser mais rápido >> Precondicionamento é
    # uma arte, uma ciência e uma indústria.

# INTERPOLAÇÂO - Importante!!

    # Interpolação 1D (interp1d)
    # Interpolação para dados multivariáveis (griddata)
        #'opengrid é menos caro computacionalmente'
        #'plot >> mostra curvas'
        #'imshow >> mostra matrizes'

    # Interpolação por Spline (legais para se usar!)
        #'Ajuste por curvas polinomiais'

    #Representação por splines para 2D
        #'Ajuste de pontos em duas dimensões'

    # Interpolção por base radial

# TRANSFORMADAS DE FOURIER

    # TF 1D escalar
    # Tipo I
    # Tipo II
    # Convolução FFT

# PROCESSAMENTO DE SINAIS

    # B-Splines
    # Filtros (lineares e não-lineares)
    # Convolução e Correlação
    # Filtros por equações de diferenças
    # Outros filtros (Wiener, Hilbert, Order, Median)

# ÁLGEBRA LINEAR

    #'Otimiza-se com a compilação das bibliotecas ATLAS LAPACK e BLAS'

    # Classe de Matrizes( comando mat, permite entrada como matlab )
    # Rotinas básicas
        #'Inversa: Matriz A >> A.I'
        #'Resolvendo sistemas lineares >> sp.linalg.solve(A,b)'
        #'Determinante >> sp.linalg.det(A)'
        #'Cálculo de normas >> sp.linalg.norm()'
        #'Resolvendo problemas de mínimos quadrados (linear) e pseudo-inversas'
        #'Inversa Generalizada >>'
        #'Autovalor e autovetor >> lambda , v = sp.linalg.eig(A)'
        #'Decomposição de valor singular (autovetor e valor para matrizes ñ nxn)'
        #'Decomposição LU >> sp.linalg.lu_solve(A)'
        #'Decomposição de Cholesky >> sp.linalg.cho_solve(A) '
        #'Decomposição QR'
        #'Decomposição de Schur'

    # Funções Matriciais
