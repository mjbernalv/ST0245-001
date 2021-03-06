class ArrayList:

    elements = []

    def __init__(self):
        self.elements = []  #T(n)=c1
        
    def size(self):
        return len(self.elements)  #T(n)=c2

    def get(self, index):
        return self.elements[index]   #T(n)=c3

    def add(self, object):
        self.elements.append(object)   #T(n)=n

    def addInIndex(self, index, object):
        self.elements = self.elements[:index]+[object]+self.elements[index:]
        #self.elements.insert(index,object) #T(n)=n

    def removeInIndex(self,index):
        self.elements=self.elements[:index]+self.elements[index+1:]
        #self.elements.pop(index) #T(n)=n

    def toString(self):
        return self.elements  #T(n)=c4

#Complejidad en el peor de los casos: T(n)=n+c / O(n)

#La complejidad si permite que sea utilizado con millones de abejas, ya que esta es
#O(n), donde n es la cantidad de abejas que son agregadas, sin embargo es posible que 
#otras estructuras de datos sean más eficientes.

array = ArrayList()
array.add(1)
array.add(2)
array.add(3)
array.add(4)
print(array.size())
print(array.toString())
print(array.get(2))
array.addInIndex(2,5)
print(array.size())
print(array.toString())
array.removeInIndex(3)
print(array.size())
print(array.toString())