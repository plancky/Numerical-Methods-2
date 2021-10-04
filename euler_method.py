import numpy as np

def euler_method(f,d=(0,5),i=(0,0),N=7):
    a,b = d
    t0,x0 = i
    h = (b - a)/(N+1)
    ii = np.linspace(a,b,N+2)
    newlist = []
    x = i[1]
    for j in ii:
        x+= j + f(j,x)*h
        newlist.append(x)
    return(x,newlist,ii)


def midpoint_euler(f,d=(0,5),i=(0,0),N=7):
    a,b = d
    t0,x0 = i
    h = (b - a)/(N+1)
    ii = np.linspace(a,b,N+2)
    newlist = []
    xi = t0
    for j in ii:
        xi+= j + f(j+h/2,xi + (h/2)*(f(j,xi)))*h
        newlist.append(xi)
    return(xi,newlist,ii)


def rk2(f,d=(0,5),i=(0,0),N=7):
    a,b = d
    t0,x0 = i
    h = (b - a)/(N+1)
    ii = np.linspace(a,b,N+2)
    newlist = []
    xi = t0
    for j in ii:
        avg_slope = (f(j,xi) + f(j+1,xi + h*f(j,xi)))/2
        xi += j + avg_slope*h
        newlist.append(xi)
    return(xi,newlist,ii)


def rk4(f,d=(0,5),i=(0,0),N=7):
    a,b = d
    t0,x0 = i
    h = (b - a)/(N+1)
    ii = np.linspace(a,b,N+2)
    xi = a
    newlist = []
    for j in ii:
        m1 = f(j,xi)
        m2 = f(j+h/2,xi + h/2*m1)
        m3 = f(j+h/2,xi + h/2*m2)
        m4 = f(j+h,xi + h*m3)
        avg_slope = ( m1 +2*(m2 +m3) + m4 )/2
        xi += j + avg_slope*h
        newlist.append(xi)
    return(xi,newlist,ii)

def pf(x):
    y = ["nodes","euler method(Forward)","euler method(Centered)", "rk2","rk4"]
    for mk in range(1,len(x)):
        plt.plot(x[0],x[mk],label=y[mk])

def forall(f,dom,ini):
    N=100
    return(np.array([np.linspace(dom[0],dom[1],N+2),euler_method(f,dom,ini,N=N)[1],midpoint_euler(fx,dom,ini,N=N)[1],rk2(fx,dom,ini,N=N)[1],rk4(fx,dom,ini,N=N)[1]],dtype=float))
    
if __name__ == '__main__':
    import matplotlib.pyplot as plt
    fx = lambda t,x : np.sin(x*t)
    
    '''
    t,x = np.linspace(0,1,20),np.linspace(0,1,20)
    T,X = np.meshgrid(t,x)
    f_i = 1/np.sqrt(1+f(T,X)**2)
    f_j = f(t,x)/np.sqrt(1+f(T,X)**2)
    plt.quiver(T,X,f_i,f_j)'''
    
    radx = lambda t,N : -N/4
    dom = (0,5)
    ini = (0,2e+4)
    ta2 = forall(radx,dom,ini)    
    pf(ta2)
    
    plt.show()

