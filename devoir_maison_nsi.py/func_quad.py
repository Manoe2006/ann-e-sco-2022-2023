from math import *
import numpy as np

def quad(xA,yA,xB,yB,xC,yC,xD,yD):
    
    
    
    # calcul des distances 
   
    AB=(xA-xB)**2+(yA-yB)**2
    AD=(xA-xD)**2+(yA-yB)**2
    BC=(xB-xC)**2+(yC-yC)**2
    DC=(xD-xC)**2+(yD-yC)**2
    
    
    #  definition des vecteurs 
    a = np.array([(xA-xB),(yA-yB)], float ) 
    b = np.array([(xA-xD),(yD-yA)], float )
    c = np.array([(xA-xC),(yA-yC)], float )
    d = np.array([(xB-xD),(yB-yD)], float )
    print(np.dot(c,d))
    print(np.dot(a,b))

    if quad(xA,yA,xB,yB,xC,yC,xD,yD):
      if (AB==AD==BC==DC):
        return {"Losange":True}
      else:
        return {"Losange":False}
    
    elif (np.dot(a,b)):
      if (AB==AD==BC==DC):
        return {"Carré":True}
      else:
        return {"Carré":False}
    
    elif (np.dot(a,b)):
      if ((AB==DC) and (AD==BC)):
        return {"rectangle":True}
      else:
        return {"rectangle":False}
    
    else:
      return None
      
      
   

print(quad(1,1,2,1,1,0,2,0)) 

