def suite_arithmetique(n, u0, r):
    """
    Calcule les n premiers termes d'une suite arithmétique
    :param n: nombre de termes à calculer
    :param u0: premier terme de la suite
    :param r: raison de la suite arithmétique
    :return: liste des termes calculés
    """
    termes = [u0]
    for i in range(1, n):
        terme = u0 + i * r
        termes.append(terme)
    return termes

# Paramètres de la suite arithmétique
n = 10  # Nombre de termes à calculer
u0 = 2  # Premier terme de la suite
r = 3   # Raison de la suite arithmétique

# Calcul et affichage des termes de la suite
termes = suite_arithmetique(n, u0, r)
print(f"Les {n} premiers termes de la suite arithmétique sont :")
print(termes)
