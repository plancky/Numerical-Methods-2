import numpy as np

def term(x,xn,i,n):
    s=0
    for k in range(0,n):
        if i!=k:
            s+= (x - xn[i])/(xn[i] - xn[k])
    return(s)

def interpolate(x,y,n):
    i = np.arrange(0,len(x))
    f = np.vectorize(term,excluded =[0,1,3] )
    return  (lambda a : np.sum(f(a,x,i,n)*y) )

