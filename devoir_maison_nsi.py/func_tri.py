from math import *

def tri(A):
  

    AB=sqrt((A[2]-A[0])**2+(A[3]-A[1])**2)
    AC=sqrt(((A[4]-A[0])**2+(A[5]-A[1])**2))
    BC=sqrt((A[4]-A[2])**2+(A[5]-A[3])**2)

    if  ((int(AB**2))==(int(AC**2))+(int(BC**2)) or (int(AC**2))==(int(AB**2))+(int(BC**2)) or (int(BC**2))==(int(AB**2))+(int(AC**2))):
      return {"Triangle rectangle":True}
    
    elif (AC==AB==BC):
      return {"Triangle équilatéral":True} 
    
    elif AB==AC or AB==BC or AC==BC :
        return {"Triangle isocèle":True}
    
    else: 
        return {"triangle quelconque":True}

print(tri(A=[3,1,0,4,8,1]))

    
    
    
    

