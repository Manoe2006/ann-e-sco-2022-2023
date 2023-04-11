from math import sqrt
from itertools import *
import matplotlib.pyplot as plt
"Ce proramme permet de reconnaitre certaines figures particulieres contenues dans un NUAGE DE POINT "
#programme principal avec le fichier et les minis focntions y compris
def princip(figure):
    V=[]
    f=open("C:\\Users\\ioana\\Desktop\\nsi\\ann-e-sco-2022-2023\\devoir_maison_nsi.py\\mano_test.csv","r")
    lignes=f.readlines()
    P=[]
    B=[]
    M=[]
    for i in range(1,len(lignes)):
        li=lignes[i]
        V=li.split(";")
        P.append([V[0],V[1]])
    for i in range(len(P)):
        s=float(P[i][0])
        k=float(P[i][1])
        B.append([s,k])
    x=[]
    y=[]
    for i in range(len(B)):
        x.append(B[i][0])
        y.append(B[i][1])
    #affichage des points en rouge avec plt.scatter
    plt.scatter(x,y,c="red")
    plt.show()
    #choix des figures }}
    if (figure==carré):
        carré(B)
    if (figure==TriangleR):
        TriangleR(B)
    if (figure==Rectangle):
        Rectangle(B)
    if  (figure==Triangle_R_Iso):
        Triangle_R_Iso(B)
    if (figure==Triangle_Equi):
        Triangle_Equi(B)
    if (figure==Parallelogramme):
        Parallelogramme(B)
    if (figure==n_figure):
        n_figure(B)
#les minis fonctions sont rappellé ici
#n designe toutes les figures
def n_figure(B):
    carré(B)
    Rectangle(B)
    TriangleR(B)
    Triangle_R_Iso(B)
    Triangle_Equi(B)
    Parallelogramme(B)

def carré(B):
    x=[]
    y=[]
    E=[]
    o=0
    #combinations de la liste B car un carré n'a que 4 cotés donc 4 points
    E=list(combinations(B,4))
    print(E)
    for i in range(len(E)):
        #calcul des distances a l'aide des formules vectorielles
        AB=sqrt((E[i][1][0]-E[i][0][0])**2+(E[i][1][1]-E[i][0][1])**2)
        AD=sqrt((E[i][3][0]-E[i][0][0])**2+(E[i][3][1]-E[i][0][1])**2)
        BC=sqrt((E[i][2][0]-E[i][1][0])**2+(E[i][2][1]-E[i][1][1])**2)
        CD=sqrt((E[i][3][0]-E[i][2][0])**2+(E[i][3][1]-E[i][2][1])**2)
        AC=sqrt((E[i][2][0]-E[i][0][0])**2+(E[i][2][1]-E[i][0][1])**2)
        BD=sqrt((E[i][3][0]-E[i][1][0])**2+(E[i][3][1]-E[i][1][1])**2)
        #coordonnée du vecteurs AB et BC
        xAB=(E[i][1][0]-E[i][0][0])
        yAB=(E[i][1][1]-E[i][0][1])
        xBC=(E[i][2][0]-E[i][1][0])
        yBC=(E[i][2][1]-E[i][1][1])
        #produit scalaire entre AB et BC afin s'ils sont perpendiculaire et qu'il ya un angle droit
        k=((xAB)*(xBC))+((yAB)*(yBC))
        if (AB==AD==BC==CD) and (k==0):
            o=o+1
            x=[E[i][0][0],E[i][1][0],E[i][2][0],E[i][3][0],E[i][0][0]]
            y=[E[i][0][1],E[i][1][1],E[i][2][1],E[i][3][1],E[i][0][1]]
            plt.plot(x,y)
            plt.xlabel("X")
            plt.ylabel("Y")
            plt.title("Tous les carrés")
    print("En tout il y'a ",o,"carré")
    plt.show()

def Rectangle(B):
        x=[]
        y=[]
        E=[]
        m=0
        E=list(combinations(B,4))
        for i in range(len(E)):
            AB=sqrt((E[i][1][0]-E[i][0][0])**2+(E[i][1][1]-E[i][0][1])**2)
            AD=sqrt((E[i][3][0]-E[i][0][0])**2+(E[i][3][1]-E[i][0][1])**2)
            BC=sqrt((E[i][2][0]-E[i][1][0])**2+(E[i][2][1]-E[i][1][1])**2)
            CD=sqrt((E[i][3][0]-E[i][2][0])**2+(E[i][3][1]-E[i][2][1])**2)
            xAB=(E[i][1][0]-E[i][0][0])
            yAB=(E[i][1][1]-E[i][0][1])
            xBC=(E[i][2][0]-E[i][1][0])
            yBC=(E[i][2][1]-E[i][1][1])
            #toujours le produit scalaire pour determiner s'il ya un angle droit
            PABBC=((xAB)*(xBC))+((yAB)*(yBC))
            if(AB==CD) and (AD==BC) and (AB!=BC) and (PABBC==0):
                m=m+1
                x=[E[i][0][0],E[i][1][0],E[i][2][0],E[i][3][0],E[i][0][0]]
                y=[E[i][0][1],E[i][1][1],E[i][2][1],E[i][3][1],E[i][0][1]]
                plt.plot(x,y)
                plt.xlabel("X")
                plt.ylabel("Y")
                plt.title("Tous les rectangles")
        print("Il ya",m,"rectangle")
        plt.show()

def TriangleR(B):
    x=[]
    y=[]
    E=[]
    v=0
    #combinaisons de 3 car un triangle rectangke n'a que 3 cotés et donc trois points relié entre eux
    E=list(combinations(B,3))
    for i in range(len(E)):
        AB=sqrt((E[i][1][0]-E[i][0][0])**2+(E[i][1][1]-E[i][0][1])**2)
        AC=sqrt((E[i][2][0]-E[i][0][0])**2+(E[i][2][1]-E[i][0][1])**2)
        BC=sqrt((E[i][2][0]-E[i][1][0])**2+(E[i][2][1]-E[i][1][1])**2)
        h=[AB,AC,BC]
        h.sort()
        # Ajout de sécurités pour vérifier que les points ne sont pas alignés

        # Calcul de l'hypoténuse noté h
        if  h[2]**2==h[0]**2+h[1]**2 :
            v=v+1
            x=[E[i][0][0],E[i][1][0],E[i][2][0],E[i][0][0]]
            y=[E[i][0][1],E[i][1][1],E[i][2][1],E[i][0][1]]
            plt.plot(x,y)
            plt.xlabel("X")
            plt.ylabel("Y")
            plt.title("Tous les triangles rectangles")
    print("Il ya ",v,"triangle rectangle")
    plt.show()
def Triangle_R_Iso(B):
    x=[]
    y=[]
    E=[]
    v=0
    E=list(combinations(B,3))
    for i in range(len(E)):
        AB=sqrt((E[i][1][0]-E[i][0][0])**2+(E[i][1][1]-E[i][0][1])**2)
        AC=sqrt((E[i][2][0]-E[i][0][0])**2+(E[i][2][1]-E[i][0][1])**2)
        BC=sqrt((E[i][2][0]-E[i][1][0])**2+(E[i][2][1]-E[i][1][1])**2)
        h=[AB,AC,BC]
        h.sort()
        if  h[2]**2==h[0]**2+h[1]**2 and h[0]==h[1] and h[2]!=h[0]:
            v=v+1
            x=[E[i][0][0],E[i][1][0],E[i][2][0],E[i][0][0]]
            y=[E[i][0][1],E[i][1][1],E[i][2][1],E[i][0][1]]
            plt.plot(x,y)
    print("Il ya",v,"triangle rectangle isocele")
    plt.show()
def Triangle_Iso(B):
    x=[]
    y=[]
    E=[]
    v=0
    E=list(combinations(B,3))
    for i in range(len(E)):
        AB=sqrt((E[i][1][0]-E[i][0][0])**2+(E[i][1][1]-E[i][0][1])**2)
        AC=sqrt((E[i][2][0]-E[i][0][0])**2+(E[i][2][1]-E[i][0][1])**2)
        BC=sqrt((E[i][2][0]-E[i][1][0])**2+(E[i][2][1]-E[i][1][1])**2)
        if (AB==AC and BC!=AB) or (AB==BC and AC!=BC) or (AC==BC) :
            v=v+1
            plt.plot(x,y)
            plt.xlabel("X")
            plt.ylabel("Y")
            plt.title("Tous les triangles isocele")
    print("il y'a",v,"Triangle Isocele")
    plt.show()
def Triangle_Equi(B):
    x=[]
    y=[]
    E=[]
    v=0
    E=list(combinations(B,3))
    for i in range(len(E)):
        AB=sqrt((E[i][1][0]-E[i][0][0])**2+(E[i][1][1]-E[i][0][1])**2)
        AC=sqrt((E[i][2][0]-E[i][0][0])**2+(E[i][2][1]-E[i][0][1])**2)
        BC=sqrt((E[i][2][0]-E[i][1][0])**2+(E[i][2][1]-E[i][1][1])**2)
        if  (AB==BC==AC):
            x=[E[i][0][0],E[i][1][0],E[i][2][0],E[i][0][0]]
            y=[E[i][0][1],E[i][1][1],E[i][2][1],E[i][0][1]]
            plt.plot(x,y)
            plt.xlabel("X")
            plt.ylabel("Y")
            plt.title("Tous les triangles equilatéral")
    print("Il ya" ,v," triangle equilatéral")
    plt.show()

def Parallelogramme(B):
    A=[]
    D=[]
    x=[]
    y=[]
    S=[]
    A=list(combinations(B, 4))
    for i in range(len(A)):
        if (((A[i][0][0]),(A[i][0][1])) != ((A[i][1][0]), (A[i][1][1])) != ((A[i][2][0]), (A[i][2][1])) != (
        (A[i][3][0]), (A[i][3][1])) != ((A[i][0][0]), (A[i][0][1]))):
            AB = sqrt(((A[i][1][0] - A[i][0][0]) ** 2) + ((A[i][1][1] - A[i][0][1]) ** 2))
            AD = sqrt(((A[i][3][0] - A[i][0][0]) ** 2) + ((A[i][3][1] - A[i][0][1]) ** 2))
            BC = sqrt(((A[i][2][0] - A[i][1][0]) ** 2) + ((A[i][2][1] - A[i][1][1]) ** 2))
            CD = sqrt(((A[i][3][0] - A[i][2][0]) ** 2) + ((A[i][3][1] - A[i][2][1]) ** 2))
            if AB == CD and BC == AD:
                S.append("c'est un parallelogramme ")
                x = [A[i][0][0], A[i][1][0], A[i][2][0], A[i][3][0], A[i][0][0]]
                y = [A[i][0][1], A[i][1][1], A[i][2][1], A[i][3][1], A[i][0][1]]
                plt.plot(x, y)
                plt.scatter(x, y)
                plt.xlabel("X")
                plt.ylabel("Y")
                plt.title("parallellogramme")
    n=0
    for i in range (len(S)):
        n=n+1
    print("il y'a",(n),"parallélogrammes")
    plt.show()

def losange(B):
    x=[]
    y=[]
    E=[]
    v=1
    E=list(combinations(B,4))
    for i in range(len(E)):
        if (((E[i][0][0]),(E[i][0][1])) != ((E[i][1][0]), (E[i][1][1])) != ((E[i][2][0]), (E[i][2][1])) != (
        (E[i][3][0]), (E[i][3][1])) != ((E[i][0][0]), (E[i][0][1]))):
        #Les distances
            AB=sqrt((E[i][1][0]-E[i][0][0])**2+(E[i][1][1]-E[i][0][1])**2)
            AD=sqrt((E[i][3][0]-E[i][0][0])**2+(E[i][3][1]-E[i][0][1])**2)
            BC=sqrt((E[i][2][0]-E[i][1][0])**2+(E[i][2][1]-E[i][1][1])**2)
            CD=sqrt((E[i][3][0]-E[i][2][0])**2+(E[i][3][1]-E[i][2][1])**2)
            AC=sqrt((E[i][2][0]-E[i][0][0])**2+(E[i][2][1]-E[i][0][1])**2)
            BD=sqrt((E[i][3][0]-E[i][1][0])**2+(E[i][3][1]-E[i][1][1])**2)
            #produit scalaire entre AB et BC afin s'ils sont perpendiculaire et qu'il ya un angle droit
            xAB=(E[i][1][0]-E[i][0][0])
            yAB=(E[i][1][1]-E[i][0][1])
            xBC=(E[i][2][0]-E[i][1][0])
            yBC=(E[i][2][1]-E[i][1][1])
            k=((xAB)*(xBC))+((yAB)*(yBC))
            #Le point E determine l'intersection des diagonales AC et BD
            #La distance BE est égale a la dsitance de la diagonale BD divisé par deux
            BE=(BD)/2
            #La distances AE est égale a la distance de la diagonale AC divisé par deux
            AE=(AC)/2
            #formule pour reconnaitre un parrallelograme
            for i in range (len(E)):
                if (((E[i][0][0]),(E[i][0][1])) != ((E[i][1][0]), (E[i][1][1])) != ((E[i][2][0]), (E[i][2][1])) != (
        (E[i][3][0]), (E[i][3][1])) != ((E[i][0][0]), (E[i][0][1]))):
                    if (AC**2+BD**2)==2*(AB**2+BC**2) and ((BE)!=(AE)) and (k!=0):
                        v=v+1
                        x=[E[i][0][0],E[i][1][0],E[i][2][0],E[i][3][0],E[i][0][0]]
                        y=[E[i][0][1],E[i][1][1],E[i][2][1],E[i][3][1],E[i][0][1]]
                        plt.plot(x,y)
                        plt.xlabel("X")
                        plt.ylabel("Y")
                        plt.title("Tous les losanges")
        print("Il y'a",v," losange")
        plt.show() 

princip(losange)
