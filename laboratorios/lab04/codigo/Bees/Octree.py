from Bees import Bees
import math
from collections import deque

class Octree():
    def octree(self, bees, mins, midX, midY, midZ):
        self.midX = midX
        self.midY = midY
        self.midZ = midZ
        octree = []
        for i in range (8):
            sectors = deque()
            octree.append(sectors)
        
        for i in range(len(bees)):
            bee = bees.pop()
            sector = self.hashing(bee, mins)
            octree[sector].insert(0, bee)

        diagonal = math.sqrt(math.pow(self.midX*111325, 2)+math.pow(self.midY*111325,2)+math.pow(self.midZ*111325,2))
        if diagonal > 100:
            for i in range (8):
                if len(octree[i])>1:
                    self.newOctree(octree[i], mins, i)
        else:
            for i in range (8):
                if len(octree[i])>0:
                    self.collisions(octree[i])

    def hashing(self, bee, mins):
        if bee.latitude <= mins[0]+self.midX:
            if bee.longitude <= mins[1]+self.midY:
                if bee.altitude <= mins[2]+self.midZ:
                    return 0
                else:
                    return 1

    def newOctree(self, bees, mins, sector):
        if sector == 0:
            self.octree(bees, mins, self.midX/2, self.midY/2, self.midZ/2)
        elif sector == 1:
            newZ = mins[2]+self.midZ
            mins.pop(2)
            mins.insert(2, newZ)
            self.octree(bees, mins, self.midX/2, self.midY/2, self.midZ/2)

    def collisions(self, bees):
        for bee in bees:
            print("[" , bee.latitude, ", ", bee.longitude, ", ", bee.altitude , "]")