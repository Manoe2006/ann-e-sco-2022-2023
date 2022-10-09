L=[]
L.append("Lundi")
L.append("Mardi")
L.append("Mercredi")
L.append("Jeudi")
L.append("Vendredi")
L.append("Samedi")
L.append("Dimache")

print(L)

# affiche vendredi
print(L[4])

# L[6] = L[0]
# print(L[6])

def  remplacer(A,a,i):
    A[a]= A[i]

    return A[int(a)] 



remplacer(L,L[6],L[0])
print(L)

# remplacer(L,L[0],L[6])
# print(L)



# for i in range(12):
#     print(L[6])

    