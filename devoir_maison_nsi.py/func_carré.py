from math import sqrt 
import numpy as np 

# fonction qui permet de determiner un carré dans un polygone
def carr(xA,yA,xB,yB,xC,yC,xD,yD):
     
     AB=int(sqrt((xA-xB)**2+(yA-yB)**2))
     AD=int(sqrt((xA-xD)**2+(yA-yD)**2))
     BC=int(sqrt((xB-xC)**2+(yB-yC)**2))
     DC=int(sqrt((xD-xC)**2+(yD-yC)**2))
     a = np.array([xD,yD], int ) 
     b = np.array([xB,yB], int )
     print(np.dot(a,b))
     
     if ((AB==AD==BC==DC) or (np.dot(a,b))):
        print("il y a  un carré")
     
     else:
        print("il n'y pas de carré")

carr(1,1,2,1,1,0,2,0)

     

     




    

   
    