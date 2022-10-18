# Créé par ioana, le 17/10/2022 en Python 3.7
A=[]
def sml(A):
    # A=[]
    # l'utilisateur rentre ses données


    # affichage du tableau
    for i in range(len(A)):
        print(A)

    # affichage de chaque indice et de leurs contenu
    for i in range(len(A)):
        print(i,A[i])

    # addition de tous les élements du tableau
    for i in range(len(A)):
        a=A[0]+A[1]+A[2]+A[3]+A[4]
        print(a)

    # ajout du resultat de la multiplication par 3de chaque elements au tableau
    for i in range(len(A)):
        B=[]
        b=(A[0]*3)
        c=(A[1]*3)
        d=(A[2]*3)
        e=(A[3]*3)
        f=(A[4]*3)
        B.append(b)
        B.append(c)
        B.append(d)
        B.append(e)
        B.append(f)
        print(B)

    # le plus grand chiffre du tableau
    for i in range(len(A)):
        print(max(A))

    # le plus petit chiffre du tableau
    for i in range(len(A)):
        print(min(A))

    #  comptage du nombre des nombres pairs du tableau
    for i in range(len(A)):
        if ((A[i]%2)==0):

            print("il y a des nombres paires")

    # calcul de la somme des nombres impairs du tableau
    for i in range(len(A)):
        C=[]
        if ((A[i]%2)!=0):
            C.append(A[i])
            print(C)
            for i in range(len(C)):
                g=C[i]+C[i]
            print(g)






















