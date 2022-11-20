from math import sqrt 
import numpy as np 

# Fonction qui permet de determiner un rectangle dans un polygone  
def rec(A):
     
     AB=int(sqrt((A[0]-A[2])**2+(A[1]-A[3])**2))
     AD=int(sqrt((A[0]-A[6])**2+(A[1]-A[7])**2))
     BC=int(sqrt((A[2]-A[4])**2+(A[3]-A[5])**2))
     DC=int(sqrt((A[6]-A[4])**2+(A[7]-A[5])**2))
     a = np.array([A[4],A[5]], int ) 
     b = np.array([A[2],A[3]], int )
     
     

     if ((AB==DC) and (AD==BC) and  (np.dot(a,b))):
        return True

     else:
        return False

print(rec(A=[1,2,3,2,1,1,3,1]))

