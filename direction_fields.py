import matplotlib.pyplot as plt
import numpy as np

plt.style.use("dark_background")
f = lambda t,x : np.sin(x*t)

t,x = np.linspace(-5,5,10),np.linspace(-5,5,10)
T,X = np.meshgrid(t,x)
f_i = 1/np.sqrt(1+f(T,X)**2)
f_j = f(t,x)/np.sqrt(1+f(T,X)**2)
fig,ax = plt.subplots(1,1,figsize=(5,5))
plt.quiver(T,X,T/(T**2+X**2+1),X/(T**2+X**2+1),color = "#f23333")
plt.savefig("/home/planck/Home2.png")
plt.show()