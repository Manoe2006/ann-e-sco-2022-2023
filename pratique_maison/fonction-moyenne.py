def moy(A):
    s=0
    m=0
    
    for i in A:
        s=s+i
        m=s//len(A)
    return m 

A=[10,11,15]
print(moy(A))
