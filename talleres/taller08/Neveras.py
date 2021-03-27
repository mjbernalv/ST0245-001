class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return "" + self.data

class Stack():
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        node = Node(data)
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node
        self.size +=1
    
    def pop(self):
        if self.top:
            data = self.top.data
            self.size-=1
            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None
            return data
        else:
            return None
    
    def peek(self):
        if self.top:
            return self.top.data
        else:
            return None

    def getSize(self):
        return self.size

class Queue():
    def __init__(self):
        self.items = []
        self.size = 0
    
    def enqueque(self, data):
        self.items.insert(0, data)
        self.size+=1

    def dequeque(self):
        data = self.items.pop()
        self.size -=1
        return data
        
    def getSize(self):
        return self.size

class Nevera():
    def __init__(self, code, desc):
        self.code = code
        self.desc = desc
    
    def getCode(self):
        return self.code
    
    def getDesc(self):
        return self.desc

    def toString(self):
        return "(" + str(self.code) + "," + str(self.desc) + ")"

class Solicitudes():
    def __init__(self, name, num):
        self.name = name
        self.num = num
    
    def getName(self):
        return self.name

    def getNum(self):
        return self.num

def Distribuir(almacen, solicitudes):
    neveras = Stack()
    solicitud = Queue()

    for i in range(len(almacen)):
        num = almacen[i][0]
        marca = almacen[i][1]
        nevera = Nevera(num, marca)
        neveras.push(nevera)
    
    for j in range (len(solicitudes)-1, -1, -1):
        nombre = solicitudes[j][0]
        cantidad = solicitudes[j][1]
        sol = Solicitudes(nombre, cantidad)
        solicitud.enqueque(sol)

    array = []

    for l in range(solicitud.getSize()):
        temp = "("
        curr = solicitud.dequeque()
        temp = temp + curr.getName() + ", ["
        for m in range(curr.getNum()):
            if neveras.getSize()==0:
                temp = temp + " No hay más neveras disponibles "
                break
            else:
                nev = neveras.pop()
                temp = temp + nev.toString() + ","
        temp = temp[:len(temp)-1] + "])"
        array.append(temp)
    
    return array

almacen = [(1,"haceb"), (2,"lg"), (3,"ibm"), (4,"haceb"), (5,"lg"), (6,"ibm"),(7,"haceb"), (8,"lg"), (9,"ibm"),(8,"lg"), (9,"ibm")]
solicitudes = [("eafit", 10), ("la14", 2), ("olimpica", 4), ("éxito", 1)]

print(Distribuir(almacen, solicitudes))