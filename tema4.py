import numpy as np
import plotly.graph_objects as go
class TriagMatrix:
    def __init__(self):
        self.n=None
        self.p=None
        self.q=None
        self.a=np.array([],float)
        self.b=np.array([],float)
        self.c=np.array([],float)
        self.kmax=10000

    def read_matrix_from_file(self,path):
        f = open(path, "r")
        linie=f.readline().strip()
        self.n=int(linie)
        linie=f.readline().strip()
        self.p=int(linie)
        linie=f.readline().strip()
        self.q=int(linie)
        linie=f.readline() #linie goala
        for i in range(0,self.n):
            linie=f.readline().strip()
            self.a=np.append(self.a,float(linie))
        linie=f.readline().strip()
        for i in range(0,self.n-self.p):
            linie=f.readline().strip()
            self.c=np.append(self.c,float(linie))
        linie=f.readline().strip()
        for i in range(0,self.n-self.q):
            linie=f.readline().strip()
            self.b=np.append(self.b,float(linie))
    def check_main_diag(self):
        for i in range(0,self.n):
            if self.a[i]==0:
                return False
        return True
    def gauss_seidel(self,f,epsilon):
        if self.check_main_diag():
            x_c=np.full(self.n,0.0,float)
            k=0
            x_p=np.copy(x_c)
            delta_vector=np.array([])
            x_vector=[]
            for i in range(0,self.n):
                if i>=self.q and i<self.n-self.p:
                    x_c[i]=(f[i]-self.c[i-1]*x_c[i-1]-self.b[i]*x_p[i+1])/self.a[i]
                elif i<self.q:
                    x_c[i]=(f[i]-self.b[i]*x_p[i+1])/self.a[i]
                elif i>=self.n-self.p:
                    x_c[i]=(f[i]-self.c[i-1]*x_c[i-1])/self.a[i]
            delta_x=np.linalg.norm(x_c-x_p)
            delta_vector=np.append(delta_vector,delta_x)
            k=k+1
            while delta_x>=epsilon and k<=self.kmax and delta_x<=10**8:
                x_p=np.copy(x_c)
                for i in range(0,self.n):
                    if i>=self.q and i<self.n-self.p:
                        x_c[i]=(f[i]-self.c[i-1]*x_c[i-1]-self.b[i]*x_p[i+1])/self.a[i]
                    elif i<self.q:
                        x_c[i]=(f[i]-self.b[i]*x_p[i+1])/self.a[i]
                    elif i>=self.n-self.p:
                        x_c[i]=(f[i]-self.c[i-1]*x_c[i-1])/self.a[i]
                delta_x=np.linalg.norm(x_c-x_p)
                delta_vector=np.append(delta_vector,delta_x)
                x_vector.append(x_p)
                k=k+1
            if delta_x<epsilon:
                return x_c,k,delta_vector,x_vector
            else:
                return "divergenta",None,None,None
        return "Elemente nule pe diag principala"
    def multiply_vector(self,x):
        vector_result=np.array([],float)
        for i in range(0,self.n):
            suma=0.0
            if i<self.n-self.p:
                suma=suma+self.b[i]*x[i+self.p]
            suma=suma+self.a[i]*x[i]
            if i>=self.q:
                suma=suma+self.c[i-self.q]*x[i-self.q]
            vector_result=np.append(vector_result,suma)
        return vector_result

def delta_x_over_iterations(delta_vector,nr_iter):
    x=[x for x in range(0,nr_iter)]
    fig = go.Figure(data=go.Scatter(x=x, y=delta_vector, name="delta_x evolution over iterations"))
    fig.show()
def x_solution_evolution(vector_x):
    fig = go.Figure()
    # Add traces, one for each slider step
    for step in range(0,len(vector_x)):
        fig.add_trace(
            go.Histogram(x=vector_x[step], histnorm='probability',name="k"+str(step)))

    for step in range(0,len(vector_x)):
        fig.data[step].visible = True

    # Create and add slider
    steps = []
    for i in range(len(fig.data)):
        step = dict(
            method="update",
            args=[{"visible": [False] * len(fig.data)},
                {"title": "Slider switched to step: " + str(i)}],  # layout attribute
        )
        step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
        steps.append(step)

    sliders = [dict(
        active=10,
        currentvalue={"prefix": "Frequency: "},
        pad={"t": 50},
        steps=steps
    )]

    fig.update_layout(
        sliders=sliders
    )

    fig.show()


class Vector_f():
    def __init__(self):
        self.n=None
        self.f=np.array([])
    def read_vector_from_file(self,path):
        file = open(path, "r")
        linie=file.readline().strip()
        self.n=int(linie)
        linie=file.readline() #linie goala
        for i in range(0,self.n):
            linie=file.readline().strip()
            self.f=np.append(self.f,float(linie))
        

A1=TriagMatrix()
A1.read_matrix_from_file("a1.txt")
f1=Vector_f()
f1.read_vector_from_file("f1.txt")
x_star_1,k_1,delta_vector_1,x_vector_1=A1.gauss_seidel(f1.f,10**(-10))
print(x_star_1)
print(np.linalg.norm(A1.multiply_vector(x_star_1)-f1.f,np.inf))
delta_x_over_iterations(delta_vector_1,k_1)
x_solution_evolution(x_vector_1)

A2=TriagMatrix()
A2.read_matrix_from_file("a2.txt")
f2=Vector_f()
f2.read_vector_from_file("f2.txt")
x_star_2,k_2,delta_vector_2,x_vector_2=A2.gauss_seidel(f2.f,10**(-3))
print(x_star_2)
print(np.linalg.norm(A2.multiply_vector(x_star_2)-f2.f,np.inf))
delta_x_over_iterations(delta_vector_2,k_2)
x_solution_evolution(x_vector_2)

A3=TriagMatrix()
A3.read_matrix_from_file("a3.txt")
f3=Vector_f()
f3.read_vector_from_file("f3.txt")
x_star_3,k_3,delta_vector_3,x_vector_3=A3.gauss_seidel(f3.f,10**(-10))
print(x_star_3)
print(np.linalg.norm(A3.multiply_vector(x_star_3)-f3.f,np.inf))
delta_x_over_iterations(delta_vector_3,k_3)
x_solution_evolution(x_vector_3)

A4=TriagMatrix()
A4.read_matrix_from_file("a4.txt")
f4=Vector_f()
f4.read_vector_from_file("f4.txt")
x_star_4,k_4,delta_vector_4,x_vector_4=A4.gauss_seidel(f4.f,10**(-10))
print(x_star_4)
print(np.linalg.norm(A4.multiply_vector(x_star_4)-f4.f,np.inf))
delta_x_over_iterations(delta_vector_4,k_4)
x_solution_evolution(x_vector_4)

A5=TriagMatrix()
A5.read_matrix_from_file("a5.txt")
f5=Vector_f()
f5.read_vector_from_file("f5.txt")
x_star_5, k_5, delta_vector_5,x_vector_1=A5.gauss_seidel(f5.f,10**(-10))
print(x_star_5)
