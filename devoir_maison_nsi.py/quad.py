from math import *
import numpy as np
# Fonction qui permet de definir les differents quadrilateres dans un polygone 
def quad(A):
    
    
    
    # calcul des distances 
   
    AB=sqrt((A[2]-A[0])**2+(A[3]-A[1])**2)
    AD=sqrt((A[6]-A[0])**2+(A[7]-A[1])**2)
    BC=sqrt((A[4]-A[2])**2+(A[5]-A[3])**2)
    DC=sqrt((A[4]-A[6])**2+(A[5]-A[7])**2)

    
    #  definition des vecteurs 
    a = np.array([(A[0]-A[2]),(A[1]-A[3])], int ) 
    b = np.array([(A[0]-A[6]),(A[1]-A[7])], int )
    
    
    if (np.dot(a,b)==0):
      if (AB==AD==BC==DC):
        return {"Carré":True}
      else:
        return {"Carré":False}
    
    elif (np.dot(a,b)==0):
      if ((AB==DC) and (AD==BC)):
        return {"rectangle":True}
      else:
        return {"rectangle":False}
    
    else:
      return {"Parallèlogramme":True}
      
      
   

print(quad(A=(1,1,2,1,1,0,2,0))) 

