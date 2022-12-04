from math import sqrt 
import numpy as np 

# fonction qui permet de determiner un carré dans un polygone
def carr(xA,yA,xB,yB,xC,yC,xD,yD):
     
     AB=(xA-xB)**2+(yA-yB)**2
     AD=(xA-xD)**2+(yA-yB)**2
     BC=(xB-xC)**2+(yC-yC)**2
     DC=(xD-xC)**2+(yD-yC)**2
     a = np.array([(xA-xB),(yA-yB)], int ) 
     b = np.array([(xA-xD),(yA-yD)], int )
     print(np.dot(a,b))
     
     if ((AB==AD==BC==DC) and  (np.dot(a,b))):
        return True
     
     else:
        return False 

print(carr(1,1,2,1,1,0,2,0))

     

     




    

   
    