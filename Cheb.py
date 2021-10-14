#import modules

import numpy as np
from sympy import *
import matplotlib.pyplot as plt
def cheb(a,b,N):
                     
    D = np.zeros((N+1,N+1))     # initialize (N+1) by (N+1) array filled with zeros 

    D[0][0] = -(2*N**2+1)/6
    D[N][N] = (2*N**2+1)/6
    D[N][0] = 0.5*(-1)**N
    D[0][N] = -0.5*(-1)**N

    x = np.zeros(N+1)


    for i in range(N+1):  
        x[i] = 0.5*(a+b) + 0.5*(a - b)*np.cos(np.pi*i/(N))
   

    #diagonal
    for i in range(1,N):
        D[i,i] = -x[i]/(2*(1-x[i]**2))

    #off-diagonal
    for i in range(1,N):
            for j in range(1,N):
                if i == j:
                    continue
                D[i,j] = (-1)**(i+j)/(x[i] - x[j]) 
            
    #right  column            
    for i in range(1,N):
        D[i,N] = 0.5*(-1)**(i+N)/(x[i] - x[N])
    #left column    
    for i in range(1,N):
        D[i,0] = 0.5*(-1)**(i)/(x[i] - x[0])   

    #bottom row    
    for j in range(1,N):
        D[N,j] = 2*(-1)**(j+N)/(x[N] - x[j])

    #top row    
    for j in range(1,N):
        D[0,j] = 2*(-1)**(j)/(x[0] - x[j])

    return x,D
