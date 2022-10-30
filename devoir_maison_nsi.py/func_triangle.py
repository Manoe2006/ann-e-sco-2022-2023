# fonction qui determine avec les coordonnées un triangle rectangle inscrit dans un polygone
def triang_rect(xA,yA,xB,yB,xE,yE):
    from math import sqrt 
    
    AB=int(sqrt(((xA-xB)**2)+((yA-yB)**2)))
    AE=int(sqrt(((xA-xE)**2)+((yA-yE)**2)))
    BE=int(sqrt(((xB-xE)**2)+((yB-yE)**2)))
    print(AB)
    print(AE)
    print(BE)
    
    if (AB**2)==(AE**2)+(BE**2):
        print("triangle rectangle avec AB qui est le plus grand coté")
    
    elif (AE**2)==(AB**2)+(BE**2):
        print("triangle rectangle avec AC qui est le plus grand coté")
    
    elif (BE**2)==(AB**2)+(AE**2):
        print("triangle rectangle avec BC qui est le plus grand coté")
    
    else:
        print("ce polygone n'a pas de triangle rectangle")

    
    
triang_rect(3,1,3,4,8,1)


    
    
