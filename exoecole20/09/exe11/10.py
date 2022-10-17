def img(a,b,c,x): 
    return a*x**2+b*x+c


from math import sqrt  
def sol(a,b,c):
    disc= b**2-4*a*c

    if disc >0:
        x1=(-b-sqrt(disc))/2*a 
        x2=(-b+sqrt(disc))/2*a
        return (1,x1,x2)
    elif (disc==0):
        x= -b/2*a 
        return (1,x)
    else:
        return (0,0,0)
         

sol(1,4,7)