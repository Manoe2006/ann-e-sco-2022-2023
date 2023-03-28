from itertools import combinations
from math import sqrt
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt


def distance(pt1, pt2):
    """Calcule la distance entre deux points."""
    return sqrt((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)


def est_carre(points):
    """Vérifie si les quatre points donnés forment un carré."""
    if len(set(tuple(pt) for pt in points)) != 4:
        raise ValueError("Les points ne forment pas un carré : certains sont confondus.")

    AB = distance(points[0], points[1])
    BC = distance(points[1], points[2])
    CD = distance(points[2], points[3])
    DA = distance(points[3], points[0])
    AC = distance(points[0], points[2])
    BD = distance(points[1], points[3])

    if AB == BC == CD == DA and AC == BD:
        return True
    else:
        return False


def est_rectangle(points):
    """Vérifie si les quatre points donnés forment un rectangle."""

    if len(set(tuple(pt) for pt in points)) != 4:
        return False  # Ignorer les rectangles avec des points confondus

    AB = distance(points[0], points[1])
    BC = distance(points[1], points[2])
    CD = distance(points[2], points[3])
    DA = distance(points[3], points[0])

    diagonal1 = distance(points[0], points[2])
    diagonal2 = distance(points[1], points[3])

    if (AB == DA and BC == CD and diagonal1 == diagonal2) or (AB == BC and CD == DA and diagonal1 == diagonal2):
        return True
    else:
        return False


def est_triangle_rectangle(points):
    """Vérifie si les trois points donnés forment un triangle rectangle."""

    if len(set(tuple(pt) for pt in points)) != 3:
        return False  # Ignorer les triangles avec des points confondus

    def distance(pt1, pt2):
        return ((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)

    cotes = [distance(points[0], points[1]), distance(points[1], points[2]), distance(points[0], points[2])]
    cotes.sort()

    if cotes[0] + cotes[1] == cotes[2]:
        return True
    else:
        return False

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
    print(H)

def polygone():
    Z = []
    fil=open("C:\\Users\\ioana\\Desktop\\nsi\\ann-e-sco-2022-2023\\devoir_maison_nsi.py\\mano_test.csv","r")
    lignes = fil.readlines()
    for i in lignes:
        i = i.rstrip()
        i = i.split(";")
        Z.append((float(i[0]), float(i[1])))
    print(Z)
    fil.close()

    n_tri_rec=list(combinations(Z, 3))
    for combination in n_tri_rec:
         if est_triangle_rectangle(combination):
             print("Triangle rectangle dans le nuage de points :", combination)
             x = [int(combination[0][0]), int(combination[1][0]), int(combination[2][0]), int(combination[0][0])]
             y = [int(combination[0][1]), int(combination[1][1]), int(combination[2][1]), int(combination[0][1])]
             print(n_tri_rec)
             plt.scatter(x, y, color="green")
             plt.plot(x, y)
    plt.title("Triangle(s) rectangle(s)")
    plt.show()

    n_carre=list(combinations(Z,4))
    for combination in n_carre:
        if est_carre(combination):
             print("Carré dans le nuage de points :", combination)
             x = [int(combination[0][0]), int(combination[1][0]), int(combination[2][0]), int(combination[0][0])]
             y = [int(combination[0][1]), int(combination[1][1]), int(combination[2][1]), int(combination[0][1])]

             plt.scatter(x, y, color="green")
             plt.plot(x, y)
    plt.title("Carré(s)")
    plt.show()



    n_rectangle=list(combinations(Z,4))
    for combination in n_rectangle:
        if est_rectangle(combination):
             print("rectangles dans le nuage de points:",combination)
             x = [int(combination[0][0]), int(combination[1][0]), int(combination[2][0]), int(combination[0][0])]
             y = [int(combination[0][1]), int(combination[1][1]), int(combination[2][1]), int(combination[0][1])]
             plt.scatter(x,y, color="green")
             plt.plot(x,y)
    plt.title("Rectangle(s)")
    plt.show()




from tkinter import filedialog

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        file_path_label.config(text=file_path)

def analyze_points():
    file_path = file_path_label.cget("text")
    if file_path:
        nuagedepts()
        polygone()
    else:
        result_label.config(text="Veuillez sélectionner un fichier CSV.")

def main():
    global file_path_label, result_label

    window = tk.Tk()
    window.title("Analyse de nuages de points")

    title_label = tk.Label(window, text="Analyse de nuages de points", font=("Arial", 16))
    title_label.pack(pady=10)

    browse_button = tk.Button(window, text="Parcourir", command=browse_file)
    browse_button.pack(pady=10)

    file_path_label = tk.Label(window, text="", wraplength=400)
    file_path_label.pack(pady=10)

    analyze_button = tk.Button(window, text="Analyser les points", command=analyze_points)
    analyze_button.pack(pady=10)

    result_label = tk.Label(window, text="", wraplength=400)
    result_label.pack(pady=10)

    quit_button = tk.Button(window, text="Quitter", command=window.quit)
    quit_button.pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    main()
