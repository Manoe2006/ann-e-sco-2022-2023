def image(x):
    f=open("image.txt","w")
    d=2*x**2-3*x+1
    for i in range(100):
        x=i 
        f.write("str(x);str(2*x**2-3*x+1)\n")
    f.close()
      
