from math import *
import numpy as np 

# "1"="carré", "2"="rectangle", "3"="losange" 
# fonction qui determine tout les quadrilataires inclus dans un polygone 
def quad(A):
    # calcul des distances 
     AB=int(sqrt((A[0]-A[2])**2+(A[1]-A[3])**2))
     AD=int(sqrt((A[0]-A[6])**2+(A[1]-A[7])**2))
     BC=int(sqrt((A[2]-A[4])**2+(A[3]-A[5])**2))
     DC=int(sqrt((A[6]-A[4])**2+(A[7]-A[5])**2))
     AC=int(sqrt((A[0]-A[4])**2+(A[1]-A[5]**2)))
     BD=int(sqrt((A[2]-A[6])**2+(A[3]-A[7])**2))
    
    #  definition des vecteurs 
     c= np.array([(A[2]-A[0]),(A[3]-A[1])], int ) 
     d= np.array([(A[6]-A[0]),(A[7]-A[1])], int )
     a = np.array([(A[4]-A[0]),(A[5]-A[1])], int ) 
     b = np.array([(A[4]-A[2]),(A[5]-A[3])], int ) 

     if (AB==AD==BC==DC) and (np.dot(c,d)):
        return "1"
    
     elif (AB==AD==BC==DC) and (np.dot(a,b)):
        return "2"
     
     elif (AD==BC) or (AB==DC) and (np.dot(c,d)):
        return "3"






'''Fonction qui permet de determiner un triangle rectangle dans un polygone'''
def triang_rect(A):
    
    
     AB=sqrt((A[0]-A[2])**2+(A[1]-A[3])**2)
     AC=sqrt((A[0]-A[4])**2+(A[1]-A[5])**2)
     BC=sqrt((A[2]-A[4])**2+(A[3]-A[5])**2)
    
     if (int(AB**2))==(int(AC**2))+(int(BC**2)):
        return "triangle rectangle avec AB qui est le plus grand coté"
    
     elif (int(AC**2))==(int(AB**2))+(int(BC**2)):
        return "triangle rectangle avec AC qui est le plus grand coté"
    
     elif (int(BC**2))==(int(AB**2))+(int(AC**2)):
        return "il y a un triangle rectangle avec BC qui est le plus grand coté"
    
     else:
        return "il n'y a pas de triangle rectangle"






'''Fonction qui permet de dérterminer les différentes figures inclus dans un polygone'''
def polygone(A): 
    X=A[2],A[3],A[4],A[5],A[6],A[7],A[8],A[9]
    Z=A[2],A[3],A[0],A[1],A[8],A[9]
    quad(X)
    triang_rect(Z)
    

A=[0,0,0,2,3,2,3,0,7,2]
print(polygone(A)) 
