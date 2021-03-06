def invertArray(array):
    new = [] #T(n)=c1
    for i in range (0, len(array)): #T(n)=c2*n
        new.append(array[len(array)-1-i]) #T(n)=c3*n*(n-1)
    return new #T(n)=c4

array = [] #T(n)=c5
num = int(input()) #T(n)=c6
while num!=-1: #T(n)=c7*n
    array.append(num) #T(n)=n*n
    num = int(input()) #T(n)=c6*n

print(array) 
print(invertArray(array))

#La complejidad para el peor de los casos es O(n^2)