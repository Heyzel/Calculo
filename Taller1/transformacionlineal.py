# -*- coding: utf-8 -*-
from matplotlib import pyplot as mt
import numpy as np
import scipy as s
import random


w = s.linspace(0,1,50)
n = 10000

A1 = [[0.85,0.04],[-0.04,0.85]]
A2 = [[0.20,0-0.26],[0.23,0.22]]
A3 = [[-0.15,0.28],[0.26,0.24]]
A4 = [[0,0],[0,0.16]]


b1 = np.array([0,1.6])
b2 = np.array([0,0.44])

x = [0.5,0.5]

xvalues = []
yvalues = []



def MatVecFila(A,x):
    C = []
    for i in range(len(A)):
        acum=0
        for j in range(len(A[i])):
            acum+=A[i][j]*x[j]
        C.append(acum)
    
    return(np.array(C))
    
def transformacion(n):
    for i in range(n):
        r  = random.uniform(0,1)
        if r<0.85:
            point = np.add(MatVecFila(A1,x),b1)
            xvalues.append(point[0])
            yvalues.append(point[1])
        elif r < 0.92:
            point = np.add (MatVecFila(A2,x),b2)
            xvalues.append(point[0])
            yvalues.append(point[1])
        elif r < 0.99:
            point = np.add (MatVecFila(A3,x),b2)
            xvalues.append(point[0])
            yvalues.append(point[1])
        elif r < 1 :
            point = MatVecFila(A4,x)
            xvalues.append(point[0])
            yvalues.append(point[1])
        
transformacion(n)
mt.scatter(xvalues,yvalues)
mt.scatter([0.5],[0.5])
mt.show()
