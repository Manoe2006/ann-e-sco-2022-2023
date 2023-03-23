# Créé par ioana, le 02/02/2023 en Python 3.7
from itertools import*
from math import*
import  matplotlib.pyplot as plt
def tri(A):
    '''Calcul des distances'''
    AB = float(A[1][0])-float(A[0][0])**2+float(A[1][1])-float(A[0][1])**2
    BC = float(A[2][0])-float(A[1][0])**2+float(A[2][1])-float(A[1][1])**2
    AC = float(A[2][0])-float(A[0][0])**2+(float(A[2][1])-float(A[0][1])**2)
    if  (int(AB**2))==(int(AC**2))+(int(BC**2)) or (int(AC**2))==(int(AB**2))+(int(BC**2)) or (int(BC**2))==(int(AB**2))+(int(AC**2)):
      return True

    else:
        return False

def carré(A):
    '''Calcul de distances'''
    AB = ((float(A[1][0])-float(A[0][0]))**2+(float(A[1][1])-float(A[0][1]))**2)
    AD = ((float(A[3][0])-float(A[0][0]))**2+(float(A[3][1])-float(A[0][1]))**2)
    DC = ((float(A[2][0])-float(A[3][0]))**2+(float(A[2][1])-float(A[3][1]))**2)
    BC = ((float(A[2][0])-float(A[1][0]))**2+(float(A[2][1])-float(A[1][1]))**2)
    VAB = [float(A[2][0])-float(A[0][0]), float(A[2][1])-float(A[0][1])]
    VAD = [float(A[3][0])-float(A[0][0]), float(A[3][1])-float(A[0][1])]
    VEC = VAB[0] * VAD[0] + VAB[1] * VAD[1]
    if (AB==BC==DC==AD) and (VEC==0):
         return True
    else:
         return False

def rec(A):
    '''Calcul des distances'''
    AB = ((float(A[1][0])-float(A[0][0]))**2+(float(A[1][1])-float(A[0][1]))**2)
    AD = ((float(A[3][0])-float(A[0][0]))**2+(float(A[3][1])-float(A[0][1]))**2)
    DC = ((float(A[2][0])-float(A[3][0]))**2+(float(A[2][1])-float(A[3][1]))**2)
    BC = ((float(A[2][0])-float(A[1][0]))**2+(float(A[2][1])-float(A[1][1]))**2)
    VAB = [float(A[2][0])-float(A[0][0]), float(A[2][1])-float(A[0][1])]
    VAD = [float(A[3][0])-float(A[0][0]), float(A[3][1])-float(A[0][1])]
    VEC = VAB[0] * VAD[0] + VAB[1] * VAD[1]

    if (((AB==DC) or  (AD==BC) and (VEC==0))):
      return True

    else:
      return False

def nuagedepts():
    Y=[]
    f=open("C:\\Users\\ioana\\Desktop\\nsi\\ann-e-sco-2022-2023\\devoir_maison_nsi.py\\monFichier_test.csv","r")
    lignes=f.readlines()
    P=[]
    H=[]
    for i in range (1,(len(lignes))):
        li=lignes[i]
        Y=li.split(";")
        P.append([Y[0],Y[1]])
    for i in range(len(P)):
        a=float(P[i][0])
        b=float(P[i][1])
        H.append([a,b])
        plt.scatter(a,b,c="purple")
    plt.show()
    x=[]
    y=[]
    for i in range(len(x)):
        x.append(H[i][0])
        y.append(H[i][1])
    print(H)

def polygone():
    Z=[]
    filin=open("C:\\Users\\ioana\\Desktop\\nsi\\ann-e-sco-2022-2023\\devoir_maison_nsi.py\\monFichier_test.csv","r")
    lignes=filin.readlines()
    for i in lignes:
        i=i.rstrip()
        i=i.split(";")
        Z.append(i)
    print(Z)
    filin.close()

    n_tri=list(combinations(Z, 3))
    for combination in n_tri:
         if tri(combination):
             print("Triangle rectangle dans le nuage de points :", combination)
             x = [float(combination[0][0]), float(combination[1][0]), float(combination[2][0]), float(combination[0][0])]
             y = [float(combination[0][1]), float(combination[1][1]), float(combination[2][1]), float(combination[0][1])]
             plt.scatter(x, y, color="green")
             plt.plot(x, y)
    plt.title("Triangle(s) rectangle(s)")
    plt.show()

    n_carré=list(combinations(Z,4))
    for combination in n_carré:
        if carré(combination):
             print("Carré dans le nuage de points :", combination)
             x = [float(combination[0][0]), float(combination[1][0]), float(combination[2][0]), float(combination[3][0])]
             y = [float(combination[0][1]), float(combination[1][1]), float(combination[2][1]), float(combination[3][1])]
             plt.scatter(x, y, color="green")
             plt.plot(x, y)
    plt.title("Carré(s)")
    plt.show()



    n_rec=list(combinations(Z,4))
    for combination in n_rec:
        if rec(combination):
             print("rectangles dans le nuage de points:",combination)
             x = [float(combination[0][0]), float(combination[1][0]), float(combination[2][0]), float(combination[0][0])]
             y = [float(combination[0][1]), float(combination[1][1]), float(combination[2][1]), float(combination[0][1])]
             plt.scatter(x,y, color="green")
             plt.plot(x,y)
    plt.title("Rectangle(s)")
    plt.show()











