

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
import matplotlib.pyplot as plt
import numpy as np
import time
import math

mic=10**(-12)
def my_tan(x,e):
    f=0
    if f==0:
        f=mic
    c=f #initial c=b0 ,dar b0 cum e 0 o sa fie estimat la mic
    d=0
    j=1
    b=1
    delta=c*d
    while abs(delta-1)>=e:
        c_anterior=c
        d_anterior=d
        f_anterior=f
        if j==1:
            d=b+x*d_anterior
        else:
            d=b+(-x**2)*d_anterior
        if d==0:
            d=mic
        if j==1:
            c=b+(x/c_anterior)
        else:
            c=b+((-x**2)/c_anterior)
        if c==0:
            c=mic
        d=1/d
        delta=c*d
        f=delta* f_anterior
        b=b+2
        j=j+1
    return f

def my_tan_2(x):
    c1 =  0.33333333333333333
    c2 =0.133333333333333333
    c3= 0.053968253968254
    c4=0.0218694885361552
    x_2=x*x
    x_3=x_2*x
    x_4=x_3*x
    x_5=x_4*x
    x_6=x_5*x
    x_7=x_6*x
    x_8=x_7*x
    x_9=x_8*x
    return x+ (c1* x_3 ) + ( c2 * x_5 ) + ( c3 * x_7 ) + ( c4 * x_9 )

vector_nr=np.linspace(-np.pi/2+mic,np.pi/2-mic,1000)
timp_initial=time.time()
for nr in vector_nr:
    print("Pentru nr:",nr)
    my_tan1=my_tan(nr,10**(-1))
    tangenta_x=math.tan(nr)
    print("Valoarea tangentei implementata de biblioteca:",tangenta_x)
    print("Metoda Lentz:",my_tan1)
    timp_curent=time.time()
    timp_trecut_1=timp_curent-timp_initial
    print("Timp trecut pentru metoda Lentz: ",timp_trecut_1)
    print("Eroarea de calcul intre tan(x)-tangenta calculata prin metoda Lentz:",abs(tangenta_x-my_tan1))
    timp_initial=timp_curent
    my_tan2 = my_tan_2(nr)
    print('Metoda MacLaurin:',my_tan2)
    timp_curent = time.time()
    timp_trecut_2=timp_curent - timp_initial
    print("Timp trecut pentru metoda MacLaurin: ",timp_trecut_2)
    print("Eroarea de calcul intre tan(x)-tangenta calculata prin metoda MacLaurin:",abs(tangenta_x-my_tan2))
    timp_initial=timp_curent

    print('Diferenta timp calcul ', abs(timp_trecut_1-timp_trecut_2))


plt.plot(vector_nr, np.tan(vector_nr))
plt.ylim(-10, 10)
plt.show()