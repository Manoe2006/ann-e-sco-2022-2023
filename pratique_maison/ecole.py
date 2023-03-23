f=open("Manoé.csv","w")
L=["X","Y"]
for i in range(-10,11):
    A=[str(i),str(i**2)]
    
    f.write(str(A))
f.close() 
