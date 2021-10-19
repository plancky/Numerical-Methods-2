import numpy as np
def put(x,i,v):
    np.put(x,i,v)
    return(x)

def rk4(i,x,f,h):
    x_i,t = x[i],x[0] 
    m1 = f[i-1](*x)
    m2 = f[i-1](*put(x,[0,i],[t+h/2,x_i+h/2*m1]))
    m3 = f[i-1](*put(x,[0,i],[t+h/2,x_i+h/2*m2]))
    m4 = f[i-1](*put(x,[0,i],[t+h,x_i+h*m3]))
    avg_m = ( m1 + 2*(m2+m3) + m4 )/6
    return(x_i + h*avg_m)

def rk2(i,x,f,h):
    return(x[i] + (f[i-1](*x) + f[i-1](*put(x,[0,i],[x[0]+h,x[i] + h*f[i-1](*x)])
    ))/2*h)

def em(i,x,f,h):
    return(x[i] + f[i-1](*put(x,[0,i],[x[0]+h/2,x[i] + (h/2)*f[i-1](*x)]))*h)

def ef(i,x,f,h):
    return(x[i] + h* f[i-1](*x))

def ode_solver(f,t_axis,ini,Nh,n,method=rk4):
    N,h = Nh
    data = np.zeros((N+2,n))
    data[:,0],data[0] = t_axis, ini
    params =  np.arange(1,n)
    iter = np.vectorize(method, excluded=[1,2,3]) 
    for j in range(N+1) :
        data[j+1,1:] = iter(params,data[j],f,h)
    return(data)

class set_problem:
    def __init__(self,f,dom,ini,N):
        self.n = len(ini) 
        if self.n-1 != len(f) :
            raise ValueError("unequal equations and parameters") 
        self.dom = np.linspace(*dom,N+2)
        self.ini = ini
        self.f =f
        self.ivp = (self.f,self.dom,self.ini,(N,self.dom[1] - self.dom[0]),self.n)
        self.dat = dict()
    def rk4(self):
        self.data_rk4 = ode_solver(*self.ivp,method=rk4)
        self.dat["rk4"] = self.data_rk4
        return(self.data_rk4)
    def rk2(self):
        self.data_rk2 = ode_solver(*self.ivp,method=rk2)
        self.dat["rk2"] = self.data_rk2
        return(self.data_rk2)
    def em(self):
        self.data_em = ode_solver(*self.ivp,method=em)
        self.dat["em"] = self.data_em
        return(self.data_em)
    def ef(self):
        self.data_ef = ode_solver(*self.ivp,method=ef)
        self.dat["ef"] = self.data_ef
        return(self.data_ef)
    def jt_plot(self,ax,j):
        for i in self.dat:
            ax.plot(self.dom,self.dat[i][:,j],"-1",label=i)
    def kj_plot(self,ax,j,k):
        for i in self.dat:
            ax.plot(self.dat[i][:,j],self.dat[i][:,k],"-p",label=i)

if __name__ == "__main__" : 
    import matplotlib.pyplot as plt
    plt.style.use("bmh")
    ivp = set_problem([lambda t,x,y : x + y -x**3 , lambda t,x,y : -x ],
                     (0.1,15),
                     (0,0,-1),N =500)
    data_rk4,data_rk2,data_em,data_ef = ivp.rk4(),ivp.rk2(),ivp.ef(),ivp.em() 
    fig,(ax1,ax2) = plt.subplots(2,1)
    fig2,ax3 = plt.subplots(1,1)
    ivp.jt_plot(ax1,1)
    ivp.jt_plot(ax2,2)
    ivp.kj_plot(ax3,1,2)

    ax1.legend(),ax2.legend(),ax3.legend()
    plt.show()

