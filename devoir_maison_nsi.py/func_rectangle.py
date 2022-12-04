from math import sqrt 
import numpy as np 

# Fonction qui permet de determiner un rectangle dans un polygone  
def rec(xA,yA,xB,yB,xC,yC,xD,yD):
     
     AB=(xA-xB)**2+(yA-yB)**2
     AD=(xA-xD)**2+(yA-yB)**2
     BC=(xB-xC)**2+(yC-yC)**2
     DC=(xD-xC)**2+(yD-yC)**2
     a = np.array([(xA-xB),(yA-yB)], int ) 
     b = np.array([(xA-xD),(yA-yD)], int )
     

     if ((AB==DC) and (AD==BC) and  (np.dot(a,b))):
        return True

     else:
        return False

print(rec(1,2,3,2,1,1,3,1))

