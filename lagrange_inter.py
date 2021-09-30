import numpy as np

Li = lambda x,xi,n,i : np.product([(x - xi[k])/(xi[i] - xi[k]) for k in range(0,n+1) if i!=k ])
Liv = np.vectorize(Li,excluded =[0,1,2])

def interpolate(x,y,inv=False):
    if inv:
        x,y=y,x
    if len(x)!=len(y):
        raise ValueError("Input arrays must be of Equal length")
    n = len(x)-1
    ii = np.arange(0,n+1,1)
    return(np.vectorize(lambda  a : Liv(a,x,n,i=ii).dot(y)))

if __name__ == "__main__":
    from scipy.interpolate.interpolate import lagrange
    from scipy.special import jn
    import matplotlib.pyplot as plt
    from legendre_function import setaxis

    plt.style.use("seaborn-dark-palette")
    xdata= np.array([0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0])
    ydata= np.array([1.0, 0.99, 0.96, 0.91, 0.85, 0.76, 0.67, 0.57, 0.46, 0.34, 0.22, 0.11, 0.0, -0.1, -0.18, -0.26])
    I = np.array([2.81,3.24,3.80,4.30,4.37,5.29,6.03])
    V = np.array([0.5,1.2,2.1,2.9,3.6,4.5,5.7])

    volt,volt_1 = interpolate(I,V),interpolate(I,V,inv=True)
    bessel,bessel_1 = interpolate(xdata,ydata),interpolate(xdata,ydata,inv=True) 
    x_space1 =np.linspace(0,3,100)
    y_space1 =np.linspace(1,-0.26)

    scipy_lagrange = lagrange(xdata,ydata)

    if np.allclose(bessel(x_space1),scipy_lagrange(x_space1),atol=1e-6):
        print("Verified")

    '''
    Todo : Plot n=2 Lagrange interpolation for all possible pairs 
    '''
    
    #Plotting
    fig1, (ax11, ax12) = plt.subplots(1, 2)

    ax11.scatter(xdata,ydata,label="dataset"),ax11.plot(x_space1,bessel(x_space1))
    ax11.plot(x_space1,jn(0,x_space1),linestyle="--",label="scipy's J_0")
    ax12.scatter(ydata,xdata,label="dataset"),ax12.plot(y_space1,bessel_1(y_space1))
    ax11.scatter(2.3,bessel(2.3),label="Interpolated values")

    ax12.scatter(0.5,bessel_1(0.5),label="Interpolated values")
    ax11.set_xlabel("$x$"),ax11.set_ylabel("$J_0(x)$")
    ax12.set_xlabel("$J_0(x)$"),ax12.set_ylabel("$x$")
    
    fig1.suptitle("Bessel Function", size=16)
    ## plot 2
    fig2, (ax21, ax22) = plt.subplots(1, 2)

    y_space2,x_space2 =np.linspace(0.49,5.7,100),np.linspace(2.81,6.08,100)
    ax21.scatter(I,V,label="dataset"),ax22.scatter(V,I,label="dataset")
    ax22.scatter(2.4,volt_1(2.4),label="Interpolated values")
    ax21.set_xlabel("I"),ax21.set_ylabel("V")
    ax22.set_xlabel("V"),ax22.set_ylabel("I")
    ax21.plot(x_space2,volt(x_space2)) ,ax22.plot(y_space2,volt_1(y_space2))

    ax21.legend(),ax22.legend()
    setaxis(ax11, "interpolate"), setaxis(ax12, "inverse interpolation")
    ax21.grid(),ax22.grid()
    fig2.suptitle("Photodetector Volatge vs intensity", size=16)
    plt.show()

    