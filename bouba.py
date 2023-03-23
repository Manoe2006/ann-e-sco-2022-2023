# Créé par hicha, le 17/01/2023 en Python 3.4
from math import sqrt
from itertools import*
import matplotlib.pyplot as plt
from six.moves import input as raw_input
from tkinter import*
def quadrilatere(B):
    A=[]
    GS=[]
    x=[]
    y=[]
    A=list(combinations(B,4))
    for i in range(len(A)):
        if(((A[i][0][0]),(A[i][0][1]))!=((A[i][1][0]),(A[i][1][1]))!=((A[i][2][0]),(A[i][2][1]))!=((A[i][3][0]),(A[i][3][1]))!=((A[i][0][0]),(A[i][0][1]))):
            disAB=sqrt(((A[i][1][0]-A[i][0][0])**2)+((A[i][1][1]-A[i][0][1])**2))
            disAD=sqrt(((A[i][3][0]-A[i][0][0])**2)+((A[i][3][1]-A[i][0][1])**2))
            disBC=sqrt(((A[i][2][0]-A[i][1][0])**2)+((A[i][2][1]-A[i][1][1])**2))
            disCD=sqrt(((A[i][3][0]-A[i][2][0])**2)+((A[i][3][1]-A[i][2][1])**2))
            VAB=A[i][1][0]-A[i][0][0],A[i][1][1]-A[i][0][1]
            VAD=A[i][3][0]-A[i][0][0],A[i][3][1]-A[i][0][1]
            vecteur=VAB[0]*VAD[0]+VAB[1]*VAD[1]
            if disAB==disAD==disBC==disCD and vecteur==0:
                GS.append("c'est un carré ")
                x=[A[i][0][0],A[i][1][0],A[i][2][0],A[i][3][0],A[i][0][0]]
                y=[A[i][0][1],A[i][1][1],A[i][2][1],A[i][3][1],A[i][0][1]]
                plt.plot(x,y)
                plt.scatter(x,y)
                plt.xlabel("X")
                plt.ylabel("Y")
                plt.title("quadrilatere")
            if disAB==disAD==disBC==disCD and vecteur!=0:
                GS.append("c'est un losange ")
                x=[A[i][0][0],A[i][1][0],A[i][2][0],A[i][3][0],A[i][0][0]]
                y=[A[i][0][1],A[i][1][1],A[i][2][1],A[i][3][1],A[i][0][1]]
                plt.plot(x,y)
                plt.scatter(x,y)
            if disAB==disCD!=disAD==disBC and vecteur==0:
                GS.append("c'est un rectangle")
            if disAB == disCD and disBC == disAD:
                GS.append("c'est un parallelogramme ")
                x = [A[i][0][0], A[i][1][0], A[i][2][0], A[i][3][0], A[i][0][0]]
                y = [A[i][0][1], A[i][1][1], A[i][2][1], A[i][3][1], A[i][0][1]]
                plt.plot(x, y)
                plt.scatter(x, y)
    plt.show()
    n=0
    for i in range (len(GS)):
        n=n+1
    print("il y'a",(n),"quadrilatères")
    for i in range (len(GS)):
            print(GS[i])
def carre(B):
    A=[]
    GS=[]
    x=[]
    y=[]
    A=list(combinations(B,4))
    for i in range(len(A)):
        if(((A[i][0][0]),(A[i][0][1]))!=((A[i][1][0]),(A[i][1][1]))!=((A[i][2][0]),(A[i][2][1]))!=((A[i][3][0]),(A[i][3][1]))!=((A[i][0][0]),(A[i][0][1]))):
            disAB=sqrt(((A[i][1][0]-A[i][0][0])**2)+((A[i][1][1]-A[i][0][1])**2))
            disAD=sqrt(((A[i][3][0]-A[i][0][0])**2)+((A[i][3][1]-A[i][0][1])**2))
            disBC=sqrt(((A[i][2][0]-A[i][1][0])**2)+((A[i][2][1]-A[i][1][1])**2))
            disCD=sqrt(((A[i][3][0]-A[i][2][0])**2)+((A[i][3][1]-A[i][2][1])**2))
            VAB=A[i][1][0]-A[i][0][0],A[i][1][1]-A[i][0][1]
            VAD=A[i][3][0]-A[i][0][0],A[i][3][1]-A[i][0][1]
            vecteur=VAB[0]*VAD[0]+VAB[1]*VAD[1]
            if disAB==disAD==disBC==disCD and vecteur==0:
                GS.append(("c'est un carré avec pour coordonnées sous forme(x,y):",(A[i][0][0],A[i][0][1]),(A[i][1][0],A[i][1][1]),(A[i][2][0],A[i][2][1]),(A[i][3][0],A[i][3][1])))
                x=[A[i][0][0],A[i][1][0],A[i][2][0],A[i][3][0],A[i][0][0]]
                y=[A[i][0][1],A[i][1][1],A[i][2][1],A[i][3][1],A[i][0][1]]
                plt.plot(x,y)
                plt.scatter(x,y)
                plt.xlabel("X")
                plt.ylabel("Y")
                plt.title("quadrilatere")
    plt.show()
    n=0
    for i in range (len(GS)):
        n=n+1
    print("il y'a",(n),"carrés")
    for i in range (len(GS)):
        print(GS[i])
def rectangle(B):
    A=[]
    GS=[]
    x=[]
    y=[]
    A=list(combinations(B,4))
    for i in range(len(A)):
        if(((A[i][0][0]),(A[i][0][1]))!=((A[i][1][0]),(A[i][1][1]))!=((A[i][2][0]),(A[i][2][1]))!=((A[i][3][0]),(A[i][3][1]))!=((A[i][0][0]),(A[i][0][1]))):
            disAB=sqrt(((A[i][1][0]-A[i][0][0])**2)+((A[i][1][1]-A[i][0][1])**2))
            disAD=sqrt(((A[i][3][0]-A[i][0][0])**2)+((A[i][3][1]-A[i][0][1])**2))
            disBC=sqrt(((A[i][2][0]-A[i][1][0])**2)+((A[i][2][1]-A[i][1][1])**2))
            disCD=sqrt(((A[i][3][0]-A[i][2][0])**2)+((A[i][3][1]-A[i][2][1])**2))
            VAB=A[i][1][0]-A[i][0][0],A[i][1][1]-A[i][0][1]
            VAD=A[i][3][0]-A[i][0][0],A[i][3][1]-A[i][0][1]
            vecteur=VAB[0]*VAD[0]+VAB[1]*VAD[1]
            if disAB==disCD!=disBC==disAD and vecteur==0:
                GS.append(("c'est un rectangle avec pour coordonnées sous forme(x,y):",(A[i][0][0],A[i][0][1]),(A[i][1][0],A[i][1][1]),(A[i][2][0],A[i][2][1]),(A[i][3][0],A[i][3][1])))
                x=[A[i][0][0],A[i][1][0],A[i][2][0],A[i][3][0],A[i][0][0]]
                y=[A[i][0][1],A[i][1][1],A[i][2][1],A[i][3][1],A[i][0][1]]
                plt.plot(x,y)
                plt.scatter(x,y)
                plt.xlabel("X")
                plt.ylabel("Y")
                plt.title("rectangles")
    plt.show()
    n=0
    for i in range (len(GS)):
        n=n+1
    print("il y'a",(n),"rectangles")
    for i in range (len(GS)):
        print(GS[i])

def losange(B):
    A=[]
    GS=[]
    x=[]
    y=[]
    A=list(combinations(B,4))
    for i in range(len(A)):
        if(((A[i][0][0]),(A[i][0][1]))!=((A[i][1][0]),(A[i][1][1]))!=((A[i][2][0]),(A[i][2][1]))!=((A[i][3][0]),(A[i][3][1]))!=((A[i][0][0]),(A[i][0][1]))):
            disAB=sqrt(((A[i][1][0]-A[i][0][0])**2)+((A[i][1][1]-A[i][0][1])**2))
            disAD=sqrt(((A[i][3][0]-A[i][0][0])**2)+((A[i][3][1]-A[i][0][1])**2))
            disBC=sqrt(((A[i][2][0]-A[i][1][0])**2)+((A[i][2][1]-A[i][1][1])**2))
            disCD=sqrt(((A[i][3][0]-A[i][2][0])**2)+((A[i][3][1]-A[i][2][1])**2))
            VAB=A[i][1][0]-A[i][0][0],A[i][1][1]-A[i][0][1]
            VAD=A[i][3][0]-A[i][0][0],A[i][3][1]-A[i][0][1]
            vecteur=VAB[0]*VAD[0]+VAB[1]*VAD[1]
            if disAB==disAD==disBC==disCD and vecteur!=0:
                GS.append("c'est un losange ")
                x=[A[i][0][0],A[i][1][0],A[i][2][0],A[i][3][0],A[i][0][0]]
                y=[A[i][0][1],A[i][1][1],A[i][2][1],A[i][3][1],A[i][0][1]]
                plt.plot(x,y)
                plt.scatter(x,y)
                plt.xlabel("X")
                plt.ylabel("Y")
                plt.title("quadrilatere")
    plt.show()
    n=0
    for i in range (len(GS)):
        n=n+1
    print("il y'a",(n),"losanges")
    for i in range (len(GS)):
        print(GS[i])

def parallelogramme(B):
    A = []
    GS = []
    x = []
    y = []
    A = list(combinations(B, 4))
    for i in range(len(A)):
        if (((A[i][0][0]), (A[i][0][1])) != ((A[i][1][0]), (A[i][1][1])) != ((A[i][2][0]), (A[i][2][1])) != (
        (A[i][3][0]), (A[i][3][1])) != ((A[i][0][0]), (A[i][0][1]))):
            disAB = sqrt(((A[i][1][0] - A[i][0][0]) ** 2) + ((A[i][1][1] - A[i][0][1]) ** 2))
            disAD = sqrt(((A[i][3][0] - A[i][0][0]) ** 2) + ((A[i][3][1] - A[i][0][1]) ** 2))
            disBC = sqrt(((A[i][2][0] - A[i][1][0]) ** 2) + ((A[i][2][1] - A[i][1][1]) ** 2))
            disCD = sqrt(((A[i][3][0] - A[i][2][0]) ** 2) + ((A[i][3][1] - A[i][2][1]) ** 2))
            if disAB == disCD and disBC == disAD:
                GS.append("c'est un parallelogramme ")
                x = [A[i][0][0], A[i][1][0], A[i][2][0], A[i][3][0], A[i][0][0]]
                y = [A[i][0][1], A[i][1][1], A[i][2][1], A[i][3][1], A[i][0][1]]
                plt.plot(x, y)
                plt.scatter(x, y)
                plt.xlabel("X")
                plt.ylabel("Y")
                plt.title("parallellogramme")
    n=0
    for i in range (len(GS)):
        n=n+1
    print("il y'a",(n),"parallélogrammes")
    for i in range (len(GS)):
        print(GS[i])
    plt.show()

def triangle(B):
    A=[]
    GS=[]
    x=[]
    y=[]
    A=list(combinations(B,3))
    for i in range(len(A)):
        if((A[i][0][0]!=A[i][1][0])or(A[i][0][1]!=A[i][1][1]))and((A[i][1][0]!=A[i][2][0])or(A[i][1][1]!=A[i][2][1]))and((A[i][2][0]!=A[i][0][0])or(A[i][2][1]!=A[i][0][1])):
            disAB=sqrt(((A[i][1][0]-A[i][0][0])**2)+((A[i][1][1]-A[i][0][1])**2))
            disAC=sqrt(((A[i][2][0]-A[i][0][0])**2)+((A[i][2][1]-A[i][0][1])**2))
            disBC=sqrt(((A[i][2][0]-A[i][1][0])**2)+((A[i][2][1]-A[i][1][1])**2))
            liste=[disAB,disAC,disBC]
            liste.sort()
            if int(liste[2]**2)==int((liste[1]**2)+(liste[0]**2)):
                GS.append(("triangle rectangle avec pour coordonnées sous forme (x,y):",(A[i][0][0],A[i][0][1]),(A[i][1][0],A[i][1][1]),(A[i][2][0],A[i][2][1])))
                x=[A[i][0][0],A[i][1][0],A[i][2][0],A[i][0][0]]
                y=[A[i][0][1],A[i][1][1],A[i][2][1],A[i][0][1]]
                plt.plot(x,y)
                plt.scatter(x,y)
                plt.xlabel("X")
                plt.ylabel("Y")
                plt.title("triangle")
            elif int(disAB==disAC==disBC==disAB):
                GS.append("cest un triangle équilatéral")
            elif disAB==disAC or disAC==disBC or disAB==disBC:
                GS.append(("triangle isocèle avec pour coordonnées sous forme (x,y):",(A[i][0][0],A[i][0][1]),(A[i][1][0],A[i][1][1]),(A[i][2][0],A[i][2][1])))
                x=[A[i][0][0],A[i][1][0],A[i][2][0],A[i][0][0]]
                y=[A[i][0][1],A[i][1][1],A[i][2][1],A[i][0][1]]
                plt.plot(x,y)
                plt.scatter(x,y)
    plt.show()
    n=0
    for i in range (len(GS)):
        n=n+1
    print("il y'a",(n),"triangles")
    for i in range (len(GS)):
        print(GS[i])

def trirec(B):
    A=[]
    GS=[]
    x=[]
    y=[]
    A=list(combinations(B,3))
    for i in range(len(A)):
        if((A[i][0][0]!=A[i][1][0])or(A[i][0][1]!=A[i][1][1]))and((A[i][1][0]!=A[i][2][0])or(A[i][1][1]!=A[i][2][1]))and((A[i][2][0]!=A[i][0][0])or(A[i][2][1]!=A[i][0][1])):
            disAB=sqrt(((A[i][1][0]-A[i][0][0])**2)+((A[i][1][1]-A[i][0][1])**2))
            disAC=sqrt(((A[i][2][0]-A[i][0][0])**2)+((A[i][2][1]-A[i][0][1])**2))
            disBC=sqrt(((A[i][2][0]-A[i][1][0])**2)+((A[i][2][1]-A[i][1][1])**2))
            liste=[disAB,disAC,disBC]
            liste.sort()
            if int(liste[2]**2)==int((liste[1]**2)+(liste[0]**2)):
                GS.append(("triangle rectangle avec pour coordonnées sous forme (x,y):",(A[i][0][0],A[i][0][1]),(A[i][1][0],A[i][1][1]),(A[i][2][0],A[i][2][1])))
                x=[A[i][0][0],A[i][1][0],A[i][2][0],A[i][0][0]]
                y=[A[i][0][1],A[i][1][1],A[i][2][1],A[i][0][1]]
                plt.plot(x,y)
                plt.scatter(x,y)
                plt.xlabel("X")
                plt.ylabel("Y")
                plt.title("Triangles rectangles")
    plt.show()
    n=0
    for i in range (len(GS)):
        n=n+1
    print("il y'a",(n),"triangle rectangle")
    for i in range (len(GS)):
        print(GS[i])

def triequi(B):
    A=[]
    GS=[]
    x=[]
    y=[]
    A=list(combinations(B,3))
    for i in range(len(A)):
        if((A[i][0][0]!=A[i][1][0])or(A[i][0][1]!=A[i][1][1]))and((A[i][1][0]!=A[i][2][0])or(A[i][1][1]!=A[i][2][1]))and((A[i][2][0]!=A[i][0][0])or(A[i][2][1]!=A[i][0][1])):
            disAB=sqrt(((A[i][1][0]-A[i][0][0])**2)+((A[i][1][1]-A[i][0][1])**2))
            disAC=sqrt(((A[i][2][0]-A[i][0][0])**2)+((A[i][2][1]-A[i][0][1])**2))
            disBC=sqrt(((A[i][2][0]-A[i][1][0])**2)+((A[i][2][1]-A[i][1][1])**2))
            liste=[disAB,disAC,disBC]
            liste.sort
            if int(disAB==disAC==disBC==disAB):
                GS.append(("triangle équilatéral avec pour coordonnées sous forme (x,y):",(A[i][0][0],A[i][0][1]),(A[i][1][0],A[i][1][1]),(A[i][2][0],A[i][2][1])))
                x=[A[i][0][0],A[i][1][0],A[i][2][0],A[i][0][0]]
                y=[A[i][0][1],A[i][1][1],A[i][2][1],A[i][0][1]]
                plt.plot(x,y)
                plt.scatter(x,y)
                plt.xlabel("X")
                plt.ylabel("Y")
                plt.title("Triangles équilatéraux")
    plt.show()
    n=0
    for i in range (len(GS)):
        n=n+1
    print("il y'a",(n),"triangle équilatéraux")
    for i in range (len(GS)):
        print(GS[i])

def triso(B):
    A=[]
    GS=[]
    x=[]
    y=[]
    A=list(combinations(B,3))
    for i in range(len(A)):
        if((A[i][0][0]!=A[i][1][0])or(A[i][0][1]!=A[i][1][1]))and((A[i][1][0]!=A[i][2][0])or(A[i][1][1]!=A[i][2][1]))and((A[i][2][0]!=A[i][0][0])or(A[i][2][1]!=A[i][0][1])):
            disAB=sqrt(((A[i][1][0]-A[i][0][0])**2)+((A[i][1][1]-A[i][0][1])**2))
            disAC=sqrt(((A[i][2][0]-A[i][0][0])**2)+((A[i][2][1]-A[i][0][1])**2))
            disBC=sqrt(((A[i][2][0]-A[i][1][0])**2)+((A[i][2][1]-A[i][1][1])**2))
            liste=[disAB,disAC,disBC]
            liste.sort
            if int(disAB==disAC or disAC==disBC or disAB==disBC):
                GS.append(("triangle isocèle avec pour coordonnées sous forme (x,y):",(A[i][0][0],A[i][0][1]),(A[i][1][0],A[i][1][1]),(A[i][2][0],A[i][2][1])))
                x=[A[i][0][0],A[i][1][0],A[i][2][0],A[i][0][0]]
                y=[A[i][0][1],A[i][1][1],A[i][2][1],A[i][0][1]]
                plt.plot(x,y)
                plt.scatter(x,y)
                plt.xlabel("X")
                plt.ylabel("Y")
                plt.title("triangles isocèles")
    plt.show()
    n=0
    for i in range (len(GS)):
        n=n+1
    print("il y'a",(n),"triangle isocèle")
    for i in range (len(GS)):
        print(GS[i])


def polygone(B):
    print(quadrilatere(B),triangle(B))
#ouverture du fichier et traitement des données
V=[]
f= open ("C:\\Users\\FAMILLE DIABY\\Downloads\\tester.csv","r")
lignes=f.readlines()
P=[]
B=[]
for i in range(1,(len(lignes))):
    li=lignes[i]
    V=li.split(";")
    P.append([V[0],V[1]])
for i in range(len(P)):
    s=float(P[i][0])
    k=float(P[i][1])
    B.append([s,k])
    plt.scatter(s,k,c='red')
x=[]
y=[]
for i in range(len(B)):
    x.append(B[i][0])
    y.append(B[i][1])
print(B)
#on cree la fenetre
fenetre=Tk()
#creation d'autres fenetres
def TRIPRINT():
    fenetretri=Toplevel(fenetre)
    fenetretri.title("Onglet triangle")
    fenetretri['bg']='#F2A961'
    fenetretri.geometry('1920x1080')
    fenetretri.resizable(height=FALSE,width=FALSE)
    label1=Label(fenetretri,text="Quels triangles recherchez-vous ? ",font=("Cascadia Code SemiBold",20),fg='#F48950',bg='#79301B')
    label1.place(x='100',y='50')
    Bou_trirec= Button(fenetretri, text="TRIANGLES RECTANGLES",font=("Cascadia Code SemiBold",18),fg='#79301B',bg='#F48950',command=lambda:trirec(B))
    Bou_trirec.place(x='400',y='300')
    Bou_triso= Button(fenetretri, text="TRIANGLES ISOCELES",font=("Cascadia Code SemiBold",18),fg='#79301B',bg='#F48950',command=lambda:triso(B))
    Bou_triso.place(x='1200',y='300')
    Bou_triequi= Button(fenetretri, text="TRIANGLES EQUILATERAUX",font=("Cascadia Code SemiBold",18),fg='#79301B',bg='#F48950',command=lambda:triequi(B))
    Bou_triequi.place(x='400',y='600')
    Bou_tout= Button(fenetretri, text="TOUS LES TRIANGLES",font=("Cascadia Code SemiBold",18),fg='#79301B',bg='#F48950',command=lambda:triangle(B))
    Bou_tout.place(x='1200',y='600')





def QUADRIPRINT():
    fenetrequadri=Toplevel(fenetre)
    fenetrequadri.title("Onglet Quadrilatere")
    fenetrequadri['bg']='#F2A961'
    fenetrequadri.geometry('1920x1080')
    fenetrequadri.resizable(height=FALSE,width=FALSE)
    label1=Label(fenetrequadri,text="Quels quadrilateres recherchez-vous ? ",font=("Cascadia Code SemiBold",23),fg='#F48950',bg='#79301B')
    label1.place(x='100',y='50')
    Bou_carre=Button(fenetrequadri, text=" CARRES ",font=("Cascadia Code SemiBold",20),fg='#79301B',bg='#F48950',command=lambda:carre(B))
    Bou_carre.place(x='600',y='300')
    Bou_losange=Button(fenetrequadri, text="LOSANGES",font=("Cascadia Code SemiBold",20),fg='#79301B',bg='#F48950',command=lambda:losange(B))
    Bou_losange.place(x='1000',y='300')
    Bou_rectangle=Button(fenetrequadri, text="RECTANGLES",font=("Cascadia Code SemiBold",20),fg='#79301B',bg='#F48950',command=lambda:losange(B))
    Bou_rectangle.place(x='400',y='500')
    Bou_parallelogramme=Button(fenetrequadri, text="PARALLELOGRAMMES",font=("Cascadia Code SemiBold",20),fg='#79301B',bg='#F48950',command=lambda:parallelogramme(B))
    Bou_parallelogramme.place(x='1200',y='500')
    Bou_tout=Button(fenetrequadri, text="TOUT LES QUADRILATERES",font=("Cascadia Code SemiBold",20),fg='#79301B',bg='#F48950',command=lambda:quadrilatere(B))
    Bou_tout.place(x='800',y='500')
def TOUTPRINT():
    #on la redimensionne
    fen=Toplevel(fenetre)
    fen.geometry('1920x1080')
    #on met le titre
    fen.title("Projet de nsi ")
    #on choist la couleur du background
    fen['bg']='#F2A961'
    #inscription pouour faire en sorte qu'il soit impossible de modifier la taille de l'ecran
    fen.resizable(height=FALSE,width=FALSE)

    #creation de differents boutons pour aller sur les autres pages
    Bou_tri= Button(fen, text="TRIANGLES",font=("Cascadia Code SemiBold",25),fg='#79301B',bg='#F48950',command=TRIPRINT)
    Bou_tri.place(x='300',y='500')
    Bou_quadri=Button(fen, text="QUADRILATERES",font=("Cascadia Code SemiBold",25),fg='#79301B',bg='#F48950',command=QUADRIPRINT)
    Bou_quadri.place(x='1200',y='500')
    Bou_tout=Button(fen, text="TOUTES LES FIGURES",font=("Cascadia Code SemiBold",25),fg='#79301B',bg='#F48950',command=lambda : polygone(B))
    Bou_tout.place(x='700',y='700')


def lancer():
    fenetre.geometry('1920x1080')
    #on met le titre
    fenetre.title("Projet de nsi ")
    #on choist la couleur du background
    fenetre['bg']='#F2A961'
    #inscription pouour faire en sorte qu'il soit impossible de modifier la taille de l'ecran
    fenetre.resizable(height=FALSE,width=FALSE)
    label1=Label(fenetre,text="Bienvenue sur mon programme qui nous permet de trouver des figures géométriques issus d'un nuage de points ",font=("Cascadia Code SemiBold",20),fg='#F48950',bg='#79301B')
    label1.place(x='100',y='50')
    BOU= Button(fenetre, text="lancer le programme avec un fichier excel",font=("Cascadia Code SemiBold",25),fg='#79301B',bg='#F48950',command=TOUTPRINT)
    BOU.place(x='500',y='500')
    BOU2= Button(fenetre, text="lancer le programme avec vos coordonnées",font=("Cascadia Code SemiBold",25),fg='#79301B',bg='#F48950',command=TOUTPRINT)
    BOU2.place(x='500',y='800')
    BOU3=Button(fenetre, text="Quitter",font=("Cascadia Code SemiBold",5),fg='#79301B',bg='#F48950',command=fermer_fenetre)
    BOU





def fermer_fenetre():
    fenetre.destroy()
    #on cree une boucle pour afficher la fenetre
    fenetre.mainloop()
