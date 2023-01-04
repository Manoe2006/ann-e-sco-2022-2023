from math import sqrt 


# Fonction qui permet de determiner un rectangle dans un polygone  
def rec(A):
    AB=sqrt((A[2]-A[0])**2+(A[3]-A[1])**2)
    AD=sqrt((A[6]-A[0])**2+(A[7]-A[1])**2)
    BC=sqrt((A[4]-A[2])**2+(A[5]-A[3])**2)
    DC=sqrt((A[4]-A[6])**2+(A[5]-A[7])**2)
    VAB=A[2]-A[0],A[3]-A[1]
    VAD=A[6]-A[0],A[7]-A[1]
    VEC=VAB[0]*VAD[0]+VAB[1]*VAD[1]
     
    if (((AB==DC) or  (AD==BC) and (VEC==0))):
      return {"Rectangle":True}

    else:
      return {"Rectangle":False}

print(rec(A=[1,2,3,2,1,1,3,1]))

