from math import sqrt

def nature(a,b,c):
    disc=b**2-4*a*c

    if disc > 0: 
        x1=(-b-sqrt(disc))/2*a 
        x2=(-b+sqrt(disc))/2*a 
        
        print("la premiere racine est : x1=", x1 )
        print("la deuxieme racine est : x2=", x2 )

    elif (disc==0):
        x= (-b)/2*a
        
        print("la racine est:x=", x )
    else:
        print("non factorisable car le discriminant est inferieur a 0")

    
nature(-6,5,-14)



    
    
