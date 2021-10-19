import numpy as np
import matplotlib.pyplot as plt
from coupled_euler import *
l,c1,c2 = 1.3,1.3,1.3
r=0
ivp = set_problem([lambda t,x,y,q1,q2,q3 : (q1/c1 - q2/c2 )/l,lambda t,x,y,q1,q2,q3 :(q2/c2 - q3/c1 )/l,
lambda t,x,y,q1,q2,q3 : -x ,lambda t,x,y,q1,q2,q3 : x+y,lambda t,x,y,q1,q2,q3 : y
],(0,50),(0,0,0,0,10,0),N=int(1e+3))
ivp.rk4()
fig,ax = plt.subplots(1,1)
ivp.jt_plot(ax,1)
ivp.jt_plot(ax,2)

plt.show()