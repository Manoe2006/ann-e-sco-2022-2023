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
        return False  # Ignorer les carrés avec des points confondus

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

def polygone(shape_function):
    Z = []
    fil=open("C:\\Users\\ioana\\Desktop\\nsi\\ann-e-sco-2022-2023\\devoir_maison_nsi.py\\mano_test.csv","r")
    lignes = fil.readlines()
    for i in lignes:
        i = i.rstrip()
        i = i.split(";")
        Z.append((float(i[0]), float(i[1])))
    fil.close()

    if shape_function == est_carre:
        n_shapes = list(combinations(Z, 4))
        shape_name = "Carré(s)"
    elif shape_function == est_rectangle:
        n_shapes = list(combinations(Z, 4))
        shape_name = "Rectangle(s)"
    elif shape_function == est_triangle_rectangle:
        n_shapes = list(combinations(Z, 3))
        shape_name = "Triangle(s) rectangle(s)"

    for combination in n_shapes:
        if shape_function(combination):
            print(f"{shape_name[:-3]} dans le nuage de points :", combination)
            x = [point[0] for point in combination] + [combination[0][0]]
            y = [point[1] for point in combination] + [combination[0][1]]

            plt.scatter(x, y, color="green")
            plt.plot(x, y)

    plt.title(shape_name)
    plt.show()




from tkinter import filedialog

# Les fonctions distance, est_carre, est_rectangle, est_triangle_rectangle, nuagedepts et polygone restent les mêmes

# '''def browse_file():
#     file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
#     if file_path:
#         file_path_label.config(text=file_path)

# def analyze_points():
#     file_path = file_path_label.cget("text")
#     if file_path:
#         shape = shape_var.get()
#         if shape == "Nuage de points":
#             nuagedepts()
#         elif shape == "Carré":
#             polygone(est_carre)
#         elif shape == "Rectangle":
#             polygone(est_rectangle)
#         elif shape == "Triangle rectangle":
#             polygone(est_triangle_rectangle)
#     else:
#         result_label.config(text="Veuillez sélectionner un fichier CSV.")

# def main():
#     global file_path_label, result_label, shape_var

#     window = tk.Tk()
#     window.title("Analyse de nuages de points")

#     style = ttk.Style()
#     style.configure("TLabel", font=("Arial", 14))
#     style.configure("TButton", font=("Arial", 14))

#     title_label = ttk.Label(window, text="Analyse de nuages de points", font=("Arial", 16))
#     title_label.pack(pady=10)

#     browse_button = ttk.Button(window, text="Parcourir", command=browse_file)
#     browse_button.pack(pady=10)

#     file_path_label = ttk.Label(window, text="", wraplength=400)
#     file_path_label.pack(pady=10)

#     shape_label = ttk.Label(window, text="Sélectionnez la forme à rechercher:")
#     shape_label.pack(pady=10)

#     shape_var = tk.StringVar()
#     shape_var.set("Nuage de points")
#     shape_options = ["Nuage de points", "Carré", "Rectangle", "Triangle rectangle"]

#     shape_menu = ttk.OptionMenu(window, shape_var, *shape_options)
#     shape_menu.pack(pady=10)

#     analyze_button = ttk.Button(window, text="Analyser les points", command=analyze_points)
#     analyze_button.pack(pady=10)

#     result_label = ttk.Label(window, text="", wraplength=400)
#     result_label.pack(pady=10)

#     quit_button = ttk.Button(window, text="Quitter", command=window.quit)
#     quit_button.pack(pady=10)

#     window.mainloop()

# if __name__ == "__main__":
#     main()'''

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from ttkthemes import ThemedTk
import matplotlib.pyplot as plt
from itertools import combinations
from math import sqrt

# Les fonctions distance, est_carre, est_rectangle, est_triangle_rectangle, nuagedepts et polygone restent les mêmes

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        file_path_label.config(text=file_path)

def analyze_points():
    file_path = file_path_label.cget("text")
    if file_path:
        shape = shape_var.get()
        if shape == "Nuage de points":
            nuagedepts()
        elif shape == "Carré":
            polygone(est_carre)
        elif shape == "Rectangle":
            polygone(est_rectangle)
        elif shape == "Triangle rectangle":
            polygone(est_triangle_rectangle)
    else:
        result_label.config(text="Veuillez sélectionner un fichier CSV.")

def main():
    global file_path_label, result_label, shape_var

    window = ThemedTk(theme="arc")  # Vous pouvez changer le thème ici
    window.title("Analyse de nuages de points")

    style = ttk.Style()
    style.configure("TLabel", font=("Arial", 14))
    style.configure("TButton", font=("Arial", 14))

    title_label = ttk.Label(window, text="Analyse de nuages de points", font=("Arial", 16))
    title_label.pack(pady=10)

    browse_button = ttk.Button(window, text="Parcourir", command=browse_file)
    browse_button.pack(pady=10)

    file_path_label = ttk.Label(window, text="", wraplength=400)
    file_path_label.pack(pady=10)

    shape_label = ttk.Label(window, text="Sélectionnez la forme à rechercher:")
    shape_label.pack(pady=10)

    shape_var = tk.StringVar()
    shape_var.set("Nuage de points")
    shape_options = ["Nuage de points", "Carré", "Rectangle", "Triangle rectangle"]

    shape_menu = ttk.OptionMenu(window, shape_var, *shape_options)
    shape_menu.pack(pady=10)

    analyze_button = ttk.Button(window, text="Analyser les points", command=analyze_points)
    analyze_button.pack(pady=10)

    result_label = ttk.Label(window, text="", wraplength=400)
    result_label.pack(pady=10)

    quit_button = ttk.Button(window, text="Quitter", command=window.quit)
    quit_button.pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    main()