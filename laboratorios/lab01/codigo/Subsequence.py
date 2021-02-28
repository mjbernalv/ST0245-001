import random
import string
from time import time
import  matplotlib.pyplot as plt


def randomAdn(size):
    letters = string.ascii_lowercase
    adn = ''.join(random.choice(letters) for i in range(size))
    return adn

def Subsequence(adn1, adn2):
    if len(adn1) == 0 or len(adn2) == 0: #T(n,m)=C1=6
        return 0 #T(n,m)=C2=1
    if adn1[len(adn1)-1] == adn2[len(adn2)-1]: #T(n,m)=C3=8
        return Subsequence(adn1[:len(adn1)-1], adn2[:len(adn2)-1])+1 #T(n,m)=T(n-1,m-1)+C4 (C4=8)
    return max(Subsequence(adn1[:len(adn1)-1], adn2), Subsequence(adn1,adn2[:len(adn2)-1])) #T(n,m)=T(n-1,m)+T(n,m-1)+C5 (C5=8)

#T(n,m)=T(n-1,m)+T(n,m-1)+C
#T(p)=2T(p-1)+C (con p=n+m y donde p es el tamaño de las cadenas de adn)
#T(n)=C(2^p-1)+C1*2^(p-1)
#O(2^p)

#Ejemplos
#print(Subsequence("ABCDGH", "AEDFHR"))
#print(Subsequence("AGGTAB", "GXTXAYB"))
#print(Subsequence("AGGTAB", "GXTXAYB"))
#print(Subsequence("ABCDEFGH", "JACBMAG"))

#Tomar tiempos
times =[]
for i in range(1,16):
    adn1 = randomAdn(i)
    adn2 = randomAdn(i)
    inicio = time()
    print(Subsequence(adn1, adn2))
    fin = time()
    total = fin-inicio
    times.append(total)
    print("El tiempo total con ", i,  " es: ", total, " ms")
   
#Graficar tiempos
plt.plot(range(1,16),times)
plt.xlabel("Dimensión (n)")
plt.ylabel("Tiempo de ejecución (ms)")
plt.title("Complejidad del algoritmo: ADN subsequence")
plt.show()