from math import sqrt 
import numpy as np 

# Fonction qui permet de determiner un rectangle dans un polygone  
def rec(xA,yA,xB,yB,xC,yC,xD,yD):
     
     AB=int(sqrt((xA-xB)**2+(yA-yB)**2))
     AD=int(sqrt((xA-xD)**2+(yA-yD)**2))
     BC=int(sqrt((xB-xC)**2+(yB-yC)**2))
     DC=int(sqrt((xD-xC)**2+(yD-yC)**2))
     a = np.array([xD,yD], int ) 
     b = np.array([xB,yB], int )
     
     

     if ((AB==DC) and (AD==BC) or  (np.dot(a,b))):
        print("il y a un rectangle")

     else:
        print("il n'y a pas de rectangle")

rec(1,2,3,2,1,1,3,1)

