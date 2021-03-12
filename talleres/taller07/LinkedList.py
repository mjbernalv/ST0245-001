class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return "" + self.data
    

class LinkedListMM():
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self,index):
        try:
            temp = self.head
            for i in range (0,index):
                temp = temp.next
            return temp.data
        except:
            print("Invalid position")

    def add(self, element, index=0):
        try:
            if index==0:
                new = Node(element)
                new.next = self.head
                self.head = new
                self.size+=1
                #Complejidad: O(1)

            else:
                new = Node(element)
                prev = self.head
                for i in range (0, index-1):
                    prev = prev.next
                temp = prev.next
                prev.next = new
                new.next = temp
                self.size+=1
                #Complejidad: O(n)

        except:
            print("Invalid position")

       
    def size(self):
        return self.size
      
    def remove(self, index):
        try:
            if index==0:
                self.head = self.head.next
                self.size-=1
            else:
                prev = self.head
                for i in range (0, index-1):
                    prev = prev.next
                temp = prev.next
                prev.next = temp.next
                self.size-=1
        except:
            print("Invalid position")
            
   
    def contains(self, element):
        temp = self.head
        while temp != None:
            if temp.data==element:
                return True
            temp = temp.next
        return False
    
    def containsPosition(self, element):
        temp = self.head
        count = 0
        while temp != None:
            if temp.data==element:
                return count
            temp = temp.next
            count+=1
        return -1  #Cuando el elemento no existe

class Main():
    l = LinkedListMM()
    l.add(1)
    l.add(2)
    l.add(3)
    l.add(4,1)
    print(l.get(0))
    print(l.get(1))
    print(l.get(2))
    print(l.get(3))
    l.add(6,10)
    print("Position of #1:",l.containsPosition(1))
    print("Position of #5:",l.containsPosition(5))
    print(l.contains(1))
    print("Size:",l.size)
    l.remove(0)
    l.remove(1)
    print(l.get(0))
    print(l.get(1))
    print("Size:",l.size)
    print(l.contains(3))
    print("Position of #1:",l.containsPosition(1))
    print(l.contains(6))