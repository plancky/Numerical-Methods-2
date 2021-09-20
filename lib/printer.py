import numpy as np
def printer(x,column=True):
    s=30
    k,m=x.shape[-1],x.shape[-2]
    print("\n"+"-"*((s+1)*k+1))
    for i in range(m):
        for j in range(k):
            a=">"
            if column==True and i==0:
                a="^"
            print("|{0:{align}{space}}".format(x[i][j],align=a,space=s),end="")
            if j==k-1:
                print("|")
                if column==True and i==0:
                    print("-"*((s+1)*k+1))
    print("-"*((s+1)*k+1)+"\n")

def matrixp(x):
    a= "\n"+r"$$\begin{pmatrix}" + "\n"
    c= r"\end{pmatrix}$$" + "\n"
    b= ""
    k,m=x.shape[-1],x.shape[-2]
    
    for i in range(m):
        func = lambda x : "{:.3g}".format(x) 
        f = np.vectorize(func)
        b += " & ".join(list(f(x[i]))) + r"\\" + "\n"
    return(a+b+c)
