import sys
from time import time
import random
import  matplotlib.pyplot as plt


def groupSum_aux(list, start, target):
    if start>= len(list):
        return target ==0
    use = groupSum_aux(list, start+1, target-list[start])
    dontUse = groupSum_aux(list, start+1, target)
    return use or dontUse

def groupSum(list, target):
    return groupSum_aux(list, 0, target)

def createArray(length):
    array = []
    for i in range(length):
        array.append(random.randint(0,100))
    return array

sys.setrecursionlimit(2000000000)

#Tomar tiempos
times =[]
for i in range(5,26, 1):
    array = createArray(i)
    inicio = time()
    print(groupSum(array, random.randint(0,500)))
    fin = time()
    total = fin-inicio
    times.append(total)
    print("El tiempo total con ", i,  " es: ", total, " ms")
   
#Graficar tiempos
plt.plot(range(5,26),times)
plt.xlabel("Dimensión (n)")
plt.ylabel("Tiempo de ejecución (ms)")
plt.title("Complejidad del algoritmo: Group Sum")
plt.show()