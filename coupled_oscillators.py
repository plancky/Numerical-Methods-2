import numpy as np
import matplotlib.pyplot as plt
from coupled_euler import *
import pandas as pd
import math

#l stands for inductance L , c1, c2 corresponds to C and C' 
l,c1,c2 = 0.1,1,1.3
#resistance
r=0
ivp = set_problem(
    f=[lambda t,x,y,q1,q2,q3 : (q1/c1 - q2/c2 -r*x)/l, #Function associated with (1)
    lambda t,x,y,q1,q2,q3 :(q2/c2 - q3/c1 -r*y)/l, #Function associated with (2)
    lambda t,x,y,q1,q2,q3 : -x , #Function associated with dq1/dt
    lambda t,x,y,q1,q2,q3 : -x-y, #Function associated with dq2/dt
    lambda t,x,y,q1,q2,q3 : y], #Function associated with dq3/dt
    dom=(0,15), # Time Domain 
    ini=(0,10000,10000,1,0,-1), #initial conditions in ordered tuple(t,I_a,I_b,q1,q2,q3)
    N=int(20000),# No. of nodes/ control step size
    vars = ("t","$I_a$","$I_b$","q1","q2","q3") # var names for labels
    )

d=ivp.rk4() # rk4 called to solve the ivp problem
fig,ax = plt.subplots(1,1) 
ivp.jt_plot(ax,1) # plots I_a vs t on ax
ivp.jt_plot(ax,2) # plots I_b vs t on ax

#ivp.jt_plot(ax,3) # plots q1 vs t
#ivp.jt_plot(ax,5) # plots q3 vs t
#ivp.kj_plot(ax,3,5) # plots q3 vs q1
#ivp.kj_plot(ax,1,2) # plots I_b vs I_a on ax
plt.legend()
plt.show()