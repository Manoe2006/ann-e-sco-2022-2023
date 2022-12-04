from math import *
import numpy as np


'''fonction qui permet de determiner un carré dans un polygone'''

def carr(xA,yA,xB,yB,xC,yC,xD,yD):
     
     
     AB=(xA-xB)**2+(yA-yB)**2
     AD=(xA-xD)**2+(yA-yB)**2
     BC=(xB-xC)**2+(yB-yC)**2
     DC=(xD-xC)**2+(yD-yC)**2
     a = np.array([(xA-xB),(yA-yB)], float ) 
     b = np.array([(xA-xD),(yD-yA)], float )
     
     
     if ((AB==AD==BC==DC) and (np.dot(a,b))):
        return {"Carré": True}
     
     else:
        return {"Carré": False}

''' Fonction qui permet de determiner un carré dans un polygone '''

def rec(xA,yA,xB,yB,xC,yC,xD,yD):

     AB=(xA-xB)**2+(yA-yB)**2
     AD=(xA-xD)**2+(yA-yB)**2
     BC=(xB-xC)**2+(yB-yC)**2
     DC=(xD-xC)**2+(yD-yC)**2
     a = np.array([(xA-xB),(yA-yB)], float ) 
     b = np.array([(xA-xD),(yD-yA)], float )
     
     if ((AB==DC),(AD==BC) and (np.dot(a,b))):
        return {"Rectangle": True}

     else:
        return {"Rectangle": False}


'''Fonction qui permet de determiner un triangle rectangle dans un polygone'''
def triang_rect(xA,yA,xB,yB,xC,yC):
    
    
     AB=sqrt((xA-xB)**2+(yA-yB)**2)
     AC=sqrt((xA-xC)**2+(yA-yC)**2)
     BC=sqrt((xB-xC)**2+(yB-yC)**2)
    
     if (int(AB**2))==(int(AC**2))+(int(BC**2)):
      return {"Triangle rectangle":True}
    
     elif (int(AC**2))==(int(AB**2))+(int(BC**2)):
      return {"Triangle rectangle":True}
    
     elif (int(BC**2))==(int(AB**2))+(int(AC**2)):
      return {"Triangle rectangle":True}
    
     else:
      return {"Triangle rectangle":False}







'''Fonction qui permet de dérterminer les différentes figures inclus dans un polygone'''
def polygone(xA,yA,xB,yB,xC,yC,xD,yD,xE,yE): 
    print(carr(xB,yB,xC,yC,xD,yD,xE,yE))
    print(rec(xB,yB,xC,yC,xD,yD,xE,yE))
    print(triang_rect(xB,yB,xA,yA,xE,yE))
    
    


polygone(0,0,0,2,3,2,3,0,7,2)
