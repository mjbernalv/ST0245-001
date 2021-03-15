from time import time
import  matplotlib.pyplot as plt

def InsertionSort(array):
    for i in range(1,len(array)): #T(n)=C1*n (C1=5)
        x = array[i] #T(n)=C2=2*n
        j=i-1 #T(n)=C3=2*n
        while j>=0 and x<array[j]: #T(n)=(C4*(n-1)/2)*n (C4=4)
            array[j+1]=array[j] #T(n)=C5(n*(n-1)/2) (C5=4)
            j=j-1 #T(n)=C6(n*(n-1)/2) (C6=2)
        array[j+1]= x #T(n)=C7*n (C7=3)
    return array #T(n)=C8=1
#T(n)=C6(n*(n-1)/2)
#T(n)=1/2*(C6*n*(n-1))
#O(n^2)

def createArray(length):
    array = []
    for i in range(length, 0, -1):
        array.append(i)
    return array

print(InsertionSort([4,32,65,3,53]))

#Tomar tiempos
times =[]
for i in range(1,10100,500):
    array = createArray(i)
    inicio = time()
    
    InsertionSort(array)
    fin = time()
    total = fin-inicio
    times.append(total)
    print("El tiempo total con ", i,  " es: ", total, " ms")
   
#Graficar tiempos
plt.plot(range(1,10100,500),times)
plt.xlabel("Dimensión (n)")
plt.ylabel("Tiempo de ejecución (ms)")
plt.title("Complejidad del algoritmo: Insertion Sort")
plt.show()