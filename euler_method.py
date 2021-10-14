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
            x.append(x[-1] + f(j,x[-1])*h)
    elif method == "em":
        for j in ii[1:]:
            x.append(x[-1] + f(j+h/2,x[-1] + (h/2)*(f(j,x[-1])))*h)
    elif method == "rk2":
        for j in ii[1:]:
            x.append(x[-1] + (f(j,x[-1]) + f(j+1,x[-1] + h*f(j,x[-1])))/2*h)
    elif method== "rk4" :
        for j in ii[1:]:
            m1 = f(j,x[-1])
            m2 = f(j+h/2,x[-1] + h/2*m1)
            m3 =f(j+h/2,x[-1] + h/2*m2)
            m4 = f(j+h,x[-1] + h*m3)
            avg_slope = ( m1 +2*(m2 +m3) + m4 )/6
            x.append(x[-1] + avg_slope*h)
    return(x[-1],np.array(x),ii)

def forall(f,g,dom,ini,d,N=100,yd=1):
    nodes = np.linspace(dom[0],dom[1],N+2)
    analytic = g(nodes)/yd
    return(pd.DataFrame(np.array([nodes/d,ode_solver(f,dom,ini,N=N)[1]/yd,ode_solver(f,dom,ini,N=N,method="em")[1]/yd,ode_solver(f,dom,ini,N=N,method="rk2")[1]/yd,ode_solver(f,dom,ini,N=N,method="rk4")[1]/yd,analytic],dtype="double").T, columns=["nodes","euler_forward","euler_centered", "rk2","rk4","analytic"]))

def error_forall(y):
    x = pd.DataFrame(y)
    x["euler_forward"] =abs(x["euler_forward"] - x["analytic"] )
    x["euler_centered"] =abs(x["euler_centered"] - x["analytic"] )
    x["rk2"] =abs(x["rk2"] - x["analytic"] )
    x["rk4"] =abs(x["rk4"] - x["analytic"] )
    x=x.drop(columns=["analytic"])
    return(x)

def melt(x):
    return(x.melt('nodes', var_name='methods', value_name='vals'))

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import seaborn as sns
    import pandas as pd 
    sns.set_style("darkgrid")
    fig1,axes1= plt.subplots(1,2,figsize=(20,12))
    fig2,axes2= plt.subplots(1,2,figsize=(20,12))
    fig3,axes3= plt.subplots(1,2,figsize=(20,12))
    #Problem 1
    halflife = 4
    lamda =  (np.log(2)/halflife) 
    ta1 = forall(lambda t,N : -N * lamda,lambda t : 2e+4*np.exp(-lamda*t),(0,5*halflife),(0,2e+4),d=halflife,yd=2e+4)
    #ax1 = sns.relplot(data=melt(ta1),x="nodes",y="vals",hue="methods",kind="line")
    ax1 = sns.lineplot(data=melt(ta1),x="nodes",y="vals",hue="methods",ax=axes1[0])
    ax1.set(xlabel='$t / t_{1/2}$', ylabel='$N/N_0$')
    ax11 = sns.lineplot(data=melt(error_forall(ta1)),x="nodes",y="vals",hue="methods",ax=axes1[1])
    ax11.set(xlabel='$t / t_{1/2}$', ylabel='$N/N_0$'),ax11.set_title("Error graph")
    fig1.suptitle("Radioactivity Q1")
    fig1.savefig("./euler_data/radioactivity.png")

    #Problem 2 
    tc = 1e+3*1e-6 
    ta2 = forall(lambda t,v : -v/tc,lambda t : 10*np.exp(-t/tc),(0,5*tc),(0,10),d=tc,yd=10)
    ax2 = sns.lineplot(data=melt(ta2),x="nodes",y="vals",hue="methods",ax=axes2[0])
    ax2.set(xlabel='$t/RC$', ylabel='$V/V_0$')
    ax21 = sns.lineplot(data=melt(error_forall(ta2)),x="nodes",y="vals",hue="methods",ax=axes2[1])
    ax21.set(xlabel='$t/RC$', ylabel='$V/V_0$'),ax21.set_title("Error graph")
    fig2.suptitle("Capacitor Discharge Q2")
    fig2.savefig("./euler_data/capacitor.png")
    #Problem 3 
    tau = 20 / (6*np.pi*100*5)
    ta3 = forall(lambda t,v : -v/tau,lambda t : 100*np.exp(-t/tau),(0,5*tau),(0,100),d=1,yd=1)
    ax3 = sns.lineplot(data=melt(ta3),x="nodes",y="vals",hue="methods",ax=axes3[0])
    ax3.set(xlabel='$t$', ylabel='$v$')
    ax31 = sns.lineplot(data=melt(error_forall(ta3)),x="nodes",y="vals",hue="methods",ax=axes3[1])
    ax31.set(xlabel='$t$', ylabel='$v$'),ax31.set_title("Error graph")
    fig3.suptitle("Stokes' Law Q3")

    fig3.savefig("./euler_data/stokes_law.png")



    '''
    fx = lambda t,x : np.sin(x*t)
    
    t,x = np.linspace(0,1,20),np.linspace(0,1,20)
    T,X = np.meshgrid(t,x)
    f_i = 1/np.sqrt(1+f(T,X)**2)
    f_j = f(t,x)/np.sqrt(1+f(T,X)**2)
    plt.quiver(T,X,f_i,f_j)'''

