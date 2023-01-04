# Créé par ioana, le 14/12/2022 en Python 3.7
import matplotlib.pyplot as plt
A=[]
f=open("mon.csv","r")
lignes=f.readlines()
B=[]
n=0
x1=[]
y1=[]
x2=[]
y2=[]
for i in range(1,len(lignes)):
    l=lignes[i]
    A=l.split(";")
    x=float(A[0])
    y=float(A[1])
    C=[x,y]
    x1.append(x)
    y1.append(y)
    B.append(C)
plt.plot(x1,y1,"+")
plt.plot
