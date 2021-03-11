import numpy as np
import copy
class matrice_rara:
    def __init__(self):
        self.n=None
        self.dictionar=dict()

    def construire_dictionar_prin_cale(self,cale):
        f = open(cale, "r")
        contor=0
        for x in f:
            linie=x.strip()
            if contor==0:
                self.n=int(linie)
                contor=contor+1
            if "," in linie:
                linieSplitata=linie.split(", ")
                linie=int(linieSplitata[1])
                coloana=int(linieSplitata[2])
                valoare=float(linieSplitata[0])
                if linie in self.dictionar.keys():
                    valoare_linie=self.dictionar[linie]
                    valoare_linie[coloana]=valoare
                    self.dictionar[linie]=valoare_linie
                else:
                    valoare_linie=dict()
                    valoare_linie[coloana]=valoare
                    self.dictionar[linie]=valoare_linie
    def adunare_matrici(self,a,b,c,p,q):
        adunare_matrici=copy.deepcopy(self.dictionar)
        for i in range(0,self.n-1):
            if i in adunare_matrici.keys():
                valoare_linie_i=adunare_matrici[i]
                if i+p in valoare_linie_i.keys():
                    adunare_matrici[i][i+p]=adunare_matrici[i][i+p]+b[i]
                else:
                    adunare_matrici[i][i+p]=b[i]
            else:
                adunare_matrici[i][i+p]=b[i]
            if i in adunare_matrici.keys():
                valoare_linie_i=adunare_matrici[i]
                if i in valoare_linie_i.keys():
                    adunare_matrici[i][i]=adunare_matrici[i][i]+a[i]
                else:
                    adunare_matrici[i][i]=a[i]
            else:
                adunare_matrici[i][i]=a[i]
            if i+q in adunare_matrici.keys():
                valoare_linie_i_plus_q=adunare_matrici[i+q]
                if i in valoare_linie_i_plus_q.keys():
                    adunare_matrici[i+q][i]=adunare_matrici[i+q][i]+c[i]
                else:
                    adunare_matrici[i+q][i]=c[i]
            else:
                adunare_matrici[i+q][i]=c[i]
        if self.n-1 in adunare_matrici.keys():
            valoare_linie_n_minus_1=adunare_matrici[self.n-1]
            if self.n-1 in valoare_linie_n_minus_1.keys():
                adunare_matrici[self.n-1][self.n-1]=adunare_matrici[self.n-1][self.n-1]+a[self.n-1]
            else:
                adunare_matrici[self.n-1][self.n-1]=a[self.n-1]
        else:
            dict_linia_n_minus_1={self.n-1:a[self.n-1]}
            adunare_matrici[self.n-1]=dict_linia_n_minus_1

        return adunare_matrici
    def operatia_de_inmultire(self,a,b,c,p,q):
        inmultire_matrici=dict()
        for i in range(0,self.n):
            for j in range(0,self.n):
                suma=0.0
                if i in self.dictionar.keys() and j in self.dictionar[i].keys():
                    suma=suma+a[j]*self.dictionar[i][j]
                if j>=p and i in self.dictionar.keys() and j-p in self.dictionar[i].keys():
                    suma=suma+b[j-p]*self.dictionar[i][j-p]

                if j<self.n-q and i in self.dictionar.keys() and j+q in self.dictionar[i].keys():
                    suma=suma+c[j]*self.dictionar[i][j+q]
                if suma!=0.0:
                    if i in inmultire_matrici.keys():
                        valoare_linie=inmultire_matrici[i]
                        valoare_linie[j]=suma
                        inmultire_matrici[i]=valoare_linie
                    else:
                        valoare_linie={j:suma}
                        inmultire_matrici[i]=valoare_linie
        return inmultire_matrici
                        




class matrice_tridiagoanala_rara:
    def __init__(self):
        self.n=None
        self.p=None
        self.q=None
        self.a=list()
        self.b=list()
        self.c=list()
    def construire_dictionar_prin_cale(self,cale):
        f = open(cale, "r")
        linie=f.readline().strip()
        self.n=int(linie)
        linie=f.readline().strip()
        self.p=int(linie)
        linie=f.readline().strip()
        self.q=int(linie)
        linie=f.readline() #linie goala
        for i in range(0,self.n):
            linie=f.readline().strip()
            self.a.append(float(linie))
        linie=f.readline().strip()
        for i in range(0,self.n-self.p):
            linie=f.readline().strip()
            self.b.append(float(linie))
        linie=f.readline().strip()
        for i in range(0,self.n-self.q):
            linie=f.readline().strip()
            self.c.append(float(linie))
            
def comparare_matrici(A,B,epsilon):
    try:
        for x,v in A.items():
            for x1,v1 in v.items():
                valoare_Norma=np.linalg.norm(A[x][x1]-B[x][x1])
                if valoare_Norma>epsilon:
                    return False
    except:
        return False
    return True


A=matrice_rara()
A.construire_dictionar_prin_cale("a.txt")
print(A.n,A.dictionar[0])
B=matrice_tridiagoanala_rara()
B.construire_dictionar_prin_cale("b.txt")
print(len(B.a),len(B.b),len(B.c))
A_plus_B=A.adunare_matrici(B.a,B.b,B.c,B.p,B.q)
A_plus_B_fisier=matrice_rara()
A_plus_B_fisier.construire_dictionar_prin_cale("aplusb.txt")
print(comparare_matrici(A_plus_B,A_plus_B_fisier.dictionar,10**(-10)))
A_ori_B=A.operatia_de_inmultire(B.a,B.b,B.c,B.p,B.q)
A_ori_B_fisier=matrice_rara()
A_ori_B_fisier.construire_dictionar_prin_cale("aorib.txt")
print(A_ori_B[0])
print(comparare_matrici(A_ori_B,A_ori_B_fisier.dictionar,10**(-10)))
