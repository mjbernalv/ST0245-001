class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __str__(self):
        return "" + self.data
    
class DoublyLinkedListMM():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self,index): #O(n)
        try:
            temp = self.head
            for i in range (0,index):
                temp = temp.next
            return temp.data
        except:
            print("Invalid position")

    def add(self, element, index=0): #O(1) for beginning and end, and O(n) for any other position
        try:
            new = Node(element)
            if self.head == None:
                self.head = new
                self.tail = self.head
            elif index == self.size or index ==-1:
                new.previous = self.tail
                self.tail.next = new
                self.tail = new
            elif index == 0:
                new.next = self.head
                self.head.previous = new
                self.head = new
            else:
                prev = self.head
                for i in range (index-1):
                    prev = prev.next
                new.previous = prev
                new.next = prev.next
                new.next.previous = new
                prev.next = new
            self.size += 1
        except:
            print("Invalid position")
       
    def size(self): #O(1)
        return self.size
      
    def remove(self, index): #O(1) for beginning and end, and O(n) for any other position
        try:
            if self.head == None:
                print("The list is empty")
            elif index == 0 and self.size == 1:
                self.head = None
                self.tail = None
            elif index == 0:
                self.head = self.head.next
            elif index == -1 or index == self.size-1:
                self.tail = self.tail.previous
                self.tail.next = None
            elif index == self.size-2:
                prev = self.head
                for i in range(index-1):
                    prev = prev.next
                self.tail.previous = prev
                prev.next = self.tail
            else:
                temp = self.head
                for i in range (index-1):
                    temp = temp.next
                temp.next.next.previous = temp.previous
                temp.next = temp.next.next
            self.size -= 1
        except:
            print("Invalid position")     
   
    def contains(self, element): #O(n)
        temp = self.head
        while temp != None:
            if temp.data==element:
                return True
            temp = temp.next
        return False
    
    def containsPosition(self, element): #O(n)
        temp = self.head
        count = 0
        while temp != None:
            if temp.data==element:
                return count
            temp = temp.next
            count+=1
        return None  #Cuando el elemento no existe
    
    def toString(self): #O(n)
        string = ""
        current = self.head
        while current!=None:
            string = string + str(current.data)
            current = current.next
        return string

class Main():
    l = DoublyLinkedListMM()
    l.add(1)
    l.add(2)
    l.add(3,-1)
    l.add(4, 3)
    l.add(5,2)
    print(l.toString())
    print(l.size)
    l.remove(1)
    l.remove(0)
    print(l.size)
    print(l.toString())
    print(l.get(2))
    print(l.contains(3))