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
            elif index==-1:
                new = Node(element)
                if self.head == None:
                    self.head = new
                else:
                    prev = self.head
                    while prev.next!=None:
                        prev = prev.next
                    prev.next = new
                self.size+=1
            else:
                new = Node(element)
                prev = self.head
                for i in range (0, index-1):
                    prev = prev.next
                temp = prev.next
                prev.next = new
                new.next = temp
                self.size+=1
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
        return None  #Cuando el elemento no existe
    
    def toString(self):
        string = ""
        current = self.head
        while current!=None:
            string = string + str(current.data)
            current = current.next
        return string


def fix(text):
    new = LinkedListMM()
    temp = ""
    x = False
    for i in range(len(text)):
        if text[i]!="[" and text[i]!="]":
            temp = temp + text[i]
        if text[i]=="[":
            if x:
                new.add(temp, 0)
                temp = ""
                x = False
            else:
                new.add(temp, -1)
                temp = ""
            x = True
        if text[i]=="]":
            if x:
                new.add(temp, 0)
                temp = ""
                x = False
            else:
                new.add(temp, -1)
                temp = ""
        if i == len(text)-1:
            if x:
                new.add(temp, 0)
            else:
                new.add(temp, -1)
    return new.toString()
    
print(fix("This_is_a_[Beiju]_text"))
print(fix("[[]][][]Happy_Birthday_to_Tsinghua_University"))
print(fix("asd[fgh[jkl"))
print(fix("asd[fgh[jkl["))
print(fix("[[a[[d[f[[g[g[h[h[dgd[fgsfa[f"))
print(fix("asd[gfh[[dfh]hgh]fdfhd[dfg[d]g[d]dg"))

#Complexity: O(n) n = length of the text