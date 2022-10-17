# Créé par ioana, le 11/10/2022 en Python 3.7
def img(a,b,c,x):
    return a*x**2+b*x+c


from math import sqrt

def sol(a,b,c):
    ''' ce programme permet de trouver les racines d'une expression du second degré'''
    if (a==0 and b==0 and c==0):
        return (3,0,0)

    elif (a==0 and b==0 and c!=0):
        return (0,0,0)

    elif (a==0 and b!=0):
        return(1,-c/b,0)

    else:
        disc= b**2-4*a*c
        if disc >0:
            x1=(-b-sqrt(disc))/(2*a)
            x2=(-b+sqrt(disc))/(2*a)
            return (2,x1,x2)

        elif (disc==0):
            x3= -b/(2*a)
            return (1,x3,0)

        elif disc < 0:
            return (0,0,0)




















