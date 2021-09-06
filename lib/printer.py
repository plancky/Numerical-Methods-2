
def printer(x):
    m=x.shape[-1]
    k=x.shape[0]
    s=30
    print("-"*((s+1)*k+1))
    for i in range(m):
        for j in range(k):
            print("|{0:>{space}}".format(x[i][j],space=s),end="")
            if j==k-1:
                print("|")
    print("-"*((s+1)*k+1))
    return(0)
