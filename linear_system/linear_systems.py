import numpy as np 
import os

def matrixp(x):
    c= r"\end{array}\right]$$" + "\n"
    b= ""
    k,m=x.shape[-1],x.shape[-2]
    a= "\n"+r"$$\left[\begin{array}"+"{"+(k-1)*"c"+"|c"+"}" + "\n"
    
    for i in range(m):
        func = lambda x : "{:.3g}".format(x) 
        f = np.vectorize(func)
        b += " & ".join(list(f(x[i]))) + r"\\" + "\n"
    return(a+b+c)


def gauss_elim(A,b,loc ="electric_circuit.md"):
    k,m = A.shape
    if b.ndim == 1 :
        b_len = len(b)
    if k != b_len:
        raise ValueError("no. of rows in A must be same as the number of rows in b ")
    aug = np.column_stack((A,b))
    dat=""
    i = 0
    for j in np.arange(m):
        bool_j = A[i:,j]!=0
        if np.any(bool_j):   
            dat+=matrixp(aug)
            new_i = np.where(bool_j)[0][0] +i 
            aug[[i,new_i]]=aug[[new_i,i]]  
            pivot =aug[i][j]
            aug[i] = aug[i]/pivot #scale
            dat+=matrixp(aug)
            if i+1 == k :
                break
            else: #pivot
                for row in np.arange(i+1,k):
                    aug[row]= aug[row]-aug[row][j]*aug[i]
                    dat+=matrixp(aug)
                i+=1
    #f = open(os.getcwd()+f'/{loc}','w')
    #f.write(dat)
    #f.close() 
    return(aug,dat)

def gauss_jordan(aug):
    aug=aug.copy()
    k = aug.shape[0]
    for j in np.arange(k-1,0,-1):
        for row in np.arange(j-1,-1,-1):
            aug[row]= aug[row]-aug[row][j]*aug[j]
    return(aug)
    
def gauss_seidel(A,b,N=500,tol=1e-8):
    A,b = A.copy(),b.copy()
    k,m = A.shape
    if b.ndim == 1 :
        b_len = len(b)
    if k != b_len:
        raise ValueError("no. of rows in A must be same as the number of rows in b ")
    aug = np.column_stack((A,b))
    i=0
    for j in np.arange(m):
        bool_j = A[i:,j]!=0
        if np.any(bool_j):
            new_i = np.where(bool_j)[0][0] +i 
            aug[[i,new_i]]=aug[[new_i,i]] 
            i+=1
    A,b = aug[:,:-1],aug[:,-1]
    x = b/(np.diagonal(A))
    for n in np.arange(N):
        new_x=x.copy()
        for row in np.arange(k): # 0,1,2,..k-1
            #print(A[row])   
            new_x[row]= (b[row]-np.sum(np.delete(A[row]*new_x,row,axis=0))) / A[row][row] 
        print(new_x)  
        if np.abs((new_x - x)).max() <= tol:
            break
        else:
            x = new_x.copy()
    return(new_x)
            

if __name__=="__main__":
    a= np.array([[4,-2,1],
                [1,1,1],
                [9,3,1]],dtype=float)
    b=np.array([20,5,25],dtype=float)
    
    print(gauss_seidel(a,b))
    print(np.linalg.solve(a,b))
    
    
    a= np.array([[4,-2,1],
                [1,1,1],
                [9,3,1]],dtype=float)
    b=np.array([20,5,25],dtype=float)

    print(gauss_seidel(a,b))
    print(np.linalg.solve(a,b))