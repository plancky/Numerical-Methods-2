import numpy as np 
import matplotlib.pyplot as plt
from lib.printer import printer

def g(x):
    if x%1!=0 or x<0:
        raise ValueError("Input should be a positive integer.{0}".format(x))
    if x>1:
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

def setaxis(ax,title=''):
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.legend(loc="lower right")
    ax.set_title(title)
    ax.grid()

def verify_recur1(x,n,pnx,pnx1,pn1x1):
    if np.allclose(n*pnx,pnx1*x - pn1x1):
        print("Hence, Verified ")
        np.savetxt('leg02.dat',np.array([x,np.ones(x.shape)*n,np.ones(x.shape)*(n-1),pnx,pnx1,pn1x1],dtype=float).T,delimiter=',',fmt='%.12e')
    else:
        print("Relation1 not satisfied")

def verify_recur2(x,n,pnx,pn1x,pn_1x):
    if np.allclose((2*n+1)*pnx*x,(n+1)*pn1x + n*pn_1x):
        print("Hence, Verified ")
        np.savetxt('leg_data/leg03.dat',np.array([x,np.ones(x.shape)*n,np.ones(x.shape)*(n-1),pnx,pn_1x,pn1x],dtype=float).T,delimiter=',',fmt='%.12e')
    else:
        print("Relation2 not satisfied")

def verify_recur3(x,n,pnx,pn_1x,pn_2x):
    if np.allclose(n*pnx,(2*n-1)*x*pn_1x - (n-1)*pn_2x):
        print("Hence, Verified ")
        np.savetxt('leg_data/leg04.dat',np.array([x,np.ones(x.shape)*n,np.ones(x.shape)*(n-1),pnx,pn_1x,pn_2x],dtype=float).T,delimiter=',',fmt='%.12e')
    else:
        print("Relation3 not satisfied")

if __name__=="__main__":
    '''
    from scipy.special import eval_legendre,legendre
    plt.style.use('seaborn-dark-palette')
    x_data=np.linspace(-0.9,0.9,100)
    leg=np.vectorize(mylegendre,excluded=[1,2])
    data= np.array([x_data,leg(x=x_data,n=0),leg(x=x_data,n=1),leg(x=x_data,n=2),leg(x=x_data,n=3)],dtype="double")
    data1= np.array([x_data,leg(x=x_data,n=0,d=1),leg(x=x_data,n=1,d=1),leg(x=x_data,n=2,d=1),leg(x=x_data,n=3,d=1)],dtype="double")
    #data= np.array([x_data,eval_legendre(0,x_data),eval_legendre(1,x_data),eval_legendre(2,x_data)],dtype="longdouble")
    
    np.savetxt('leg_data/leg00.dat',data.T,delimiter=',',fmt='%.12e')
    np.savetxt('leg_data/leg01.dat',data1.T,delimiter=',',fmt='%.12e')
    '''

    ldata=np.loadtxt('leg_data/leg00.dat',delimiter=',',dtype='double').T
    ldata1=np.loadtxt('leg_data/leg01.dat',delimiter=',',dtype='double').T
    

    '''
    fig,(ax1,ax2) = plt.subplots(1,2)
    for i in range(1,4):
        ax1.plot(ldata[0],ldata[i],label="$P_{0}$".format(i-1))    
    for i in [1,3]:
        ax2.plot(ldata1[0],ldata1[i],label="$P'_{0}$".format(i-1))
    ax2.plot(ldata[0],ldata[2],label="$P_1$")
    setaxis(ax1,'(a)'),setaxis(ax2,"(b)")
    fig.suptitle("Legendre series", size=16)
    '''
    verify_recur1(ldata[0],2,ldata[3],ldata1[3],ldata1[2]) 
    verify_recur2(ldata[0],2,ldata[3],ldata[4],ldata[2])
    verify_recur3(ldata[0],3,ldata[4],ldata[3],ldata[2])

    mat = np.ones((4,4))
    mat2 = np.identity(4)

    for i in range(4):
        for j in range(4):
            mat[i][j]=np.sum(ldata[i+1]*ldata[j+1]*np.diff(ldata[0])[0])
            mat2[i][j]*=2/(2*j+1)
    printer(mat,column=False)
    printer(mat2,column=False)
    

    plt.show()
    