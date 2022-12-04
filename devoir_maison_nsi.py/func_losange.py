from math import sqrt 
import numpy as np 

# fonction qui permet de determiner un losange dans un polygone
def los(xA,yA,xB,yB,xC,yC,xD,yD):
     
     AB=(xA-xB)**2+(yA-yB)**2
     AD=(xA-xD)**2+(yA-yB)**2
     BC=(xB-xC)**2+(yC-yC)**2
     DC=(xD-xC)**2+(yD-yC)**2
     c = np.array([(xA-xC),(yA-yC)], int )
     d = np.array([(xB-xD),(yB-yD)], int )
     
     
     if ((AB==AD==BC==DC) and  (np.dot(c,d))):
        return True
     
     else:
        return False 

print(los(1,1,2,1,1,0,2,0))
