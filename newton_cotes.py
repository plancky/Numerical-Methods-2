import numpy as np 
import matplotlib.pyplot as plt
import scipy.integrate as integrate

def func(x):
    return(np.exp(x))

def trapezoidal(a,b,y=-1,N=10,f=func):
    integral=0 
    x=np.linspace(a,b,N+1) 
    if y==-1:
        y=f(x)
    
    if len(x)!=len(y):
        return("Error")
    for i in range(len(x)):
        if i==0 or i==len(x)-1:
            integral+=y[i]
        else:
            integral+=2*y[i]
    h=(b-a)/N
    return((h/2)*integral)

def simpson(a,b,y=-1,N=10,f=func):
    integral=0
    x=np.linspace(a,b,N+1) 
    if y==-1:
        y=f(x)
    
    if len(x)!=len(y):
        return("Error")
    for i in range(len(x)):
        if i==0 or i==len(x)-1:
            integral+=y[i]
        elif i%2==0:
            integral+=2*y[i]
        else:
            integral+=4*y[i]
    h=(b-a)/N
    return((h/3)*integral)

def integration(function,a,b,ni):
    y_data_2,y_data,y_data_3=[],[],[]
    n_array=np.arange(10,41)

    for n in n_array:
        x_data=np.linspace(a,b,n+1)
        y_data.append(trapezoidal(a,b,N=n,f=function))
        y_data_2.append(simpson(a,b,N=n,f=function))
        y_data_3.append(integrate.simpson(func(x_data),x_data))
    
    trueval=integrate.quad(function,a,b)
    trapval=trapezoidal(a,b,N=ni,f=function)
    simpval=simpson(a,b,N=ni,f=function)
    print("{0:{fill}<66}".format('',fill='-'))
    print("|{:<20}|".format("Quad method scipy"),"{0:^16} |{1:>23}|".format(trueval[0], trueval[1] ))
    print("|{:<20}|".format("Trapezoidal rule"),"{0:^16} |{1:>23}|".format(trapval, trapval- trueval[0] ))
    print("|{:<20}|".format("Simpson's rule"),"{0:^16} |{1:>23}|".format(simpval, simpval-trueval[0]))
    print("{0:{fill}<66}".format('',fill='-'))
    plt.plot(10/n_array,y_data,label="Trapezoidal rule")
    plt.plot(10/n_array,y_data_2,label="Simpson's rule")
    plt.plot(10/n_array,y_data_3,label="scipy's simpson implementation")
    plt.legend()


if __name__=="__main__":
    #n=int(input("Enter the number of sub-interval's : "))
    #a=int(input("Enter the lower-limit(a) : "))
    #b=int(input("Enter the upper-limit(b) : "))
    '''
    PART 3(a)
    '''
    V= [0,0.5,2.0,4.05,8,12.5,18,24.5,32,40.5,50]
    trapval=trapezoidal(0,1,y=V,N=10)
    simpval=simpson(0,1,y=V,N=10)
    print("{0:{fill}<40}".format('-',fill='-'))
    print("|{:<20}|".format("Trapezoidal rule"),"{0:>16.6f} |".format(trapval))
    print("|{:<20}|".format("Simpson's rule"),"{0:>16.6f} |".format(simpval))
    print("{0:{fill}<40}".format('',fill='-'))

    '''
    PART 3(b)
    integration(func,3,13,100)

    plt.show()
    '''