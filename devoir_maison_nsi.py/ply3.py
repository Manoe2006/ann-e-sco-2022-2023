# Créé par ioana, le 14/02/2023 en Python 3.7
from itertools import*
from math import*
import  matplotlib.pyplot as plt
def tri(A):
    '''Calcul des distances'''
    AB = int(A[1][0])-int(A[0][0])**2+(int(A[1][1])-int(A[0][1]))**2
    BC = int(A[2][0])-int(A[1][0])**2+(int(A[2][1])-int(A[1][1]))**2
    AC = int(A[2][0])-int(A[0][0])**2+(int(A[2][1])-int(A[0][1])**2)

    if  ((AB**2)==(AC**2)+(BC**2) or (AC**2)==(AB**2)+(BC**2) or (BC**2)==(AB**2)+(AC**2)):
      return {"Triangle rectangle":True}

    else:
        return {"triangle rectangle":False}

def carré(A):
    '''Calcul de distances'''
    AB = ((int(A[1][0])-int(A[0][0]))**2+(int(A[1][1])-int(A[0][1]))**2)
    AD = ((int(A[3][0])-int(A[0][0]))**2+(int(A[3][1])-int(A[0][1]))**2)
    DC = ((int(A[2][0])-int(A[3][0]))**2+(int(A[2][1])-int(A[3][1]))**2)
    BC = ((int(A[2][0])-int(A[1][0]))**2+(int(A[2][1])-int(A[1][1]))**2)
    VAB = [int(A[2][0])-int(A[0][0]), int(A[2][1])-int(A[0][1])]
    VAD = [int(A[3][0])-int(A[0][0]), int(A[3][1])-int(A[0][1])]
    VEC = VAB[0] * VAD[0] + VAB[1] * VAD[1]
    if (AB==BC==DC==AD) and (VEC==0):
         return {"carré":True}
    else:
         return {"carré":False}

def rec(A):
    '''Calcul des distances'''
    AB = ((int(A[1][0])-int(A[0][0]))**2+(int(A[1][1])-int(A[0][1]))**2)
    AD = ((int(A[3][0])-int(A[0][0]))**2+(int(A[3][1])-int(A[0][1]))**2)
    DC = ((int(A[2][0])-int(A[3][0]))**2+(int(A[2][1])-int(A[3][1]))**2)
    BC = ((int(A[2][0])-int(A[1][0]))**2+(int(A[2][1])-int(A[1][1]))**2)
    VAB = [int(A[2][0])-int(A[0][0]), int(A[2][1])-int(A[0][1])]
    VAD = [int(A[3][0])-int(A[0][0]), int(A[3][1])-int(A[0][1])]
    VEC = VAB[0] * VAD[0] + VAB[1] * VAD[1]

    if (((AB==DC) or  (AD==BC) and (VEC==0))):
      return {"Rectangle":True}

    else:
      return {"Rectangle":False}

def nuagedepts():
    Y=[]
    f=open("C:\\Users\\ioana\\Desktop\\nsi\\ann-e-sco-2022-2023\\devoir_maison_nsi.py\\mano_test.csv","r")
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
    filin=open("C:\\Users\\ioana\\Desktop\\nsi\\ann-e-sco-2022-2023\\devoir_maison_nsi.py\\mano_test.csv","r")
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
             x = [int(combination[0][0]), int(combination[1][0]), int(combination[2][0]), int(combination[0][0])]
             y = [int(combination[0][1]), int(combination[1][1]), int(combination[2][1]), int(combination[0][1])]
             plt.scatter(x, y, color="green")
             plt.plot(x, y)
    plt.title("Triangle(s) rectangle(s)")
    plt.show()

    n_carré=list(combinations(Z,4))
    for combination in n_carré:
        if carré(combination):
             print("Carré dans le nuage de points :", combination)
             x = [int(combination[0][0]), int(combination[1][0]), int(combination[2][0]), int(combination[0][0])]
             y = [int(combination[0][1]), int(combination[1][1]), int(combination[2][1]), int(combination[0][1])]

             plt.scatter(x, y, color="green")
             plt.plot(x, y)
    plt.title("Carré(s)")
    plt.show()



    n_rec=list(combinations(Z,4))
    for combination in n_rec:
        if rec(combination):
             print("rectangles dans le nuage de points:",combination)
             x = [int(combination[0][0]), int(combination[1][0]), int(combination[2][0]), int(combination[0][0])]
             y = [int(combination[0][1]), int(combination[1][1]), int(combination[2][1]), int(combination[0][1])]
             plt.scatter(x,y, color="green")
             plt.plot(x,y)
    plt.title("Rectangle(s)")
    plt.show()




