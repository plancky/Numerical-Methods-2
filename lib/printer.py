
def printer(x,column=True):
    s=30
    k=x.shape[0]
    m=x.shape[-1]
    print("-"*((s+1)*k+1))
    for i in range(m):
        for j in range(k):
            print("|{0:>{space}}".format(x[i][j],space=s),end="")
            if j==k-1:
                print("|")
                if column==True and i==0:
                    print("-"*((s+1)*k+1))
    print("-"*((s+1)*k+1))
