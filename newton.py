# -*- coding: cp1252 -*-
import numpy as np
import pylab as pl
from numpy.linalg import solve

#Defini��o da fun��o que resolve sistema de equa��es
def newtonRaphsonMod(fun, x0 , xtol=1e-8 , itermax=200 , jacob=None):

    #Define-se tol., erro, chute inicial e contador para entrar no loop DO-WHILE
    erro = 2 * xtol
    x    = np.asarray(x0) # Se x0 n�o for array, transforma em array
    ite = 0
    F = fun(x)

    #La�o
    while (erro > xtol) and (ite < itermax):       
        print '***'
        if jacob is None: #C�lculo num�rico do Jacobiano
            linhas = colunas = len(x)
            J = np.zeros((linhas,colunas))
            y = x.copy()        
            for j in range(colunas):                
                y[j] = x[j]*(1 + xtol)
                J[:,j] = (fun(y)-fun(x))/(x[j]*xtol)
                        




            
        else:
            J = jacob(x)

        dx = solve(J,-F) # resolu��o de um sistema linear xn + f(x)/f'(x) = xn+1
                         # onde dx =(xn+1) - (xn) , J = f'(x) e F = f(x)
                         # ou J*dx = J*[(xn+1) - (xn)] = F, i.e., J * dx - F = 0
                         # isto �, um sistema linear Ax + B = 0

	# Aqui � implementada a parte robusta do m�todo, n�o permitindo dx > x
        # isso � feito dividindo o incremento dx de modo que o novo x seja > 0    
##        for j in range(len(x)):
##            while (x[j] + dx[j]) < 0.: # novo x n�o pode ser negativo
##                dx[j] *= .5
        
        'Elimina-se o loop de FOR pois ele � muito custoso computacionalmente'
        while len(dx[x+dx<0]) != 0:
            dx[x+dx<0] *= 0.5
                 
        ite += 1 # contando..
        x += dx  # incrementa-se os valores de xn para virar xn+1

        F = fun(x) # atualiza-se o xn

        erro = max(np.sqrt(np.dot(F,F)) , abs(F).max())

        if ite == itermax:
            print "N�o convergiu com %s itera��es!" %ite
        
    return x, ite, F

if __name__ == '__main__':

    import time
    x0 = .005 , .005 , .005 # Chute inicial

    #Defini-se uma fun��o fun() que representa o sistema de equa��es n�o-lineares
    def fun(x): #x � um vetor
        x1,x2,x3 = x # desempacotando o vetor
        return np.array((
            x1**2 - np.sin(2.*x2) - 0.3*np.log(x3) - 1.42721880871 ,
            x2**3 + np.cos(2.*x1) +   x3**(-1./2)  - 8.16120343264 ,
            0.5*x1**(2./3) + x2**(2./7) - np.cos(x3) - 2.70900961508
                       )) # d�o os restos, que deve ser aproximadamente zero!

    #Defini��o da fun��o que calcula o jacobiano do sistema de equa��es 
    def jacob(x):
        x1, x2, x3 = x
        return np.array(( 
            [  2.*x1            , -2*np.cos(2.*x2)  , -.3/x3             ],
            [  -2*np.sin(2*x1)  , 3.*x2**2           , -1./2*x3**(-3./2) ],
            [  1./3*x1**(-1./3) , 2./7*x2**(5./7)   , np.sin(x3)         ]
                        )) # Matriz do Jacobiano

    start = time.time() # mede um tempo
    x, ite, res = newtonRaphsonMod(fun,x0,xtol=1e-8,jacob = None)
    stop = time.time() # mede outro tempo final
    
    print "Ra�zes: %s  \nItera��es: %s  \nRestos: %s \nTempo: %.4fs"%(x, ite, res, stop-start)
    
    x = np.arange(-1000,1000)
    pl.plot(x, x**2 - np.sin(2.*x) - 0.3*np.log(x) - 1.42721880871 )
    #pl.show()
