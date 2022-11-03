from math import sqrt 

# fonction qui determine avec les coordonnées un triangle rectangle inscrit dans un polygone
def triang_rect(xA,yA,xB,yB,xC,yC):
   
    
    AB=sqrt((xA-xB)**2+(yA-yB)**2)
    AC=sqrt((xA-xC)**2+(yA-yC)**2)
    BC=sqrt((xB-xC)**2+(yB-yC)**2)
    
    if (int(AB**2))==(int(AC**2))+(int(BC**2)):
        print("triangle rectangle avec AB qui est le plus grand coté")
    
    elif (int(AC**2))==(int(AB**2))+(int(BC**2)):
        print("triangle rectangle avec AC qui est le plus grand coté")
    
    elif (int(BC**2))==(int(AB**2))+(int(AC**2)):
        print("il y a un triangle rectangle avec BC qui est le plus grand coté")
    
    else:
        print("il n'y a pas de triangle rectangle")

    
    
triang_rect(3,1,3,4,8,1)


    
    
