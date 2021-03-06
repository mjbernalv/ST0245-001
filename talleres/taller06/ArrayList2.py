import numpy as np

class ArrayList:

    capacity = 10

    def __init__(self, capacity=10, size=0):
        self.capacity = 10
        self.size = 0
        self.elements = np.zeros(capacity)
        # Complejidad en el peor caso: O(1) (cuando el arreglo está lleno)
 
    def size(self):
        return self.size
        # Complejidad en el peor caso: O(1) (cuando el arreglo está lleno)
    
    def get(self, index):
        return self.elements[index]
        # Complejidad en el peor caso: O(1) (cuando el arreglo está lleno)
    
    def add(self, object):
        if self.size == self.elements.size:
           new = np.zeros(self.elements.size*1.5)
           for i in range(0, self.elements.size): # O(n)
              new[i] = self.elements[i]  # O(n)
           self.elements = new
        else:
            self.elements[self.size] = object                                               # - - > C10
        self.size = self.size + 1  
        # Complejidad en el peor caso: O(n) (cuando el arreglo está lleno)
 
    def addInIndex(self, index, object):
        try:
            if index<=self.size:
                new = np.zeros(self.elements.size+1)
                for i in range (0, index):
                    new[i]= self.elements[i]
                new[index]=object
                for j in range(index+1, self.elements.size):
                    new[j] = self.elements[j-1]
                self.elements = new
                self.size+=1
        except:
            print("index out of bounds exception")
        # Complejidad en el peor caso: O(n) (cuando el arreglo está lleno)

    def removeInIndex(self, index):
        try:
            if index<self.size:
                new = np.zeros(self.elements.size-1)
                for j in range(0, self.elements.size-1):
                    if self.elements[j]!=self.elements[index]:
                        new[j] = self.elements[j]
                self.elements = new
                self.size-=1
        except:
            print("index out of bounds exception")
        # Complejidad en el peor caso: O(n) (cuando el arreglo está lleno)
            
    def toString(self):
        return self.elements
    # Complejidad en el peor caso: O(1) (cuando el arreglo está lleno)

#Complejidad en el peor de los casos: T(n)=n+c / O(n)

#La complejidad si permite que sea utilizado con millones de abejas, ya que esta es
#O(n), donde n es la cantidad de abejas que son agregadas, sin embargo es posible que 
#otras estructuras de datos sean más eficientes.

array = ArrayList()
array.add(1)
array.add(2)
array.add(3)
array.add(4)
print(array.size)
print(array.toString())
print(array.get(2))
array.addInIndex(2,5)
array.addInIndex(5,4)
print(array.size)
print(array.toString())
array.removeInIndex(3)
array.removeInIndex(7)
print(array.size)
print(array.toString())