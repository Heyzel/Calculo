# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt   
import numpy as np
import scipy as s

r = 1/2
n = 123456789
unitcircle = plt.Circle((0,0),r,color='b',fill=False)

plt.rcParams.update({'figure.figsize': [8,6],'font.size': 18, 'font.family': 'serif'})

fig = plt.figure()
ax = plt.subplot(aspect='equal')
ax.add_artist(unitcircle)

pi_aproximations = []



def poligon(n):
    
    coseno = lambda n,k : r * (s.cos(((2*np.pi)*(k))/n))
    seno = lambda n,k : r * (s.sin(((2*np.pi)*(k))/n))
    xvalues = []
    yvalues = []

    for i in range(n+1):
        xvalues.append(coseno(n,i))
        yvalues.append(seno(n,i))
       #ax.plot(xvalues,yvalues, 'r')
        
    
    x = (xvalues[1]-xvalues[0])**2
    y = (yvalues[1] - yvalues[0])**2
        
    L = 0
    L = (n)*np.sqrt(x + y)
    pi_aproximations.append(L)

for i in range(4,n+1):
    poligon(i)
result = list(map(lambda y: np.abs(np.pi-y), pi_aproximations))


fig1, ax1 = plt.subplots(figsize = (10,4))
ax1.semilogy(result, 'r', label='$|\pi - error|$')
ax1.set_xlabel('$ \#\quadde\quad lados \quad del \quad poligono$')
ax1.set_ylabel('error')

ax1.legend(loc=0)