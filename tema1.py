

#Exercitiul 1

for i in range(10000,0,-1):
    u=10**(-i)
    if 1.0+u != 1.0 :
        print(f"Precizia masina gasita este: {u}")
        break

##############################################

#Exercitiul 2

a=1.0
b=u/10
c=u/10

elem1=(a+b)+c
elem2=a+(b+c)
if elem1==elem2:
    print("Adunarea este asociativa")
else:
    print("Adunarea nu este asociativa")
    print("(a+b)+c=",elem1)
    print("a+(b+c)=",elem2)

import random
while True:
    a=random.uniform(0, 1)
    b=random.uniform(0, 1)
    c=random.uniform(0, 1)
    elem1=(a*b)*c
    elem2=a*(b*c)
    if elem1!=elem2:
        break
print("Exemplul pentru care inmultirea nu este asociativa:")
print(f"a={a}")
print(f"b={b}")
print(f"b={c}")

#############################################################

#Exercitiul 3


