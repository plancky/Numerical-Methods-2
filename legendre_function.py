import numpy as np 
import matplotlib.pyplot as plt
from scipy.special import eval_legendre,legendre

def g(x):
    if x%1!=0 or x<0:
        raise ValueError("Input should be a positive integer.{0}".format(x))
    if x>=1:
        return(x*g(x-1))
    else:
        return(1)        

def mylegendre(x,n=0,d=0):
    if n%2==0:
        m=n/2
    else:
        m=(n-1)/2
    def term(k):
        if n-2*k-d>=0:
            return(((-1)**k*g(2*n-2*k)*g(n-2*k)/(2**n*g(k)*g(n-k)*g(n-2*k)*g(n-2*k-d)))*x**(n-2*k-d))
        else:
            return(0)
    t=np.vectorize(term)
    i= np.arange(0,m+1,1,dtype="int")
    return(np.sum(t(i)))

if __name__=="__main__":
    #t=posint_gamma(0)
    print(mylegendre(1,7))
    print(legendre(7))
    x_data=np.linspace(-0.9,0.9,100)
    leg=np.vectorize(mylegendre,excluded=[1,2])
    data= np.array([x_data,leg(x=x_data,n=0),leg(x=x_data,n=1),leg(x=x_data,n=2)])
    '''
    with open("leg00.dat",'wr') as f:
        f.write()
    #print(t)
    '''