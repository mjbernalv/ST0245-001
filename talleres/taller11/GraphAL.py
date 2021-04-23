class GraphAL():

    def __init__(self, size):
        self.size = size
        self.list = [[] for i in range(size)]

    def addArc(self, vertex, edge, weight):
        self.list[vertex].append((edge, weight))

    def getSuccessors(self, vertex):
        sucessors = []
        for i in range (len(self.list[vertex])):
            sucessors.append(self.list[vertex][i])
        return sucessors

    def getWeight(self, source, destination):
        for i in self.list[source]:
            if i[0] == destination:
                return i[1]

    def __str__(self):
        return f'{self.list}'

graph = GraphAL(3)
graph.addArc(0, 3, 10)
print(graph)
print(graph.getWeight(0, 3))
graph.addArc(0, 4, 7)
graph.addArc(1, 5, 2)
print(graph)
print(graph.getSuccessors(0))