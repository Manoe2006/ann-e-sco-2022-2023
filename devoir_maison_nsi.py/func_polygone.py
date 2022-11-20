from math import *
import numpy as np


'''fonction qui permet de determiner un carré dans un polygone'''

def carr(xA,yA,xB,yB,xC,yC,xD,yD):
     
     AB=(xA-xB)**2+(yA-yB)**2
     AD=(xA-xD)**2+(yA-yB)**2
     BC=(xB-xC)**2+(yC-yC)**2
     DC=(xD-xC)**2+(yD-yC)**2
     a = np.array([(xA-xB),(yA-yB)], int ) 
     b = np.array([(xA-xD),(yD-yA)], int )
     np.dot(a,b)
     
     if ((AB==AD==BC==DC) and (np.dot(a,b)==0)):
        return ("il y a  un carré")
     
     else:
        return ("il n'y pas de carré")

''' Fonction qui permet de determiner un carré dans un polygone '''

def rec(xA,yA,xB,yB,xC,yC,xD,yD):
     AB=(xA-xB)**2+(yA-yB)**2
     AD=(xA-xD)**2+(yA-yB)**2
     BC=(xB-xC)**2+(yC-yC)**2
     DC=(xD-xC)**2+(yD-yC)**2
     a = np.array([(xA-xB),(yA-yB)], int ) 
     b = np.array([(xA-xD),(yD-yA)], int )
     
     if ((AB==DC),(AD==BC) and (np.dot(a,b)==0)):
        return("il y a un rectangle")

     else:
        return("il n'y a pas de rectangle")


'''Fonction qui permet de determiner un triangle rectangle dans un polygone'''
def triang_rect(A):
    
    
     AB=sqrt((A[0]-A[2])**2+(A[1]-A[3])**2)
     AC=sqrt((A[0]-A[4])**2+(A[1]-A[5])**2)
     BC=sqrt((A[2]-A[4])**2+(A[3]-A[5])**2)
    
     if (int(AB**2))==(int(AC**2))+(int(BC**2)):
      return True,"AB est l'hypothénus"
    
     elif (int(AC**2))==(int(AB**2))+(int(BC**2)):
      return True,"AC est l'hypothénus"
    
     elif (int(BC**2))==(int(AB**2))+(int(AC**2)):
      return True
    
     else:
      return False







'''Fonction qui permet de dérterminer les différentes figures inclus dans un polygone'''
def polygone(A): 
    a=A[2],A[3],A[4],A[5],A[6],A[7],A[8],A[9]
    b=A[2],A[3],A[0],A[1],A[8],A[9]
    c=A[2],A[3],A[4],A[5],A[6],A[7],A[8],A[9]
    
    print(rec(a))
    print(triang_rect(b))
    

A=[0,0,0,2,3,2,3,0,7,2]
polygone(A)
