# Créé par ioana, le 20/09/2022 en Python 3.7
def remplacer(A,a,i):
    '''securité de valeure positive'''
    if i<0:
        print("entrer une valeure posotive")
        return
    '''securite i ne dois pas etre superieur au nombre d'element du tableau'''
    if i> len(A):
        print("i ne doit pas etre superieur a la longueur du tableau")
        return

    B=A
    B[i]=A
    return B





def inserer(A,a,i):
    B=[]
    for j in range (i):
        B.append(A[j])

    B.append(a)
    for j in range (i,len(A)):
        B.append(A[j])

    return B







