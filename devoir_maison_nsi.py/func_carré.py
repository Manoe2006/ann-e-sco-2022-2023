from math import sqrt 


# fonction qui permet de determiner un carré dans un polygone
def carr(A):
     
    AB=sqrt((A[2]-A[0])**2+(A[3]-A[1])**2)
    AD=sqrt((A[6]-A[0])**2+(A[7]-A[1])**2)
    BC=sqrt((A[4]-A[2])**2+(A[5]-A[3])**2)
    DC=sqrt((A[4]-A[6])**2+(A[5]-A[7])**2)
    VAB=A[2]-A[0],A[3]-A[1]
    VAD=A[6]-A[0],A[7]-A[1]
    VEC=VAB[0]*VAD[0]+VAB[1]*VAD[1]

    if ((AB==AD==BC==DC) and  (VEC==0)):
        return {"Carré":True}
     
    else:
        return {"Carré":False} 

print(carr(A=(0,0,0,2,2,2,2,0)))

     

     




    

   
    