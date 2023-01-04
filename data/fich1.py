f=open("man.csv","w")
C=["1","2"]
for i in range(-15,16):
    A=[str(i),str(i//2)]
    B=";".join(C)+"\n"
    f.write(str(B))
f.close()