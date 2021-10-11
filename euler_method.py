import numpy as np

def ode_solver(f,d=(0,5),i=(0,0),N=7,method = "ef" ):
    if method not in ["ef","em","rk2","rk4"]:
        raise ValueError("Method not supported")
    a,b = d
    t0,x0 = i
    ii = np.linspace(a,b,N+2)
    h = np.diff(ii)[0]
    x = [x0]
    if method == "ef":
        for j in ii[1:]:
            x.append(j + f(j,x[-1])*h)
    elif method == "em":
        for j in ii[1:]:
            x.append(j + f(j+h/2,x[-1] + (h/2)*(f(j,x[-1])))*h)
    elif method == "rk2":
        for j in ii[1:]:
            x.append(j + (f(j,x[-1]) + f(j+1,x[-1] + h*f(j,x[-1])))/2*h)
    elif method== "rk4" :
        for j in ii[1:]:
            m1 = f(j,x[-1])
            m2 = f(j+h/2,x[-1] + h/2*m1)
            m3 = f(j+h/2,x[-1] + h/2*m2)
            m4 = f(j+h,x[-1] + h*m3)
            avg_slope = ( m1 +2*(m2 +m3) + m4 )/6
            x.append(j + avg_slope*h)
    return(x[-1],x,ii)

def pf(x):
    y = ["nodes","euler method(Forward)","euler method(Centered)", "rk2","rk4"]
    for mk in range(1,len(x)):
        plt.plot(x[0],x[mk],label=y[mk])

def forall(f,dom,ini):
    N=100
    return(np.array([np.linspace(dom[0],dom[1],N+2),ode_solver(f,dom,ini,N=N)[1],ode_solver(fx,dom,ini,N=N,method="em")[1],ode_solver(fx,dom,ini,N=N,method="rk2")[1],ode_solver(fx,dom,ini,N=N,method="rk4")[1]],dtype="double"))
    
if __name__ == '__main__':
    import matplotlib.pyplot as plt
    
    
    radx = lambda t,N : -N/4
    dom = (0,0.02)
    ini = (0,2e+4)
    print(len(ode_solver(radx,dom,ini,N=100)[1]))
    ta2 = forall(radx,dom,ini)
    pf(ta2)
    plt.yscale("log")
    
    plt.show()





    '''
    fx = lambda t,x : np.sin(x*t)
    
    t,x = np.linspace(0,1,20),np.linspace(0,1,20)
    T,X = np.meshgrid(t,x)
    f_i = 1/np.sqrt(1+f(T,X)**2)
    f_j = f(t,x)/np.sqrt(1+f(T,X)**2)
    plt.quiver(T,X,f_i,f_j)'''

