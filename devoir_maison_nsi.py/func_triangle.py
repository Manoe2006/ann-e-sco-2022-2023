from math import sqrt 

'''fonction qui determine avec les coordonnées un triangle rectangle'''
def triang_rect(A):
   
    # calculs des distances
    AB=sqrt((A[2]-A[0])**2+(A[3]-A[1])**2)
    AC=sqrt(((A[4]-A[0])**2+(A[5]-A[1])**2))
    BC=sqrt((A[4]-A[2])**2+(A[5]-A[3])**2)
    
    if ((int(AB**2))==(int(AC**2))+(int(BC**2)) or (int(AC**2))==(int(AB**2))+(int(BC**2)) or (int(BC**2))==(int(AB**2))+(int(AC**2))):
      return {"Triangle rectangle":True}
    
    else:
      return {"Triangle rectangle":False}

print(triang_rect(A=[3,1,3,4,8,1]))


'''fonction qui determine avec les coordonnées un triangle rectangle dans un nuage de points'''
def tri(A):
  for i in range(len(A)):
      # calculs des distances
      AB=((A[i][2]-A[i][0])**2+(A[i][3]-A[i][1])**2)
      AC=((A[i][4]-A[i][0])**2+(A[i][5]-A[i][1])**2)
      BC=((A[i][4]-A[i][2])**2+(A[i][5]-A[i][3])**2)

      if  ((int(AB**2))==(int(AC**2))+(int(BC**2)) or (int(AC**2))==(int(AB**2))+(int(BC**2)) or (int(BC**2))==(int(AB**2))+(int(AC**2))):
        return {"Triangle rectangle":True}
      
      else: 
          return {"triangle rectangle":False} 






    
    
