class GraphAL():

    def __init__(self, size):
        self.size = size
        self.list = [[] for i in range(size)]

    def addArc(self, vertex, edge, weight):
        self.list[vertex].append((edge, weight))

    def getSuccessors(self, vertex):
        sucessors = []
        for d in self.list[vertex]:
            sucessors.append(d[0])
        return sucessors

    def getWeight(self, source, destination):
        for i in self.list[source]:
            if i[0] == destination:
                return i[1]

    def __str__(self):
        return f'{self.list}'
