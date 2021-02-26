from time import time
import random
import  matplotlib.pyplot as plt

def GroupSum(array, sum=0):
    for i in range (len(array)): #T(n)=C1*n (C1=5)
        sum = sum+array[i] #T(n)=C2*n (C2=3)
    return sum #T(n)=C3=1
#T(n)=C2*n
#O(n)

print(GroupSum([1,2,3,4,5,6]))

def createArray(length):
    array = []
    for i in range(length):
        array.append(random.randint(0,100000))
    return array

#Tomar tiempos
times =[]
for i in range(100,40000,2000):
    array = createArray(i)
    inicio = time()
    print(GroupSum(array))
    fin = time()
    total = fin-inicio
    times.append(total)
    print("El tiempo total con ", i,  " es: ", total, " ms")
   
#Graficar tiempos
plt.plot(range(1,40000,2000),times,label="ArrayMax")
plt.xlabel("Dimensión (n)")
plt.ylabel("Tiempo de ejecución (ms)")
plt.title("Complejidad del algoritmo: Group sum")
plt.show()