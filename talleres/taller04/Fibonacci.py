from time import time
import  matplotlib.pyplot as plt

def Fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2)

#tomar tiempos
times=[]
for i in range(36):
    start = time()
    print(Fibonacci(i))
    end = time()
    total = end-start
    times.append(total)
    print(total)

#graficar complejidad
plt.plot(times)
plt.xlabel("Dimensión (n)")
plt.ylabel("Tiempo de ejecución (ms)")
plt.title("Complejidad del algoritmo: Sucesión de Fibonacci")
plt.show()