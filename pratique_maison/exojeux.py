def compare (A,a,i):
    B=[0,0]



    for j in range (len(A)):
        if (A[j]==a):
            B[0]=0
            B[1]=1
        print (B[1])


             if (i==j):
                B[0]=1
           return B




def jeu (A,n):

    B=[0,0,0]
    for j in range (10):

         B[0]=int(input("Entrez le premier chiffre de la combinaison"))
         B[1]= int(input("entrer le second chiffre de la combinaison "))
         B[2]= int(input("entrer le troisieme chiffre de la combinaison "))


         nbp=0
         nbi=0


         for i in range(len(B)):
            C= compare(A,B[i],i)
            nbp= int(nbp)+int(C[0])
            nbi= int(nbi)+int(C[1])

         print(nbp,nbi)


A=[1,2,5]

jeu(A,5)










