import numpy as np 
import matplotlib.pyplot as plt
import scipy.integrate as integrate
from lib.printer import printer

def func(x):
    return(np.exp(x))

def trapezoidal(a,b,y=None,N=10,f=func):
    integral=0 
    x=np.linspace(a,b,N+1) 
    if y is None:
        y=f(x)
    y=np.array(y)
    l=len(y)
    if len(x)!=len(y):
        raise ValueError("length of x must be same as y")
    for i in range(len(x)):
        if i==0 or i==len(x)-1:
            integral+=y[i]
        else:
            integral+=2*y[i]
    integral*=(b-a)/(2*N)
    
    #Alternatively,
    '''
    y_1=y[:l-1:2]
    y_2=y[1:l:2]

    integral = (b-a)/(N*2) * (np.sum(y_1 + y_2))
    '''
    return(integral)

def simpson(a,b,y=None,N=10,f=func):
    integral=0
    x=np.linspace(a,b,N+1) 
    if y is None:
        y=f(x)
    y=np.array(y)
    l=len(y)
    if len(x)!=l:
        raise ValueError("length of x must be same as y")
    
    for i in range(len(x)):
        if i==0 or i==len(x)-1:
            integral+=y[i]
        elif i%2==0:
            integral+=2*y[i]
        else:
            integral+=4*y[i]

    integral*=(b-a)/(N*3)
    #Alternatively,
    '''
    y_1=y[:l-2:2]
    y_2=y[1:l-1:2]
    y_3=y[2:l:2]

    integral = (b-a)/(N*3) * (np.sum(y_1 + 4*y_2 + y_3))
    '''
    return(integral)

def integration(a,b,ni,function=None):
    trueval=integrate.quad(function,a,b)
    trapval=trapezoidal(a,b,N=ni,f=function)
    simpval=simpson(a,b,N=ni,f=function)

    #PRINTING 
    printer(np.array([
            ["Method used","Integral", "Error constant " ],
            ["Quad method scipy",trueval[0], trueval[1] ],
            ["Trapezoidal rule",trapval, trueval[1]-(trapval-trueval[0]) ],
            ["Simpson's rule",simpval, trueval[1]-(simpval-trueval[0]) ]
            ]))
            
    #PLOTTING CONVERGENCE GRAPH

    y_data_2,y_data,y_data_3=[],[],[]
    n_array=np.arange(40,370,2)
    h_array=(b-a)/n_array
    
    for n in n_array:
        x_data=np.linspace(a,b,n+1)
        y_data.append(trapezoidal(a,b,N=n,f=function))
        y_data_2.append(simpson(a,b,N=n,f=function))
        y_data_3.append(integrate.simpson(func(x_data),x_data))
    
    plt.xscale('log')
    plt.plot(h_array,y_data,label="Trapezoidal rule")
    plt.scatter(h_array,y_data,label="Trapezoidal rule")
    plt.plot(h_array,y_data_2,label="Simpson's rule")
    plt.scatter(h_array,y_data_2,label="Trapezoidal rule")
    plt.plot(h_array,y_data_3,linestyle='--',label="scipy's simpson implementation")
    plt.legend()


if __name__=="__main__":

    #n=int(input("Enter the number of sub-intervals : "))
    #a=int(input("Enter the lower-limit(a) : "))
    #b=int(input("Enter the upper-limit(b) : "))
    '''
    PART 3(a)
    '''
    V= [0,0.5,2.0,4.05,8,12.5,18,24.5,32,40.5,50]
    trapval=trapezoidal(0,1,y=V,N=10)
    simpval=simpson(0,1,y=V,N=10)

    printer(np.array([
        ["Trapezoidal rule",trapval],
        ["Simpson's rule",simpval]
    ]),column=False)

    '''
    PART 3(b)
    https://github.com/scipy/scipy/blob/v1.7.1/scipy/integrate/_quadrature.py#L433-L555
    '''
    integration(0,13,100,function=func)

    plt.show()
    