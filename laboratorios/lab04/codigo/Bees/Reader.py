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

    def getCollisions(self, midX, midY, midZ, diagonal):
        if diagonal > 100:
            octree = Octree()
            octree.octree(self.bees, self.mins, midX, midY, midZ)
        else:
            self.collisions()

    def collisions(self):
        for bee in self.bees:
            print("[" , bee.latitude, ", ", bee.longitude, ", ", bee.altitude , "]")
