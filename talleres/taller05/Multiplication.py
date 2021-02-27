from time import time
import  matplotlib.pyplot as plt

def multiplication(n):
    for i in range (1, n+1): #T(n)=C1*n (C1=5)
        for j in range (0,11): #T(n)=C2*(n-1)*n (C2=4)
            print(i,"x",j,"=",i*j) #T(n)=C3*(n-1)*n
#T(n)=C3*(n-1)*n
#T(n)=C3*n^2-C3*n
#O(n^2)

multiplication(3)

#Tomar tiempos
times =[]
for i in range(1,205,20):
    inicio = time()
    multiplication(i)
    fin = time()
    total = fin-inicio
    times.append(total)
    print("El tiempo total con ", i,  " es: ", total, " ms")
   
#Graficar tiempos
plt.plot(range(1,205,20),times)
plt.xlabel("Dimensión (n)")
plt.ylabel("Tiempo de ejecución (ms)")
plt.title("Complejidad del algoritmo: Tablas de multiplicar")
plt.show()


#La commplejidad teórica no corresponde con aquella obtenida experimentalmente
#debido a que la teórica muestra un crecimiento cuadráditico(O(n^2)), mientras que
#la gráfica muestra un comportamiento lineal (O(n)).