# Créé par ioana, le 04/10/2022 en Python 3.7
def addition_v1(a,b):
    c=a+b



def addition_v2(a,b):
    c=a+b

    return c




i=addition_v1(2,3)
j=addition_v2(2,3)

print(i)
print(j)



c=addition_v2(2,3)+addition_v2(4,6)
print(c)

d=addition_v1(2,3)+addition_v1(4,6)
print(d)

e=addition_v1(2,3)+addition_v2(4,6)
print(e)
