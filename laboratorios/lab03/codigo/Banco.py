from collections import deque
class Queue():
    def __init__(self):
        self.items = []
        self.size = 0
    
    def enqueque(self, data):  #O(1)
        self.items.insert(0, data)
        self.size+=1

    def dequeque(self): #O(1)
        data = self.items.pop()
        self.size -=1
        return data
        
    def getSize(self): #O(1)
        return self.size

class Banco():
    def __init__(self, f1, f2, f3, f4):
        self.fila1 = f1
        self.fila2 = f2
        self.fila3 = f3
        self.fila4 = f4

    def getFila1(self):
        return self.fila1
    
    def getFila2(self):
        return self.fila2

    def getFila3(self):
        return self.fila3

    def getFila4(self):
        return self.fila4

class Main():
    def simulator(banco):
        final = Queue()
        while(banco.getFila1().getSize()>0 or banco.getFila2().getSize()>0 or banco.getFila3().getSize()>0 or banco.getFila4().getSize()>0): #O(n) n = longest queue
            if banco.getFila1().getSize()>0:
                final.enqueque(banco.getFila1().dequeque())
            if banco.getFila2().getSize()>0:
                final.enqueque(banco.getFila2().dequeque())
            if banco.getFila3().getSize()>0:
                final.enqueque(banco.getFila3().dequeque())
            if banco.getFila4().getSize()>0:
                final.enqueque(banco.getFila4().dequeque())
        
        cajero1 = "Cajero 1 atiende a: "
        cajero2 = "Cajero 2 atiende a: "
        for i in range (final.getSize()): #O(m) m = number of people in the bank
            if final.getSize()>1:
                print(cajero1, final.dequeque())
                print(cajero2, final.dequeque())
            elif final.getSize()>0:
                print(cajero1, final.dequeque())
        return

    fila1 = Queue()
    fila1.enqueque("Maria")
    fila1.enqueque("Martin")
    fila1.enqueque("Jose")
    fila2 = Queue()
    fila2.enqueque("Camila")
    fila2.enqueque("Camilo")
    fila3 = Queue()
    fila3.enqueque("Felipe")
    fila4 = Queue()
    fila4.enqueque("Tomás")
    fila4.enqueque("Andrea")

    banco = Banco(fila1, fila2, fila3, fila4)
    simulator(banco)

#Complexity: O(m) where n is the number of people in the bank