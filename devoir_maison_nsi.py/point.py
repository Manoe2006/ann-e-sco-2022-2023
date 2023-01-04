def fich():
    A=[]
    f = open("mon.csv","r")
    lignes = f.readlines()
    for i in f:
        A=i.rstrip().split("\t")
        A.append(i)
    
    print(A) 

fich()


