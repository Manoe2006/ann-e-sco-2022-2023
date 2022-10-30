
from math import sqrt 

# fonction qui permet de determiner un carré
def carr(xA,yA,xB,yB,xC,yC,xD,yD):
     
     AB=int(sqrt((xA-xB)**2+(yA-yB)**2))
     AD=int(sqrt((xA-xD)**2+(yA-yD)**2))
     BC=int(sqrt((xB-xC)**2+(yB-yC)**2))
     DC=int(sqrt((xD-xC)**2+(yD-yC)**2))
     VAB=((xB-xA),(yB-yA))
     VAD=((xD-xA),(yD-yA))
     psca=(((xB-xA)*(xD-xA))+((yB-yA)*(yD-yA)))
     
     if ((AB==AD==BC==DC) and (psca==0)):
        print("il y a  un carré")
     
     else:
        print("il n'y pas de carré")

# Fonction qui permet de determiner un carré dans un polygone 
def rec(xA,yA,xB,yB,xC,yC,xD,yD):
     AB=int(sqrt((xA-xB)**2+(yA-yB)**2))
     AD=int(sqrt((xA-xD)**2+(yA-yD)**2))
     BC=int(sqrt((xB-xC)**2+(yB-yC)**2))
     DC=int(sqrt((xD-xC)**2+(yD-yC)**2))
     VAB=((xB-xA),(yB-yA))
     VAD=((xD-xA),(yD-yA))
     psca=(((xB-xA)*(xD-xA))+((yB-yA)*(yD-yA)))

     if ((AB==DC) and (AD==BC) and  (psca==0)):
        print("il y a un rectangle")

     else:
        print("il n'y a pas de rectangle")


# Fonction qui permet de determiner un triangle rectangle dans un polygone 
def triang_rect(xA,yA,xB,yB,xC,yC):
    
    
     AB=int(sqrt(((xA-xB)**2)+((yA-yB)**2)))
     AC=int(sqrt(((xA-xC)**2)+((yA-yC)**2)))
     BC=int(sqrt(((xB-xC)**2)+((yB-yC)**2)))
    
    
     if (AB**2)==(AC**2)+(BC**2):
        print("triangle rectangle avec AB qui est le plus grand coté")
    
     elif (AC**2)==(AB**2)+(BC**2):
        print("triangle rectangle avec AC qui est le plus grand coté")
    
     elif (BC**2)==(AB**2)+(AC**2):
        print("il y a un triangle rectangle avec BC qui est le plus grand coté")
    
     else:
        print("il n'y a pas de triangle rectangle")






'''Fonction qui permet de derterminer les différenes figures unclus dans un polygone'''
def polygone(xA,yA,xB,yB,xC,yC,xD,yD,xE,yE): 
    
    rec(xB,yB,xC,yC,xD,yD,xE,yE)
    triang_rect(xB,yB,xA,yA,xE,yE)
    carr(xB,yB,xC,yC,xD,yD,xE,yE) 
    
polygone(4,4,4,6,4,8,10,8,10,6)