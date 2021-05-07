from Octree import Octree
from Bees import Bees
import math

class Reader():
    def __init__(self):
        self.minX = math.inf
        self.maxX = -math.inf
        self.minY = math.inf
        self.maxY = -math.inf
        self.minZ = math.inf
        self.maxZ = -math.inf
        self.mins = []*3
        self.bees = []

    def read(self, name):
        file = open(name, 'r')
        text = file.read()
        file.close()
        rows = text.split("\n")
        print("The set of " + str(len(rows)-2) + " bees are: [x, y, z]")
        for row in rows:
            column = row.split(",")

            if column[0]=="Coordenada x de la abeja":
                continue
            if len(column)<3:
                break

            currX = float(column[0])
            currY = float(column[1])
            currZ = float(column[2])

            self.addBee(currX, currY, currZ)

        self.mins = [self.minX, self.minY, self.minZ] 
        midX = (self.minX - self.maxX)/2
        midY = (self.maxY - self.minY)/2
        midZ = (self.maxZ - self.minZ)/2

        #ph = math.sqrt(math.pow(midX*111325, 2)+math.pow(midY*111325,2))
        #diagonal = math.sqrt(math.pow(ph, 2)+math.pow(midZ, 2))

        print("")
        print("The bees that are in danger of colliding are:")

        octree = Octree()
        octree.octree(self.bees, self.mins, midX, midY, midZ)

    def addBee(self, currX, currY, currZ):
        if currX > self.maxX:
            self.maxX = currX
        if currX < self.minX:
            self.minX = currX
        if currY > self.maxY:
            self.maxY = currY
        if currY < self.minY:
            self.minY = currY
        if currZ > self.maxZ:
            self.maxZ = currZ
        if currZ < self.minZ:
            self.minZ = currZ
        
        bee = Bees(currX, currY, currZ)
        self.bees.append(bee)
        print(bee.__str__())

    '''def collisions(self):
        for bee in self.bees:
            print("[" , bee.latitude, ", ", bee.longitude, ", ", bee.altitude , "]")'''
