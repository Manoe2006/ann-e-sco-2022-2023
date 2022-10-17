A=[]
def sml(A):
    # A=[]
    # l'utilisateur rentre ses données
    # A[0]=int(input("entrez le premier chiffre: "))
    # A[1]=int(input("entrez le deuxieme chiffre: "))
    # A[2]=int(input("entrez le troisieme chiffre: "))
    # A[3]=int(input("entrez le quatrieme chiffre: "))
    # A[4]=int(input("entrez le cinquieme chiffre: "))

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
            print("il y a des nombres paires ")
    
    # calcul de la somme des nombres pairs du tableau 
    for i in range(len(A)):
        C=[]
        if ((A[i]%2)!=0):
            C.append(A[i])
        g=A[0]+A[1]+A[2]+A[3]+A[4]
        print(g) 



sml(A=[2,5,4,7,9])

        


    


    
       





