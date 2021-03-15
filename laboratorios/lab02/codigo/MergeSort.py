from time import time
import  matplotlib.pyplot as plt

def MergeSort(array):
    if len(array)>1: #T(n)=C1=3
        middle = len(array)//2 #T(n)=C2=3
        firstHalf = array[:middle] #T(n)=C3=2
        secondHalf = array[middle:] #T(n)=C4=2
        
        MergeSort(firstHalf) #T(n)=T(n/2)
        MergeSort(secondHalf) #T(n)=T(n/2)

        i=0 #T(n)=C5=1
        j=0 #T(n)=C6=1
        k=0 #T(n)=C7=1
        while i<len(firstHalf) and j<len(secondHalf): #T(n)=C8*n (C8=5)
            if firstHalf[i]<secondHalf[j]: 
                array[k]=firstHalf[i] 
                i+=1 
            else: 
                array[k]=secondHalf[j] 
                j+=1 
            k+=1 
        while i < len(firstHalf): #T(n)=C8*n
            array[k] = firstHalf[i]
            i += 1 
            k += 1 
        while j < len(secondHalf): #T(n)=C8*n
            array[k] = secondHalf[j] 
            j += 1
            k += 1

    return array
#T(n)=T(n/2)*n*c
#O(nlogn)

def createArray(length):
    array = []
    for i in range(length,0,-1):
        array.append(i)
    return array

print(MergeSort([12, 11, 13, 5, 6, 7]))


#Tomar tiempos
times =[]
for i in range(100,2000100,100000):
    array = createArray(i)
    inicio = time()
    MergeSort(array)
    fin = time()
    total = fin-inicio
    times.append(total)
    print("El tiempo total con ", i,  " es: ", total, " ms")
   
#Graficar tiempos
plt.plot(range(100,2000100,100000),times)
plt.xlabel("Dimensión (n)")
plt.ylabel("Tiempo de ejecución (ms)")
plt.title("Complejidad del algoritmo: Merge Sort")
plt.show()