def suite_geometrique(n, u0, q):
    """
    Calcule les n premiers termes d'une suite géométrique
    :param n: nombre de termes à calculer
    :param u0: premier terme de la suite
    :param q: raison de la suite géométrique
    :return: liste des termes calculés
    """
    termes = [u0]
    for i in range(1, n):
        terme = u0 * (q ** i)
        termes.append(terme)
    return termes

# Paramètres de la suite géométrique
n = 15 # Nombre de termes à calculer
u0 = 2  # Premier terme de la suite
q = 3   # Raison de la suite géométrique

# Calcul et affichage des termes de la suite
termes = suite_geometrique(n, u0, q)
print(f"Les {n} premiers termes de la suite géométrique sont :")
print(termes)

suite_geometrique(20,65000,0.03)

