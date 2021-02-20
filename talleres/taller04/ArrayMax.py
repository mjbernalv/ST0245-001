import sys
from time import time
import random
import  matplotlib.pyplot as plt

def arrayMax(arr):
    return arrayMax_aux(arr, 0, 0)

def arrayMax_aux(arr, i, max):
    if i==len(arr):
        return max
    if arr[i]>max:
        max=arr[i]
    return arrayMax_aux(arr, i+1, max)

def createArray(length):
    array = []
    for i in range(length):
        array.append(random.randint(0,100000))
    return array

sys.setrecursionlimit(2000000)

print(arrayMax([12,342,255,542,23]))

times =[]
for i in range(100,10000,500):
    array = createArray(i)
    inicio = time()
    print(arrayMax(array))
    fin = time()
    total = fin-inicio
    times.append(total)
    print("El tiempo total con ", i,  " es: ", total, " ms")
    
plt.plot(range(1,9600,500),times,label="ArrayMax")
plt.xlabel("Dimensión (n)")
plt.ylabel("Tiempo de ejecución (ms)")
plt.title("Complejidad del algoritmo: Array Max")
plt.show()