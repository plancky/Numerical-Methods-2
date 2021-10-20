import numpy as np
import matplotlib.pyplot as plt
from coupled_euler import *
import pandas as pd
import math
l,c1,c2 = 0.1,1,1.3
r=0
ivp = set_problem(f=[lambda t,x,y,q1,q2,q3 : (q1/c1 - q2/c2 -r*x)/l,lambda t,x,y,q1,q2,q3 :(q2/c2 - q3/c1 -r*y)/l,
lambda t,x,y,q1,q2,q3 : -x ,lambda t,x,y,q1,q2,q3 : -x-y,lambda t,x,y,q1,q2,q3 : y],
dom=(0,15),
ini=(0,10000,10000,1,0,-1),
N=int(20000))
d=ivp.rk4()
fig,ax = plt.subplots(1,1)
ivp.jt_plot(ax,1)
ivp.jt_plot(ax,2)
#ivp.kj_plot(ax,3,5)
#ivp.kj_plot(a,1,2)
plt.show()