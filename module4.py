# Créé par ioana, le 28/09/2022 en Python 3.7

A=[0,0,0,0,0]
def maximum(A):
    '''création du tableau'''
    A[0]=int(input("entrez le premier chiffre du tableau:"))
    A[1]=int(input("entrez le second chiffre du tableau:"))
    A[2]=int(input("entrez le troisieme chiffre du tableau:"))
    A[3]=int(input("entrez le quatireme chiffre du tableau:"))
    A[4]=int(input("entrez le cinquieme chiffre du tableau:"))

    maxi= A[0]
    longueur= len(A)
    for i in range(longueur):
        if A[i] >= maxi:
            maxi=A[i]
    return maxi

A=[0,0,0,0,0]
def minimum(A):
    '''création du tableau'''
    A[0]=int(input("entrez le premier chiffre du tableau:"))
    A[1]=int(input("entrez le second chiffre du tableau:"))
    A[2]=int(input("entrez le troisieme chiffre du tableau:"))
    A[3]=int(input("entrez le quatireme chiffre du tableau:"))
    A[4]=int(input("entrez le cinquieme chiffre du tableau:"))

    '''affectation de commande a des variables'''
    mini= A[0]
    longueur= len(A)
    indice_mini=0

    ''' boucle qui va definir le minimum du tableau en comparant les differents elements du tableau '''
    for i in range(longueur):
        if A[i] <= mini:
            mini=A[i]
            indice_mini=i
    return indice_mini



