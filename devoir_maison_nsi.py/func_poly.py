# Créé par ioana, le 14/02/2023 en Python 3.7
from itertools import*
from math import*
import  matplotlib.pyplot as plt
def tri(A):
    '''Calcul des distances
    AB = int(A[1][0])-int(A[0][0])**2+int(A[1][1])-int(A[0][1])**2
    BC = int(A[2][0])-int(A[1][0])**2+int(A[2][1])-int(A[1][1])**2
    AC = int(A[2][0])-int(A[0][0])**2+int(A[2][1])-int(A[0][1])**2


    if  (int(AB**2))==(int(AC**2))+(int(BC**2)):
      return {"Triangle rectangle":True}

    elif (int(AC**2))==(int(AB**2))+(int(BC**2)):
      return {"Triangle rectangle":True}

    elif (int(AC**2))==(int(AB**2))+(int(BC**2)):
      return {"Triangle rectangle":True}

    else:
      return {"triangle rectangle":False}'''

    if (AB==BC==BC):
        return False
    elif (maxi==AB):
        if (int(AB**2))==(int(AC**2))+(int(AB**2)):
            return {"Triangle rectangle":True}

    elif (maxi== AC):
        if (int(AC**2))==(int(AB**2))+(int(BC**2)):
          return {"Triangle rectangle":True}

    elif (maxi==BC):
        if (int(BC**2))==(int(AB**2))+(int(AC**2)):
          return {"Triangle rectangle":True}

    else:
        return {"triangle rectangle":False}

'''def tri(A):
    ''''''Vérifie si un triangle défini par des points est rectangle''''''
    AB = ((int(A[1][0]) - int(A[0][0]))**2 + (int(A[1][1]) - (int(A[0][1]))**2)
    BC = ((int(A[2][0]) - int(A[1][0]))**2 + (int(A[2][1]) - (int(A[1][1]))**2)
    AC = ((A[2][0] - A[0][0])**2 + (A[2][1] - A[0][1])**2)
    sorted_distances = sorted([AB, BC, AC])
    if abs(sorted_distances[0] + sorted_distances[1] - sorted_distances[2]) < 1e-9:
        return True
    else:
        return False'''



def carré(A):
    '''Calcul de distances'''
    AB = sqrt((((A[1][0])-(A[0][0]))**2)+(((A[1][1])-(A[0][1]))**2))
    AD = sqrt((((A[3][0])-(A[0][0]))**2)+(((A[3][1])-(A[0][1]))**2))
    DC = sqrt((((A[2][0])-(A[3][0]))**2)+(((A[2][1])-(A[3][1]))**2))
    BC = sqrt((((A[2][0])-(A[1][0]))**2)+(((A[2][1])-(A[1][1]))**2))
    VAB = [int(A[2][0])-int(A[0][0]), int(A[2][1])-int(A[0][1])]
    VAD = [int(A[3][0])-int(A[0][0]), int(A[3][1])-int(A[0][1])]
    VEC = VAB[0] * VAD[0] + VAB[1] * VAD[1]
    if (AB==BC==DC==AD) and (VEC==0):
         return {"carré":True}
    else:
         return {"carré":False}

def rec(A):
    '''Calcul des distances'''
    print(A[0],A[1])
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
    A=[]
    for i in range (1,(len(lignes))):
        li=lignes[i]
        Y=li.split(";")
        P.append([Y[0],Y[1]])
    for i in range(len(P)):
        a=float(P[i][0])
        b=float(P[i][1])
        A.append([a,b])
        plt.scatter(a,b,c="purple")
    plt.show()
    carré(A)
    print(H)

def polygone():
    Z=[]
    fil=open("C:\\Users\\ioana\\Desktop\\nsi\\ann-e-sco-2022-2023\\devoir_maison_nsi.py\\mano_test.csv","r")
    lignes=fil.readlines()
    for i in lignes:
        i=i.rstrip()
        i=i.split(";")
        Z.append(i)
    print(Z)
    fil.close()

    n_tri_rec=list(combinations(Z, 3))
    for combination in n_tri_rec:
         if tri(combination):
             print("Triangle rectangle dans le nuage de points :", combination)
             x = [int(combination[0][0]), int(combination[1][0]), int(combination[2][0]), int(combination[0][0])]
             y = [int(combination[0][1]), int(combination[1][1]), int(combination[2][1]), int(combination[0][1])]
             print(n_tri_rec)
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

'''def main():
    window = tk.Tk()
    window.title("Analyse de nuages de points")

    title_label = tk.Label(window, text="Analyse de nuages de points", font=("Arial", 16))
    title_label.pack(pady=10)

    polygone_button = tk.Button(window, text="Trouver les polygones", command=polygone)
    polygone_button.pack(pady=10)

    nuagedepts_button = tk.Button(window, text="Afficher le nuage de points", command=nuagedepts)
    nuagedepts_button.pack(pady=10)

    quit_button = tk.Button(window, text="Quitter", command=window.quit)
    quit_button.pack(pady=10)

    window.mainloop()

    if __name__ == "__main__":
     main()'''

'''import tkinter as tk
from tkinter import ttk

def main():
    window = tk.Tk()
    window.title("Analyse de nuages de points")
    window.geometry("300x300")
    window.configure(bg="#FFFFFF")

    title_label = tk.Label(
        window,
        text="Analyse de nuages de points",
        font=("Arial", 16),
        bg="#FFFFFF",
        fg="#000000",
    )
    title_label.pack(pady=20)

    style = ttk.Style()
    style.configure(
        "TButton",
        font=("Arial", 12),
        bg="#FFFFFF",
        fg="#000000",
        relief="flat",
        padding=5,
    )
    style.map("TButton", background=[("active", "#BBBBBB")])

    polygone_button = ttk.Button(window, text="Trouver les polygones", command=polygone)
    polygone_button.pack(pady=10)

    nuagedepts_button = ttk.Button(window, text="Afficher le nuage de points", command=nuagedepts)
    nuagedepts_button.pack(pady=10)

    quit_button = ttk.Button(window, text="Quitter", command=window.quit)
    quit_button.pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    main()'''



