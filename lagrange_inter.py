#from numba import jit
import seaborn as sns
from numpy.core.function_base import linspace
from legendre_function import setaxis
import numpy as np
import matplotlib.pyplot as plt

#@jit(nopython=True)
def L(x,xi,n,i):
    ''' 
    s=1
    for k in range(0,n+1):
        if i!=k:
            s*= (x - xi[k])/(xi[i] - xi[k])
    return(s)
    Alternatively
    '''    
    return (np.product([(x - xi[k])/(xi[i] - xi[k]) for k in range(0,n+1) if i!=k ]))

Li = np.vectorize(L,excluded =[0,1])
    
def interpolate(x,y):
    if len(x)!=len(y):
        raise ValueError("Input arrays must be of Equal length")
    n = len(x)-1
    ii = np.arange(0,n+1,1)
    return(np.vectorize(lambda  a : Li(a,x,n,i=ii).dot(y)))

def inverse_interpolate(y,x):
    if len(x)!=len(y):
        raise ValueError("Input arrays must be of Equal length")
    n = len(x)-1
    ii = np.arange(0,n+1,1)
    return(np.vectorize(lambda  a : Li(a,x,n,i=ii).dot(y)))

if __name__ == "__main__":
    plt.style.use("seaborn-dark-palette")
    dataset = [[0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0],
            [1.0, 0.99, 0.96, 0.91, 0.85, 0.76, 0.67, 0.57, 0.46, 0.34, 0.22, 0.11, 0.0, -0.1, -0.18, -0.26],
            [2.81,3.24,3.80,4.30,4.37,5.29,6.03],
            [0.5,1.2,2.1,2.9,3.6,4.5,5.7] ]
    xdata= [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0]
    ydata= [1.0, 0.99, 0.96, 0.91, 0.85, 0.76, 0.67, 0.57, 0.46, 0.34, 0.22, 0.11, 0.0, -0.1, -0.18, -0.26]
    V = [2.81,3.24,3.80,4.30,4.37,5.29,6.03]
    I = [0.5,1.2,2.1,2.9,3.6,4.5,5.7]
    
    #Plotting
    fig1, (ax11, ax12) = plt.subplots(1, 2)
    x_space1 =np.linspace(0,3,100)
    y_space1 =np.linspace(1,-0.26)
    bessel,bessel_1 = interpolate(xdata,ydata),inverse_interpolate(xdata,ydata)
    ax11.scatter(xdata,ydata),ax11.plot(x_space1,bessel(x_space1))
    ax12.scatter(ydata,xdata),ax12.plot(y_space1,bessel_1(y_space1))
    ax11.set_xlabel("$x$"),ax11.set_ylabel("$J_0(x)$")
    ax12.set_xlabel("$J_0(x)$"),ax12.set_ylabel("$x$")
    setaxis(ax11, "interpolate"), setaxis(ax12, "inverse interpolation")
    fig1.suptitle("Bessel Function", size=16)
    #########  new plot
    fig2, (ax21, ax22) = plt.subplots(1, 2)
    volt,volt_1 = interpolate(I,V),inverse_interpolate(I,V)
    x_space2,y_space2 =np.linspace(0.49,5.7,100),np.linspace(2.81,6.03,100)
    ax21.scatter(I,V,label="dataset"),ax22.scatter(V,I,label="dataset")
    ax21.plot(x_space2,volt(x_space2)) ,ax22.plot(y_space2,volt_1(y_space2)) 
    plt.legend()
    ax21.grid(),ax22.grid()
    fig2.suptitle("Photodetector Volatge vs intensity", size=16)
    plt.show()
    fig2.show()
    










'''

def lbf(x1,y1):
    if len(x1) != len(y1):
        raise ValueError("length of x and y must be the same. ")
    n = len(x1)-1
    x= symbols('x')
    i,k = symbols('i k')
    yi = IndexedBase('y')
    yi = Array(y1)
    xi = Array(x1)
    #xi = IndexedBase('xi')
    Lip = Sum(Product((x-xi[k])/(xi[i] - xi[k]),(k,0,n))*yi[i],(i,0,n))
    f = lambdify(x,Lip,"numpy")
    return f
'''