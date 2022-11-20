from math import *
import numpy as np

def quad(xA,yA,xB,yB,xC,yC,xD,yD):
    M={}
    N={}
    O={}
    
    
    # calcul des distances 
    AB=(xA-xB)**2+(yA-yB)**2
    AD=(xA-xD)**2+(yA-yB)**2
    BC=(xB-xC)**2+(yC-yC)**2
    DC=(xD-xC)**2+(yD-yC)**2
    AC=(xA-xC)**2+(yA-yC)**2
    BD=(xB-xD)**2+(yC-yD)**2
    
    #  definition des vecteurs 
    a = np.array([(xA-xB),(yA-yB)], int ) 
    b = np.array([(xA-xD),(yA-yD)], int )
    c = np.array([(xA-xC),(yA-yC)], int )
    d = np.array([(xB-xD),(yB-yD)], int )

    if (AB==AD==BC==DC) and (np.dot(c,d)):
      B={"losange": True}
      return M.update(B)
      print(M)
   
    

    elif (AB==AD==BC==DC) and (np.dot(a,b)):
      C={"Carré": True}
      return N.update(C)
      print(N)
   
     
    elif (AD==BC) or (AB==DC) and (np.dot(a,b)):
      D={"rectangle":True}
      return O.update(D)
      print(O)
   

print(quad(1,1,2,1,1,0,2,0))
