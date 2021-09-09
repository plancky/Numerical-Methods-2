
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
