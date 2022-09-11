# Créé par ioana, le 08/09/2022 en Python 3.7

def med (A):
    n= len(A)

    if (n%2!=0) :
        ind=int(n//2)
        m=A[ind]

    else:
        ind1=int(n//2)
        ind2= int((n//2)+1)
        m1= A[ind1]
        m2= A[ind2]
        m= ((A[ind1]+A[ind2])//2)
    return m

# a = [2,6,7,10]



n1= int(input("entrer votre premiere note"))
n2= int(input("entrer votre seconde note"))
n3= int(input("entrer votre troisieme note"))
n4= int(input("entrer votre quatrieme note"))

a= [n1,n2,n3,n4]

print(med(a))
























