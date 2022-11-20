from math import sqrt 
import numpy as np 

# fonction qui permet de determiner un carré dans un polygone
def carr(A):
     
     AB=int(sqrt((A[0]-A[2])**2+(A[1]-A[3])**2))
     AD=int(sqrt((A[0]-A[6])**2+(A[1]-A[7])**2))
     BC=int(sqrt((A[2]-A[4])**2+(A[3]-A[5])**2))
     DC=int(sqrt((A[6]-A[4])**2+(A[7]-A[5])**2))
     a = np.array([(A[2]-A[0]),(A[3]-A[1])], int ) 
     b = np.array([(A[6]-A[0]),(A[7]-A[1])], int )
     print(np.dot(a,b))
     
     if ((AB==AD==BC==DC) and  (((A[6]-A[0])-(A[7]-A[1]))+((A[2]-A[0])-(A[3]-A[1]))==0)):
        print("il y a  un carré")
     
     else:
        print("il n'y pas de carré")

carr(A=[1,1,2,1,1,0,2,0])

     

     




    

   
    