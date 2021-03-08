import csv
import numpy as np
import math
from scipy.linalg import lu
import random

####################################
def preluare_date_csv(cale,n):
    A_intermediar=list() 
    b_intermediar=list() 
    with open(cale) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            b_intermediar.append(float(row[n]))
            linie=list()
            for j in range(0,n):
                linie.append(float(row[j]))
            A_intermediar.append(linie)
    A=np.array(A_intermediar) #matricea sistemului simetrica si strict pozitiva
    b=np.array(b_intermediar) #vectorul termenilor liberi
    d=np.array([])
    for i in range(0,len(A)):
        d=np.append(d,A[i][i])

    return A,b,d

A,b,d=preluare_date_csv("date.csv",3)
epsilon=pow(10,-5)
def citire_data_tastatura():
    n=int(input("Dati dimensiunea matricii: "))
    epsilon=float(input("Dati eroarea: "))
    A=np.full((n,n),0.0)
    b=np.full(n,0.0)
    for i in range(0,n):
        linie_Matrice=input("Dati linia "+ str(i)+" a matricii cu elementele separate prin virgula: ")
        linie_matrice_splitata=linie_Matrice.split(",")
        for j in range(0,len(linie_matrice_splitata)):
            A[i][j]=float(linie_matrice_splitata[j])
    coloana_vector_liber=input("Dati n elemente separate prin virgula are vectorului liber b: ")
    coloana_vector_liber_splitata=coloana_vector_liber.split(",")
    for j in range(0,len(coloana_vector_liber_splitata)):
        b[j]=float(coloana_vector_liber_splitata[j])
    return epsilon,A,b
def generare_matrice(n):
    A_generat=np.full((n,n),0.0)
    for i in range(0,n):
        for j in range(i,n):
            A_generat[i][j]=random.uniform(1.0,90.0)
            if i!=j:
                A_generat[j][i]=A_generat[i][j]
    return A_generat
A=generare_matrice(10)
b=np.random.rand(10)
def validare_matrice_simetrica(A):
    for i in range(0,len(A)):
        for j in range(i,len(A)):
            if A[j][i]!=A[i][j]:
                return False
    return True
print(validare_matrice_simetrica(A.copy()))
def descompunere_Cholesky_matrice_modificata(A_initial):
    
    for i in range(0,len(A_initial)):
        for j in range(i,len(A_initial)):
            if i==j:
                valSuma=0
                for k in range(0,i):
                    valSuma=valSuma+pow(A_initial[i][k],2)
                A_initial[i][j]=math.sqrt(d[i]-valSuma)
            else:
                valSuma=0
                for k in range(0,i):
                    valSuma=valSuma+A_initial[j][k]*A_initial[i][k]
                if math.fabs(A_initial[i][i])>epsilon:
                    A_initial[j][i]=(A_initial[j][i]-valSuma)/A_initial[i][i]
                else:
                    print("Nu se poate face impartirea")
    return A_initial
def validare_descompunere_Cholesky(A,L,L_transpus):
    print(np.linalg.norm(A-L@L_transpus))
def validare_determinant(A,det_A):
    print(np.linalg.norm(np.linalg.det(A) - det_A))
def calculare_determinat_matrice(A):
    det_A=1
    for i in range(0,len(A)):
        det_A=A[i][i]*det_A
    return det_A*det_A

def sisteme_liniare_metoda_substitutiei(L,b):
    y_star=np.array([])
    for i in range(0,len(L)):
        valSuma=0
        for j in range(0,i):
            valSuma=valSuma+L[i][j]*y_star[j]
        if math.fabs(L[i][i])>epsilon:
            y_star=np.append(y_star,((b[i]-valSuma))/L[i][i])
        else:
            print("Nu se poate face impartirea")
    return y_star

def sisteme_liniare_inversa_metodei_substitutiei(L_transpus,y):
    x_star=np.full(len(L_transpus),0.0)
    for i in range(len(L_transpus)-1,-1,-1):
        valSuma=0
        for j in range(i+1,len(L_transpus)):
            valSuma=valSuma+L_transpus[j][i]*x_star[j]
        if math.fabs(L_transpus[i][i])>epsilon:
            x_star[i]=(y[i]-valSuma)/L_transpus[i][i]
        else:
            print("Nu se poate face impartirea")
    return x_star
def verificare_solutie_sistem(A,x_star,b):
    print(np.linalg.norm(A@x_star-b))

def returnare_matrice_L(A):
    for i in range(0,len(A)):
        for j in range(0,len(A)):
            if j>i:
                A[i][j]=0.0
    return A
def returnare_matrice_L_transpus(A):
    for i in range(0,len(A)):
        for j in range(0,len(A)):
            if i>j:
                A[i][j]=0.0
            else:
                A[i][j]=A[j][i]
    return A
def returnare_matrice_initiala(A):
    for i in range(0,len(A)):
        for j in range(0,len(A)):
            if i==j:
                A[i][j]=d[i]
            elif i>j:
                A[i][j]=A[j][i]
    return A


def afisare_matrice_L(A):
    for i in range(0,len(A)):
        for j in range(0,len(A)):
            if j>i:
                print("0.0",end=" ")
            else:
                print(A[i][j],end=" ")
        print(end="\n")
def afisare_matrice_L_transpus(A):
    for i in range(0,len(A)):
        for j in range(0,len(A)):
            if i>j:
                print("0.0",end=" ")
            else:
                print(A[j][i],end=" ")
        print(end="\n")
def afisare_matrice_initiala_A(A):
    for i in range(0,len(A)):
        for j in range(0,len(A)):
            if i==j:
                print(d[i],end=" ")
            elif i<j:
                print(A[i][j],end=" ")
            else:
                print(A[j][i],end=" ")
        print(end="\n") 
def descompunere_LU(A):
    p,l,u=lu(A)
    return l,u
def calculare_inversa_matricii(A):
    matricea_inversa=np.full((len(A),len(A)),0.0)
    for i in range(0,len(A)):
        matricea_identitate=np.full(3,0.0)
        matricea_identitate[i]=1
        y_star=sisteme_liniare_metoda_substitutiei(A,matricea_identitate)
        x_star=sisteme_liniare_inversa_metodei_substitutiei(A,y_star)
        for j in range(0,len(A)):
            matricea_inversa[j][i]=x_star[j]
    return matricea_inversa
def validare_inversa_cu_matricea_identitate(A,A_inversat):
    print(np.linalg.norm(A @ A_inversat - np.eye(len(A), len(A))))

def validare_inversa_cu_inversa_din_alta_biblioteca(A,A_inversat):
    print(np.linalg.norm(A_inversat - np.linalg.inv(A)))
A_modificat=descompunere_Cholesky_matrice_modificata(A.copy())

#######################################
#BONUS
def stocare_matrice_a(A):
    A_limitat=np.array([])
    for i in range(0,len(A)):
        for j in range(0,len(A)):
            if i>=j:
                A_limitat=np.append(A_limitat,A[i][j])
    return A_limitat
A_limitat=stocare_matrice_a(A)
print(A_limitat)
def get_index_element_prin_coordonate(linie,coloana,tip):
    if coloana>linie and tip==1: #simetrie
        temp=linie
        linie=coloana
        coloana=temp
    pozitie_vector=(linie*(linie+1)//2)+coloana
    return pozitie_vector
def descompunere_Cholesky_bonus(A,n):
    L=np.full(n*(n+1)//2,0.0)
    for i in range(0,n):
        for j in range(i,n):
            if i==j:
                valSuma=0
                for k in range(0,i):
                    valSuma=valSuma+pow(L[get_index_element_prin_coordonate(i,k,2)],2)
                L[get_index_element_prin_coordonate(i,j,2)]=math.sqrt(A[get_index_element_prin_coordonate(i,j,1)]-valSuma)
            else:
                valSuma=0
                for k in range(0,i):
                    valSuma=valSuma+L[get_index_element_prin_coordonate(j,k,2)]*L[get_index_element_prin_coordonate(i,k,2)]
                if math.fabs(L[get_index_element_prin_coordonate(i,i,2)])>epsilon:
                    L[get_index_element_prin_coordonate(j,i,2)]=(A[get_index_element_prin_coordonate(j,i,1)]-valSuma)/L[get_index_element_prin_coordonate(i,i,2)]
                else:
                    print("Nu se poate face impartirea")
    L_transpus=np.array([])
    for i in range(0,n):
        for j in range(i,n):
            L_transpus=np.append(L_transpus,L[get_index_element_prin_coordonate(j,i,2)])
    return L,L_transpus

def sisteme_liniare_metoda_substitutiei_bonus(L,b,n):
    y_star=np.array([])
    for i in range(0,n):
        valSuma=0
        for j in range(0,i):
            valSuma=valSuma+L[get_index_element_prin_coordonate(i,j,2)]*y_star[j]
        if math.fabs(L[get_index_element_prin_coordonate(i,i,2)])>epsilon:
            y_star=np.append(y_star,((b[i]-valSuma))/L[get_index_element_prin_coordonate(i,i,2)])
        else:
            print("Nu se poate face impartirea")
    return y_star

def sisteme_liniare_inversa_metodei_substitutiei_bonus(L_transpus,y,n):
    x_star=np.full(n,0.0)
    for i in range(n-1,-1,-1):
        valSuma=0
        for j in range(i+1,n):
            valSuma=valSuma+L_transpus[get_index_element_prin_coordonate(j,i,2)]*x_star[j]
        if math.fabs(L_transpus[get_index_element_prin_coordonate(i,i,2)])>epsilon:
            x_star[i]=(y[i]-valSuma)/L_transpus[get_index_element_prin_coordonate(i,i,2)]
        else:
            print("Nu se poate face impartirea")
    return x_star
#######################################################
if validare_matrice_simetrica(A.copy()):
    print("Matricea A modificata cu descompunerea Cholesky")
    print(A_modificat)
    print("Matricea L in descompunerea Cholesky")
    afisare_matrice_L(A_modificat.copy())
    print("Matricea L transpusa in descompunerea Cholesky ")
    afisare_matrice_L_transpus(A_modificat.copy())
    print("Validarea descompunerii Cholesky calculand norma diferentei dintre A si LL_transpus")
    L=returnare_matrice_L(A_modificat.copy())
    L_transpus=returnare_matrice_L_transpus(A_modificat.copy())
    A_init=returnare_matrice_initiala(A_modificat.copy())
    validare_descompunere_Cholesky(A_init,L,L_transpus)
    print("Putem valida cu varianta determinantului din numpy")
    det_A=calculare_determinat_matrice(A_modificat)
    print("Valoare determinant matrice A:det(L)^^2: ",det_A)
    validare_determinant(A_init,det_A)
    print("Matricea initiala")
    afisare_matrice_initiala_A(A_modificat.copy())
    y_star=sisteme_liniare_metoda_substitutiei(A_modificat,b)
    x_star=sisteme_liniare_inversa_metodei_substitutiei(A_modificat,y_star)
    print("Solutia Ly=b este: ")
    print(y_star)
    print("Solutia L_transpus.x=y este:")
    print(x_star)
    print("Verificarea solutiei prin afisarea normei: ")
    verificare_solutie_sistem(A_init,x_star,b)
    print("Afisarea descompunerii LU a matricii A: ")
    l,u=descompunere_LU(A_init)
    print("Matricea inferior triunghiulara L")
    print(l)
    print("Matricea superior triunghiulara L")
    print(u)
    print("Solutia x_star prin descompunerea LU din biblioteca:")
    x_star_lu=np.linalg.solve(A_init,b)
    print(x_star_lu)
    print("Inversa matricei A: ")
    A_inversat=calculare_inversa_matricii(A_modificat.copy())
    print(A_inversat)
    print("Putem valida calculand norma A*A^^-1-In")
    validare_inversa_cu_matricea_identitate(A_init,A_inversat)
    print("De asemenea putem valida si cu versiunea de calculare a inversei din numpy:")
    validare_inversa_cu_inversa_din_alta_biblioteca(A_init,A_inversat)


###############
#BONUS
A_limitat=stocare_matrice_a(A)
L_bonus,L_transpus_bonus=descompunere_Cholesky_bonus(A_limitat.copy(),3)
print(L_bonus)
print(L_transpus_bonus)
y_star_bonus=sisteme_liniare_metoda_substitutiei_bonus(L_bonus,b,3)
print(y_star_bonus)
x_star_bonus=sisteme_liniare_inversa_metodei_substitutiei_bonus(L_bonus,y_star_bonus,3)
print(x_star_bonus)