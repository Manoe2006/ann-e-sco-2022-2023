from math import *
from itertools import *

'''fonction qui permet de determiner un carré '''
def carr(A):
    
    # calculs des distances
    AB=sqrt((A[2]-A[0])**2+(A[3]-A[1])**2)
    AD=sqrt((A[6]-A[0])**2+(A[7]-A[1])**2)
    BC=sqrt((A[4]-A[2])**2+(A[5]-A[3])**2)
    DC=sqrt((A[4]-A[6])**2+(A[5]-A[7])**2)
    VAB=A[2]-A[0],A[3]-A[1]
    VAD=A[6]-A[0],A[7]-A[1]
    VEC=VAB[0]*VAD[0]+VAB[1]*VAD[1]

    if ((AB==AD==BC==DC) and  (VEC==0)):
        return {"Carré":True}
     
    else:
        return {"Carré":False} 


'''Fonction qui permet de determiner un rectangle'''  
def rec(A):
    # calculs des distances
    AB=sqrt((A[2]-A[0])**2+(A[3]-A[1])**2)
    AD=sqrt((A[6]-A[0])**2+(A[7]-A[1])**2)
    BC=sqrt((A[4]-A[2])**2+(A[5]-A[3])**2)
    DC=sqrt((A[4]-A[6])**2+(A[5]-A[7])**2)
    VAB=A[2]-A[0],A[3]-A[1]
    VAD=A[6]-A[0],A[7]-A[1]
    VEC=VAB[0]*VAD[0]+VAB[1]*VAD[1]
     
    if (((AB==DC) or  (AD==BC) and (VEC==0))):
      return {"Rectangle":True}

    else:
      return {"Rectangle":False}


'''fonction qui determine avec les coordonnées un triangle rectangle '''
def tri(A):
  for i in range(len(A)):
      # calculs des distances
      AB=sqrt(((A[i][2]-A[i][0])**2+(A[i][3]-A[i][1])**2))
      AC=sqrt(((A[i][4]-A[i][0])**2+(A[i][5]-A[i][1])**2))
      BC=sqrt(((A[i][4]-A[i][2])**2+(A[i][5]-A[i][3])**2))

      if  ((int(AB**2))==(int(AC**2))+(int(BC**2)) or (int(AC**2))==(int(AB**2))+(int(BC**2)) or (int(BC**2))==(int(AB**2))+(int(AC**2))):
        return {"Triangle rectangle":True}
      
      elif (AC==AB==BC):
        return {"Triangle équilatéral":True} 
      
      elif AB==AC or AB==BC or AC==BC:
          return {"Triangle isocèle":True}
      
      else: 
          return {"triangle quelconque":True} 



   

'''Fonction nuage de points/reconnaissance de forme'''
def pts():
  A=[]
  f=open("mon.csv","r")
  lignes=f.readlines()
  B=[]
  C=[]
  for i in range(1,(len(lignes))):
    l=lignes[i]
    A=l.split(";")
    B.append(A[0],A[1])
  for i in range(len(B)):
    s=float(B[i][0])
    k=float(len(B))
    C.append([s,k])
  return C

print(pts())   

    


     









