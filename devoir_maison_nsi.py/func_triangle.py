from math import sqrt 

# fonction qui determine avec les coordonnées un triangle rectangle inscrit dans un polygone
def triang_rect(A):
   
    
    AB=sqrt((A[0]-A[2])**2+(A[1]-A[3])**2)
    AC=sqrt((A[0]-A[4])**2+(A[1]-A[5])**2)
    BC=sqrt((A[2]-A[4])**2+(A[3]-A[5])**2)
    
    if (int(AB**2))==(int(AC**2))+(int(BC**2)):
            
        return True,"AB est l'hypothénus"
    
    elif (int(AC**2))==(int(AB**2))+(int(BC**2)):
        return True,"AC est l'hypothénus"
    
    elif (int(BC**2))==(int(AB**2))+(int(AC**2)):
        return True,"BC est l'hypothénus"
    
    else:
       return False

    
    
print(triang_rect(A=[3,1,3,4,8,1]))



    
    
